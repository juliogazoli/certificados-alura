
# 📄 Download de Certificados da Alura

Script em Python para baixar automaticamente todos os certificados (formais) dos cursos concluídos na Alura e salvá-los em PDF.

---

## 🚀 Funcionalidades

* 🔐 Login automático na Alura
* 📚 Coleta de todos os cursos concluídos
* 📄 Download dos certificados formais (`formalCertificate`)
* ⚡ Download em paralelo (rápido)
* 📊 Barra de progresso no terminal
* ♻️ Evita baixar arquivos duplicados

---

## 📁 Estrutura

```id="8j3n4y"
.
├── main.py
├── certificados/
│   ├── curso-1.pdf
│   ├── curso-2.pdf
│   └── ...
```


---

## 📥 Como obter o projeto

### 🔹 Opção 1: Clonar com Git (recomendado)

Se você já tem o **Git** instalado:

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

---

### 🔹 Opção 2: Baixar como ZIP

1. Acesse o repositório no GitHub
2. Clique no botão **Code**
3. Clique em **Download ZIP**
4. Extraia o arquivo no seu computador
5. Abra a pasta extraída no terminal

---

## 📦 Instalando as dependências

Recomenda-se usar um ambiente virtual:

### 🔹 Criar ambiente virtual

```bash
python -m venv venv
```

### 🔹 Ativar ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Mac:**

```bash
source venv/bin/activate
```

---

### 🔹 Instalar dependências com `requirements.txt`

```bash
pip install -r requirements.txt
```

---

### 🔹 Instalar navegadores do Playwright

Após instalar as dependências, execute:

```bash
playwright install
```

---

## ✅ Pronto!

Agora você já pode rodar o script normalmente:

```bash
python main.py
```
