from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..controllers.pessoa_controller import PessoaController

router = APIRouter()
controller = PessoaController()

class PessoaCreate(BaseModel):
    nome: str
    idade: int
    email: str

class PessoaResponse(BaseModel):
    id: int
    nome: str
    idade: int
    email: str

@router.post("/persons", response_model=PessoaResponse)
def registrar_pessoa(pessoa_data: PessoaCreate):
    """Rota para registrar uma pessoa"""
    pessoa = controller.criar_pessoa(
        nome=pessoa_data.nome,
        idade=pessoa_data.idade,
        email=pessoa_data.email
    )
    return PessoaResponse(
        id=pessoa.id,
        nome=pessoa.nome,
        idade=pessoa.idade,
        email=pessoa.email
    )

@router.get("/persons/{pessoa_id}")
def listar_pessoa(pessoa_id: int):
    """Rota para listar uma pessoa com todos os endereços"""
    resultado = controller.obter_pessoa_com_enderecos(pessoa_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    return resultado