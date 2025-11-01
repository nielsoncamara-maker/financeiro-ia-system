from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
import pandas as pd
import os
from datetime import datetime
import re
from io import BytesIO
import anthropic

app = Flask(__name__)
CORS(app)

# Configuração da API Claude (o usuário deve definir sua chave)
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')

# Configurações
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Dados fixos do sistema
CLIENTE_AVULSO = {
    'cpf': '69216118334',
    'tipo': 'R'  # Receber
}

FORNECEDOR_AVULSO = {
    'cnpj': '75882806000150',
    'tipo': 'P'  # Pagar
}

CONTA_BANCARIA = '237-2293-6721'


def classificar_com_ia(descricao, valor_credito, valor_debito):
    """
    Usa IA (Claude) para classificar o lançamento e sugerir centro de custo
    """
    
    # Regras básicas sem IA (fallback)
    if valor_credito and not valor_debito:
        # É entrada de dinheiro
        tipo = 'R'
        cnpj_cpf = CLIENTE_AVULSO['cpf']
        
        # Análise simples de palavras-chave para centro de custo
        descricao_lower = descricao.lower()
        if 'pix' in descricao_lower or 'transferencia' in descricao_lower:
            centro_custo = '1.01.001.0001'  # Receita de vendas
            observacao = 'Recebimento via PIX - Cliente Avulso'
        elif 'liquidacao' in descricao_lower or 'cobranca' in descricao_lower:
            centro_custo = '1.01.001.0001'  # Receita de vendas
            observacao = 'Recebimento de cobrança - Cliente Avulso'
        elif 'rentab' in descricao_lower or 'invest' in descricao_lower:
            centro_custo = '1.02.001.0001'  # Receita financeira
            observacao = 'Rendimento de investimento'
        else:
            centro_custo = '1.01.001.0001'  # Receita genérica
            observacao = 'Recebimento - Cliente Avulso'
            
    else:
        # É saída de dinheiro
        tipo = 'P'
        cnpj_cpf = FORNECEDOR_AVULSO['cnpj']
        
        # Análise simples de palavras-chave
        descricao_lower = descricao.lower()
        if 'tarifa' in descricao_lower or 'taxa' in descricao_lower:
            centro_custo = '2.01.004.0002'  # Despesas bancárias
            observacao = 'Tarifa bancária - Fornecedor Avulso'
        elif 'pagto' in descricao_lower or 'pagamento' in descricao_lower:
            centro_custo = '2.01.001.0001'  # Despesas operacionais
            observacao = 'Pagamento - Fornecedor Avulso'
        elif 'pix' in descricao_lower or 'transferencia' in descricao_lower:
            centro_custo = '2.01.001.0001'  # Despesas operacionais
            observacao = 'Pagamento via PIX - Fornecedor Avulso'
        elif 'saque' in descricao_lower:
            centro_custo = '2.01.005.0001'  # Retiradas
            observacao = 'Saque - Fornecedor Avulso'
        else:
            centro_custo = '2.01.001.0001'  # Despesa genérica
            observacao = 'Pagamento - Fornecedor Avulso'
    
    # Se tiver API key da Anthropic, usa IA para melhorar a classificação
    if ANTHROPIC_API_KEY and len(ANTHROPIC_API_KEY) > 10:
        try:
            client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
            
            prompt = f"""Você é um especialista em contabilidade brasileira. Analise este lançamento bancário e sugira:

Lançamento: {descricao}
Valor Crédito: {valor_credito}
Valor Débito: {valor_debito}

Baseado nisso, me diga:
1. Qual o melhor CENTRO DE CUSTO (formato: 9.99.999.9999)?
   - Receitas: 1.xx.xxx.xxxx
   - Despesas: 2.xx.xxx.xxxx
2. Uma OBSERVAÇÃO clara e profissional (máximo 50 caracteres)

Responda APENAS no formato JSON:
{{"centro_custo": "X.XX.XXX.XXXX", "observacao": "texto aqui"}}"""

            message = client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Parseia resposta da IA
            resposta = message.content[0].text.strip()
            if resposta.startswith('{') and resposta.endswith('}'):
                import json
                sugestao = json.loads(resposta)
                if 'centro_custo' in sugestao:
                    centro_custo = sugestao['centro_custo']
                if 'observacao' in sugestao:
                    observacao = sugestao['observacao'][:80]  # Limita tamanho
                    
        except Exception as e:
            print(f"Erro ao usar IA: {e}")
            # Continua com a classificação básica
            pass
    
    return {
        'tipo_movimento': tipo,
        'cnpj_cpf': cnpj_cpf,
        'centro_custo': centro_custo,
        'observacao': observacao
    }


def processar_valor(valor_str):
    """Converte valor do formato brasileiro (1.234,56) para float"""
    if pd.isna(valor_str) or valor_str == '':
        return 0.0
    
    valor_str = str(valor_str).strip()
    # Remove pontos e substitui vírgula por ponto
    valor_str = valor_str.replace('.', '').replace(',', '.')
    
    try:
        return float(valor_str)
    except:
        return 0.0


