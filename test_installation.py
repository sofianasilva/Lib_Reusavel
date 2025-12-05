#!/usr/bin/env python3
"""
Script para testar se a instalação está funcionando corretamente
"""

def test_imports():
    """Testa se todas as importações estão funcionando"""
    print("🧪 Testando importações...")
    
    try:
        # Testar biblioteca do TestPyPI
        from repositorio_generico import Pessoa, Endereco, RepositorioPessoa, RepositorioEndereco
        print("✅ repositorio-generico: OK")
        
        # Testar FastAPI
        from fastapi import FastAPI
        print("✅ FastAPI: OK")
        
        # Testar Uvicorn
        import uvicorn
        print("✅ Uvicorn: OK")
        
        # Testar Pydantic
        from pydantic import BaseModel
        print("✅ Pydantic: OK")
        
        return True
        
    except ImportError as e:
        print(f"❌ Erro de importação: {e}")
        return False

def test_functionality():
    """Testa funcionalidade básica"""
    print("\n🔧 Testando funcionalidade...")
    
    try:
        from repositorio_generico import Pessoa, RepositorioPessoa
        
        # Testar criação de pessoa
        repo = RepositorioPessoa()
        pessoa = Pessoa(nome="Teste", idade=25, email="teste@exemplo.com")
        pessoa_salva = repo.salvar(pessoa)
        
        if pessoa_salva.id is not None:
            print("✅ Criação de pessoa: OK")
            
            # Testar busca
            pessoa_encontrada = repo.buscar_por_id(pessoa_salva.id)
            if pessoa_encontrada and pessoa_encontrada.nome == "Teste":
                print("✅ Busca de pessoa: OK")
                return True
            else:
                print("❌ Busca de pessoa: FALHOU")
                return False
        else:
            print("❌ Criação de pessoa: FALHOU")
            return False
            
    except Exception as e:
        print(f"❌ Erro de funcionalidade: {e}")
        return False

def main():
    print("🚀 Teste de Instalação - API Pessoa Endereço")
    print("=" * 50)
    
    # Testar importações
    if not test_imports():
        print("\n❌ Falha nos testes de importação!")
        print("Execute: python install.py")
        return False
    
    # Testar funcionalidade
    if not test_functionality():
        print("\n❌ Falha nos testes de funcionalidade!")
        return False
    
    print("\n🎉 Todos os testes passaram!")
    print("✅ A instalação está funcionando corretamente!")
    print("\n🚀 Para executar a API:")
    print("   python -m app.main")
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)