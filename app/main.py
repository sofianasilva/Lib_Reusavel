from fastapi import FastAPI
from .views.pessoa_routes import router as pessoa_router
from .views.endereco_routes import router as endereco_router

app = FastAPI(
    title="API Pessoa Endereço",
    description="API para registrar pessoas e endereços usando biblioteca reutilizável",
    version="1.0.0"
)

app.include_router(pessoa_router)
app.include_router(endereco_router)

@app.get("/")
def root():
    return {"mensagem": "API Pessoa Endereço funcionando"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)