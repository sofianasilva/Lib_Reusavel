from repositorio_generico import Endereco, RepositorioEndereco, RepositorioPessoa

class EnderecoController:
    def __init__(self):
        self.repositorio_endereco = RepositorioEndereco()
        self.repositorio_pessoa = RepositorioPessoa()
    
    def criar_endereco(self, logradouro: str, numero: str, estado: str, 
                      cidade: str, bairro: str, pessoa_id: int) -> Endereco:
        """Cria um novo endereço"""
        #se pessoa existe
        pessoa = self.repositorio_pessoa.buscar_por_id(pessoa_id)
        if not pessoa:
            raise ValueError(f"Pessoa com id {pessoa_id} não encontrada")
        
        endereco = Endereco(
            logradouro=logradouro,
            numero=numero,
            estado=estado,
            cidade=cidade,
            bairro=bairro,
            pessoa_id=pessoa_id
        )
        return self.repositorio_endereco.salvar(endereco)