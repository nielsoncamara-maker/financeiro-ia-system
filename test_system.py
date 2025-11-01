#!/usr/bin/env python3
"""
Script de Teste e Verificação do Sistema
Verifica se todas as dependências e componentes estão funcionando
"""

import sys
import os

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def test_python_version():
    print_header("🐍 Testando Versão do Python")
    version = sys.version_info
    print(f"Versão: Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Versão compatível!")
        return True
    else:
        print("❌ Python 3.8+ necessário!")
        return False

def test_dependencies():
    print_header("📦 Testando Dependências")
    
    dependencies = [
        'flask',
        'flask_cors',
        'pandas',
        'openpyxl',
        'xlrd',
        'anthropic'
    ]
    
    all_ok = True
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✅ {dep}")
        except ImportError:
            print(f"❌ {dep} - FALTANDO!")
            all_ok = False
    
    return all_ok

def test_file_structure():
    print_header("📁 Testando Estrutura de Arquivos")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html',
        'README.md',
        'DEPLOY_GUIDE.md'
    ]
    
    all_ok = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - FALTANDO!")
            all_ok = False
    
    return all_ok

def test_directories():
    print_header("📂 Testando Diretórios")
    
    required_dirs = ['uploads', 'outputs', 'templates']
    
    all_ok = True
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name}/")
        else:
            print(f"⚠️  {dir_name}/ - Será criado automaticamente")
    
    return all_ok

def test_app_import():
    print_header("🔧 Testando Importação do App")
    
    try:
        from app import app
        print("✅ App Flask importado com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar: {e}")
        return False

def test_api_key():
    print_header("🤖 Testando Configuração da IA")
    
    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    
    if api_key and len(api_key) > 10:
        print("✅ API Key configurada!")
        print("   IA avançada será utilizada")
    else:
        print("⚠️  API Key não configurada")
        print("   Sistema funcionará com IA básica (regras)")
        print("   Para IA avançada, configure ANTHROPIC_API_KEY")
    
    return True

def print_summary(results):
    print_header("📊 RESUMO DOS TESTES")
    
    total = len(results)
    passed = sum(results)
    
    print(f"\nTestes executados: {total}")
    print(f"✅ Passou: {passed}")
    print(f"❌ Falhou: {total - passed}")
    
    if passed == total:
        print("\n🎉 TUDO FUNCIONANDO PERFEITAMENTE!")
        print("\n📝 Próximos Passos:")
        print("   1. Execute: python app.py")
        print("   2. Acesse: http://localhost:5000")
        print("   3. Faça upload de um extrato para testar")
        print("\n   Ou siga DEPLOY_GUIDE.md para subir online!")
        return True
    else:
        print("\n⚠️  ALGUNS TESTES FALHARAM")
        print("\n🔧 Como resolver:")
        print("   1. Instale dependências: pip install -r requirements.txt")
        print("   2. Verifique se todos os arquivos estão presentes")
        print("   3. Execute este teste novamente")
        return False

def main():
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║     🤖 SISTEMA DE AUTOMAÇÃO FINANCEIRA COM IA         ║
    ║              Teste de Verificação                     ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
    """)
    
    results = []
    
    # Executa todos os testes
    results.append(test_python_version())
    results.append(test_dependencies())
    results.append(test_file_structure())
    results.append(test_directories())
    results.append(test_app_import())
    results.append(test_api_key())
    
    # Mostra resumo
    success = print_summary(results)
    
    # Retorna código de saída
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
