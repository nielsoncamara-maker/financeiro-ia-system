# 🤖 Sistema de Automação Financeira com IA

Sistema web completo para processar extratos bancários e gerar arquivos prontos para importação no ERP, usando Inteligência Artificial para classificação automática.

## 🎯 Funcionalidades

✅ Upload de extrato bancário (.XLS / .XLSX)  
✅ Processamento automático com IA  
✅ Classificação inteligente de Clientes vs Fornecedores  
✅ Sugestão automática de Centro de Custo  
✅ Tabela editável para ajustes manuais  
✅ Exportação no formato do modelo ERP  
✅ Interface moderna e responsiva  

## 🚀 Como Hospedar GRATUITAMENTE

### **Opção 1: Render.com (RECOMENDADO)** ⭐

Melhor opção: deploy automático e gratuito!

1. **Acesse**: [https://render.com](https://render.com)
2. **Crie uma conta** (pode usar GitHub)
3. **Clique em "New +"** → **"Web Service"**
4. **Conecte seu repositório GitHub** com este código
5. **Configure**:
   - **Name**: `financeiro-ia-system`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Escolha **Free**
6. **Adicione variável de ambiente** (opcional):
   - Key: `ANTHROPIC_API_KEY`
   - Value: sua chave da API Claude (para IA avançada)
7. **Deploy!**

✅ Pronto! Seu sistema estará no ar em minutos!

### **Opção 2: Railway.app** 🚂

Outra excelente opção gratuita:

1. **Acesse**: [https://railway.app](https://railway.app)
2. **Conecte com GitHub**
3. **"New Project"** → **"Deploy from GitHub repo"**
4. **Selecione o repositório**
5. **Railway detecta automaticamente** e faz deploy!
6. **Adicione variável de ambiente** (Settings):
   - `ANTHROPIC_API_KEY=sua_chave`

### **Opção 3: PythonAnywhere** 🐍

Para deploy mais manual:

1. **Acesse**: [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. **Crie conta gratuita**
3. **Upload dos arquivos** via dashboard
4. **Configure Web App** → **Flask**
5. **Instale dependências** no console:
   ```bash
   pip install --user -r requirements.txt
   ```
6. **Configure WSGI** apontando para `app.py`

### **Opção 4: Vercel (Frontend) + Render (Backend)** ⚡

Para performance máxima:

**Backend no Render** (instruções acima)

**Frontend no Vercel**:
1. Separe o HTML em pasta `public/`
2. Deploy no Vercel: [https://vercel.com](https://vercel.com)
3. Configure variável de ambiente apontando para URL do backend

## 💻 Rodando Localmente

### Pré-requisitos

- Python 3.8+
- pip

### Instalação

```bash
# Clone o repositório
git clone [seu-repositorio]
cd financeiro-ia-system

# Instale as dependências
pip install -r requirements.txt

# (Opcional) Configure a chave da API
cp .env.example .env
# Edite .env e adicione sua ANTHROPIC_API_KEY

# Execute o servidor
python app.py
```

Acesse: http://localhost:5000

## 🔑 Configuração da IA (Opcional)

O sistema funciona **sem precisar de API key**, usando regras básicas.

Para IA avançada (classificação mais precisa):

1. **Obtenha uma chave**: [https://console.anthropic.com/](https://console.anthropic.com/)
2. **Adicione no ambiente**:
   - Localmente: arquivo `.env`
   - Render/Railway: nas variáveis de ambiente
3. **A IA vai melhorar automaticamente** a classificação!

## 📋 Como Usar

1. **Acesse o sistema** no navegador
2. **Faça upload** do extrato bancário (.XLS do Bradesco)
3. **Aguarde o processamento** (IA trabalhando! 🤖)
4. **Revise os dados** na tabela (pode editar clicando nos campos amarelos)
5. **Clique em "Exportar para ERP"**
6. **Importe o arquivo** no seu sistema ERP!

## 🏗️ Estrutura do Projeto

```
financeiro-ia-system/
│
├── app.py                  # Backend Flask (API)
├── templates/
│   └── index.html         # Interface web
├── requirements.txt       # Dependências Python
├── .env.example          # Exemplo de configuração
├── README.md             # Este arquivo
│
├── uploads/              # (criado automaticamente)
└── outputs/              # (criado automaticamente)
```

## 🔧 Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **IA**: Claude API (Anthropic)
- **Processamento**: Pandas, OpenPyXL
- **Deploy**: Gunicorn (produção)

## 📊 Formato de Dados

### Entrada (Extrato Bradesco)
- Data
- Lançamento
- Documento
- Crédito/Débito
- Saldo

### Saída (Modelo ERP)
- Tipo Movimento (R/P)
- CNPJ/CPF (Cliente/Fornecedor Avulso)
- Centro de Custo
- Valores e Datas
- Observações

## 🤝 Suporte

Dúvidas? Entre em contato!

## 📝 Licença

MIT License - Livre para uso comercial e pessoal

---

**Desenvolvido com ❤️ e 🤖 IA**
