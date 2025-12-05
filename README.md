## Execução

```bash
cd caminho/para/seu/projeto

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -i https://test.pypi.org/simple/ repositorio-generico==1.0.1

pip install fastapi==0.104.1 uvicorn[standard]==0.24.0 pydantic==2.5.0

python -m app.main
```

#