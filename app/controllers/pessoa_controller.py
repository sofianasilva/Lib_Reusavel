from typing import Optional, Dict, Any
from repositorio_generico import Pessoa, RepositorioPessoa, RepositorioEndereco

class PessoaController:
    def __init__(self):
        self.repositorio_pessoa = RepositorioPessoa()
        self.repositorio_endereco = RepositorioEndereco()
    
    def criar_pessoa(self, nome: str, idade: int, email: str) -> Pessoa:
        """Cria uma nova pessoa"""
        pessoa = Pessoa(nome=nome, idade=idade, email=email)
        return self.repositorio_pessoa.salvar(pessoa)
    
    def obter_pessoa_com_enderecos(self, pessoa_id: int) -> Optional[Dict[str, Any]]:
        """Obtém pessoa com todos os endereços"""
        pessoa = self.repositorio_pessoa.buscar_por_id(pessoa_id)
        if not pessoa:
            return None
        
        enderecos = self.repositorio_endereco.buscar_por_pessoa_id(pessoa_id)
        
        return {
            "pessoa": {
                "id": pessoa.id,
                "nome": pessoa.nome,
                "idade": pessoa.idade,
                "email": pessoa.email
            },
            "enderecos": [
                {
                    "id": endereco.id,
                    "logradouro": endereco.logradouro,
                    "numero": endereco.numero,
                    "estado": endereco.estado,
                    "cidade": endereco.cidade,
                    "bairro": endereco.bairro,
                    "pessoa_id": endereco.pessoa_id
                }
                for endereco in enderecos
            ]
        }