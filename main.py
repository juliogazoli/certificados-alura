import os
import re
import asyncio
from getpass import getpass
from playwright.async_api import async_playwright
from tqdm import tqdm


DOWNLOAD_DIR = "certificados"
BASE_URL = "https://cursos.alura.com.br"
CONCURRENCY = 5


def extrair_nome(url):
    nome = url.split("/course/")[1].split("/formalCertificate")[0]
    nome = nome.replace("/", "-")
    nome = re.sub(r"[^\w\s-]", "", nome)
    return nome


async def baixar_certificado(context, url, sem, pbar):
    async with sem:
        page = await context.new_page()

        try:
            await page.goto(url)
            await page.wait_for_load_state("networkidle")

            nome = extrair_nome(url)
            caminho = os.path.join(DOWNLOAD_DIR, f"{nome}.pdf")

            if not os.path.exists(caminho):
                await page.pdf(
                    path=caminho,
                    format="A4",
                    print_background=True
                )

        except Exception as e:
            print(f"\nErro em {url}: {e}")

        finally:
            await page.close()
            pbar.update(1)


async def run():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # entrada do usuário
    email = input("Digite seu e-mail: ")
    senha = getpass("Digite sua senha: ")
    usuario_alura = input("Digite seu usuário da Alura (verificar a URL do perfil): ")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # login
        await page.goto("https://cursos.alura.com.br/loginForm")
        await page.fill('input[name="username"]', email)
        await page.fill('input[name="password"]', senha)
        await page.click('button:has-text("Entrar")')

        # perfil
        await page.goto(f"https://cursos.alura.com.br/user/{usuario_alura}")

        await page.get_by_role("button", name="ver todos os cursos concluí").click()
        await page.wait_for_load_state("networkidle")

        links = page.locator("a.course-card__certificate")
        total = await links.count()

        certificados_urls = []

        for i in range(total):
            href = await links.nth(i).get_attribute("href")
            if href:
                url = BASE_URL + href
                url_formal = url.replace("certificate", "formalCertificate")
                certificados_urls.append(url_formal)

        certificados_urls = list(set(certificados_urls))

        print(f"Total: {len(certificados_urls)}")

        sem = asyncio.Semaphore(CONCURRENCY)

        # barra de progresso
        with tqdm(total=len(certificados_urls), desc="Baixando certificados") as pbar:

            tasks = [
                baixar_certificado(context, url, sem, pbar)
                for url in certificados_urls
            ]

            await asyncio.gather(*tasks)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(run())
