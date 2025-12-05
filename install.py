#!/usr/bin/env python3
"""
Script de instalação universal para Windows, Linux e macOS
"""
import subprocess
import sys
import os

def run_command(command):
    """Executa comando e mostra output"""
    print(f"Executando: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")
        return False

def main():
    print("🚀 Instalador Universal - API Pessoa Endereço")
    print("=" * 50)
    
    # Verificar se está em ambiente virtual
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  AVISO: Recomendamos usar um ambiente virtual!")
        print("Execute: python -m venv venv")
        if os.name == 'nt':  # Windows
            print("         venv\\Scripts\\activate")
        else:  # Linux/macOS
            print("         source venv/bin/activate")
        print()
        
        resposta = input("Continuar mesmo assim? (s/N): ").lower()
        if resposta != 's':
            print("Instalação cancelada.")
            return
    
    print("📦 Instalando dependências...")
    
    # Instalar biblioteca do TestPyPI
    print("\n1. Instalando repositorio-generico do TestPyPI...")
    if not run_command("pip install -i https://test.pypi.org/simple/ repositorio-generico==1.0.1"):
        print("❌ Falha ao instalar repositorio-generico")
        return
    
    # Instalar FastAPI
    print("\n2. Instalando FastAPI...")
    if not run_command("pip install fastapi==0.104.1"):
        print("❌ Falha ao instalar FastAPI")
        return
    
    # Instalar Uvicorn
    print("\n3. Instalando Uvicorn...")
    if not run_command("pip install uvicorn[standard]==0.24.0"):
        print("❌ Falha ao instalar Uvicorn")
        return
    
    # Instalar Pydantic
    print("\n4. Instalando Pydantic...")
    if not run_command("pip install pydantic==2.9.2"):
        print("❌ Falha ao instalar Pydantic")
        return
    
    print("\n✅ Instalação concluída com sucesso!")
    print("\n🚀 Para executar a API:")
    print("   python -m app.main")
    print("\n📖 Documentação estará disponível em:")
    print("   http://localhost:8000/docs")

if __name__ == "__main__":
    main()