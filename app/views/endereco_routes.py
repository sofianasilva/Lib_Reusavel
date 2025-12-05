from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..controllers.endereco_controller import EnderecoController

router = APIRouter()
controller = EnderecoController()

class EnderecoCreate(BaseModel):
    logradouro: str
    numero: str
    estado: str
    cidade: str
    bairro: str
    pessoa_id: int

class EnderecoResponse(BaseModel):
    id: int
    logradouro: str
    numero: str
    estado: str
    cidade: str
    bairro: str
    pessoa_id: int

@router.post("/addresses", response_model=EnderecoResponse)
def registrar_endereco(endereco_data: EnderecoCreate):
    """Rota para registrar um endereço"""
    try:
        endereco = controller.criar_endereco(
            logradouro=endereco_data.logradouro,
            numero=endereco_data.numero,
            estado=endereco_data.estado,
            cidade=endereco_data.cidade,
            bairro=endereco_data.bairro,
            pessoa_id=endereco_data.pessoa_id
        )
        return EnderecoResponse(
            id=endereco.id,
            logradouro=endereco.logradouro,
            numero=endereco.numero,
            estado=endereco.estado,
            cidade=endereco.cidade,
            bairro=endereco.bairro,
            pessoa_id=endereco.pessoa_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))