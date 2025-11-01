#!/bin/bash

echo "🚀 Testando Sistema de Automação Financeira com IA"
echo "=================================================="
echo ""

# Verifica Python
echo "✓ Verificando Python..."
python3 --version

echo ""
echo "✓ Instalando dependências..."
pip install -r requirements.txt --quiet

echo ""
echo "✓ Iniciando servidor Flask..."
echo ""
echo "🌐 Acesse: http://localhost:5000"
echo "📌 Pressione Ctrl+C para parar"
echo ""

python3 app.py
