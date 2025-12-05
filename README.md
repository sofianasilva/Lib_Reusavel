## Execução

### Instalação Universal (Windows, Linux, macOS)

#### Método 1: Usando requirements.txt (Recomendado)
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instalar todas as dependências
pip install -r requirements.txt

# Executar API
python -m app.main
```

#### Método 2: Script de Instalação Universal
```bash
# Executar script que instala tudo automaticamente
python install.py
```

#### Método 3: Instalação Manual
```bash
# Ativar ambiente virtual primeiro (ver comandos acima)

# Instalar biblioteca do TestPyPI
pip install -i https://test.pypi.org/simple/ repositorio-generico==1.0.1

# Instalar outras dependências
pip install fastapi==0.104.1 uvicorn[standard]==0.24.0 pydantic==2.9.2

# Executar API
python -m app.main
```

### Verificação da Instalação
```bash
# Testar se tudo está funcionando
python test_installation.py
```