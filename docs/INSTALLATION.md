# Guia Completo de Instalação - EchoX

## 📋 Requisitos do Sistema

### Mínimos
- **OS**: Windows 10 ou superior
- **RAM**: 512 MB
- **Espaço em Disco**: 50 MB (sem música)
- **Processador**: Intel Core i3 ou equivalente

### Recomendados
- **OS**: Windows 11
- **RAM**: 2 GB ou mais
- **Espaço em Disco**: 100 MB
- **Processador**: Intel Core i5 ou superior

---

## 🚀 Opção 1: Instalador Windows (Recomendado)

### Passos

1. **Baixar o Instalador**
   - Acesse [Releases](https://github.com/akra2017linux-rgb/EchoX/releases)
   - Procure pela versão mais recente
   - Clique em `EchoX-Setup.exe`

2. **Executar o Instalador**
   - Abra o arquivo `EchoX-Setup.exe`
   - Selecione idioma (se aplicável)
   - Clique em "Next"

3. **Aceitar Termos**
   - Leia e aceite os termos de licença
   - Clique em "I Agree"

4. **Selecionar Pasta de Instalação**
   - Padrão: `C:\Program Files\EchoX`
   - Modifique se desejar
   - Clique em "Next"

5. **Criar Atalhos**
   - ✓ Desktop shortcut (recomendado)
   - ✓ Start Menu shortcut
   - Clique em "Next"

6. **Instalar**
   - Clique em "Install"
   - Aguarde a conclusão
   - Clique em "Finish"

7. **Lançar**
   - Duplo-clique no atalho do Desktop
   - Ou encontre "EchoX" no Menu Iniciar

---

## 💻 Opção 2: Instalação a partir do Código-Fonte

### Pré-requisitos
- Git instalado
- Python 3.8 ou superior
- pip (geralmente vem com Python)

### Passos

#### 1. Clone o Repositório

```bash
git clone https://github.com/akra2017linux-rgb/EchoX.git
cd EchoX
```

#### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
```

#### 3. Ative o Ambiente Virtual

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

#### 4. Instale as Dependências

```bash
pip install -r requirements.txt
```

#### 5. Execute o Aplicativo

```bash
python main.py
```

---

## 🔧 Construir o Executável (Para Desenvolvedores)

### Pré-requisitos
- Seguir os passos da Opção 2 acima
- PyInstaller já estará instalado via `requirements.txt`

### Passos

#### 1. Prepare o Ambiente

```bash
# Certifique-se de estar no diretório do projeto
cd EchoX

# Ative o ambiente virtual
venv\Scripts\activate
```

#### 2. Crie o Executável

```bash
pyinstaller main.spec
```

#### 3. Localize o Executável

O arquivo estará em: `dist/EchoX.exe`

#### 4. Teste

```bash
dist\EchoX.exe
```

---

## 📦 Criar o Instalador Windows (Inno Setup)

### Pré-requisitos
- [Inno Setup 6.0+](https://jrsoftware.org/isdl.php) instalado
- Executável criado (veja seção anterior)

### Passos

1. **Abra o Inno Setup**
   - Procure por "Inno Setup Compiler" no Menu Iniciar

2. **Abra o Script**
   - File → Open
   - Navegue para `build/inno_setup.iss`
   - Clique em "Abrir"

3. **Compile**
   - Menu: Build → Compile
   - Ou pressione: Ctrl+F9
   - Aguarde a conclusão

4. **Localize o Instalador**
   - Arquivo salvo em: `build/Output/EchoX-Setup.exe`

5. **Distribua**
   - Faça upload para [Releases](https://github.com/akra2017linux-rgb/EchoX/releases)
   - Compartilhe com usuários

---

## 🆘 Solução de Problemas

### Erro: "Python não é reconhecido"

**Solução:**
1. Verifique se Python está instalado: `python --version`
2. Se não estiver, baixe de [python.org](https://www.python.org)
3. **Importante**: Durante a instalação, marque "Add Python to PATH"
4. Reinicie o Command Prompt

### Erro: "pip não é reconhecido"

**Solução:**
```bash
python -m pip install --upgrade pip
```

### Erro: "Módulo não encontrado (customtkinter, pygame, etc.)"

**Solução:**
```bash
pip install --upgrade -r requirements.txt
```

### Erro: "Acesso negado ao instalar"

**Solução:**
- Execute como Administrador
- Ou use: `pip install --user -r requirements.txt`

### O aplicativo não inicia

**Solução:**
1. Verifique se o ambiente virtual está ativado
2. Reinstale as dependências: `pip install --upgrade -r requirements.txt`
3. Verifique os logs de erro
4. Reporte em [Issues](https://github.com/akra2017linux-rgb/EchoX/issues)

---

## 📝 Próximos Passos

1. Abra o EchoX
2. Clique em "Add Folder" (ou similar)
3. Selecione a pasta com suas músicas MP3
4. Aguarde a varredura
5. Comece a ouvir! 🎵

---

## 📞 Suporte

Se tiver problemas:
- Verifique as [FAQ](FAQ.md)
- Abra uma [Issue](https://github.com/akra2017linux-rgb/EchoX/issues)
- Participe das [Discussions](https://github.com/akra2017linux-rgb/EchoX/discussions)

**Happy listening!** 🎧