def processar_data(data_str):
    """Converte data para formato dd/mm/yyyy"""
    if pd.isna(data_str):
        return ''
    
    try:
        # Tenta converter para datetime
        if isinstance(data_str, str):
            data_obj = pd.to_datetime(data_str, format='%d/%m/%Y')
        else:
            data_obj = pd.to_datetime(data_str)
        
        return data_obj.strftime('%d/%m/%Y')
    except:
        return str(data_str)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/processar-extrato', methods=['POST'])
def processar_extrato():
    """
    Processa o arquivo de extrato e retorna os dados formatados
    """
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Nome de arquivo inválido'}), 400
        
        # Salva temporariamente
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        # Lê o extrato (pula as primeiras 7 linhas de cabeçalho do Bradesco)
        extrato_raw = pd.read_excel(filepath, skiprows=7)
        
        # Define nomes das colunas
        extrato_raw.columns = ['Data', 'Lançamento', 'Dcto', 'Crédito', 'Débito', 'Saldo']
        
        # Remove linha duplicada do cabeçalho
        extrato = extrato_raw[extrato_raw['Data'] != 'Data'].copy()
        
        # Remove o saldo anterior se existir
        extrato = extrato[extrato['Lançamento'] != 'SALDO ANTERIOR'].copy()
        
        # Reseta índice
        extrato.reset_index(drop=True, inplace=True)
        
        # Processa cada linha
        resultado = []
        
        for idx, row in extrato.iterrows():
            data = processar_data(row['Data'])
            lancamento = str(row['Lançamento']) if pd.notna(row['Lançamento']) else ''
            dcto = str(row['Dcto']) if pd.notna(row['Dcto']) else ''
            
            valor_credito = processar_valor(row['Crédito'])
            valor_debito = processar_valor(row['Débito'])
            
            # Determina o valor final (crédito ou débito)
            valor = valor_credito if valor_credito > 0 else valor_debito
            
            # Classifica com IA
            classificacao = classificar_com_ia(lancamento, valor_credito, valor_debito)
            
            # Monta o registro no formato do ERP
            registro = {
                'id': idx,
                'tipo_movimento': classificacao['tipo_movimento'],
                'num_doc': dcto,
                'cnpj_cpf': classificacao['cnpj_cpf'],
                'tipo_doc': '273',  # Padrão
                'data_emissao': data,
                'observacao': classificacao['observacao'],
                'conta_fin': classificacao['centro_custo'],
                'centro_custo': classificacao['centro_custo'],
                'valor': valor,
                'dt_venc': data,
                'valor_pago': valor,
                'data_baixa': data,
                'conta_bancaria': CONTA_BANCARIA,
                # Dados extras para visualização
                'lancamento_original': lancamento,
                'credito': valor_credito,
                'debito': valor_debito
            }
            
            resultado.append(registro)
        
        # Remove arquivo temporário
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'total': len(resultado),
            'dados': resultado,
            'estatisticas': {
                'total_creditos': sum(1 for r in resultado if r['tipo_movimento'] == 'R'),
                'total_debitos': sum(1 for r in resultado if r['tipo_movimento'] == 'P'),
                'soma_creditos': sum(r['credito'] for r in resultado),
                'soma_debitos': sum(r['debito'] for r in resultado)
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/exportar-erp', methods=['POST'])
def exportar_erp():
    """
    Exporta os dados no formato do modelo de importação do ERP
    """
    try:
        dados = request.json.get('dados', [])
        
        if not dados:
            return jsonify({'error': 'Nenhum dado para exportar'}), 400
        
        # Cria DataFrame no formato do ERP
        df_export = pd.DataFrame([{
            'Tipo Movimento': d['tipo_movimento'],
            'Num Doc': d['num_doc'],
            'CNPJ/CPF Fonte Devedora/Pagadora': d['cnpj_cpf'],
            'Tipo Doc': d['tipo_doc'],
            'Data de Emissão': d['data_emissao'],
            'Obsevacao': d['observacao'],
            'Conta Fin': d['conta_fin'],
            'Centro Custo': d['centro_custo'],
            'Valor': d['valor'],
            'Dt Venc': d['dt_venc'],
            'Valor Pago': d['valor_pago'],
            'Data Baixa': d['data_baixa'],
            'Conta Bancária': d['conta_bancaria']
        } for d in dados])
        
        # Gera arquivo Excel
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_export.to_excel(writer, index=False, sheet_name='Importação')
        
        output.seek(0)
        
        # Nome do arquivo com data
        filename = f'importacao_erp_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Verifica se a API está funcionando"""
    return jsonify({
        'status': 'ok',
        'ia_ativa': len(ANTHROPIC_API_KEY) > 10,
        'versao': '1.0.0'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
