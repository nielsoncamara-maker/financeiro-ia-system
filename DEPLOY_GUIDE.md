# 🚀 GUIA COMPLETO DE DEPLOY - Passo a Passo

## 📋 Índice
1. [Preparação](#preparação)
2. [Deploy no Render.com (RECOMENDADO)](#deploy-no-rendercom)
3. [Deploy no Railway.app](#deploy-no-railwayapp)
4. [Deploy no PythonAnywhere](#deploy-no-pythonanywhere)
5. [Configuração da IA (Opcional)](#configuração-da-ia)
6. [Resolução de Problemas](#resolução-de-problemas)

---

## 📦 Preparação

### 1. Criar Conta no GitHub (se não tiver)

1. Acesse: https://github.com
2. Clique em "Sign up"
3. Siga as instruções

### 2. Criar Repositório

1. No GitHub, clique em **"New repository"**
2. Nome: `financeiro-ia-system`
3. Descrição: `Sistema de Automação Financeira com IA`
4. Público ou Privado (sua escolha)
5. **NÃO** inicialize com README
6. Clique em **"Create repository"**

### 3. Fazer Upload do Código

**Opção A: Via Interface Web (Fácil)**
1. Clique em **"uploading an existing file"**
2. Arraste TODOS os arquivos do sistema
3. Commit: "Initial commit"
4. Clique em **"Commit changes"**

**Opção B: Via Git (Avançado)**
```bash
cd financeiro-ia-system
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/seu-usuario/financeiro-ia-system.git
git push -u origin main
```

---

## 🎯 Deploy no Render.com (RECOMENDADO)

### ⭐ Por que Render?
- ✅ 100% Gratuito
- ✅ Deploy automático
- ✅ SSL/HTTPS incluído
- ✅ Fácil de configurar
- ✅ 750 horas/mês grátis

### 📝 Passo a Passo

#### 1. Criar Conta
1. Acesse: https://render.com
2. Clique em **"Get Started"**
3. Escolha **"Sign Up with GitHub"**
4. Autorize o Render a acessar seus repositórios

#### 2. Criar Web Service
1. No Dashboard, clique em **"New +"**
2. Selecione **"Web Service"**

#### 3. Conectar Repositório
1. Procure por `financeiro-ia-system`
2. Clique em **"Connect"**

#### 4. Configurar o Service

**Settings (Configurações):**
```
Name: financeiro-ia-system
Region: Oregon (US West) ou qualquer outra
Branch: main
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
```

**Instance Type:**
- Selecione: **Free**

#### 5. Adicionar Variável de Ambiente (Opcional)

Para usar IA avançada:

1. Na seção **"Environment"**
2. Clique em **"Add Environment Variable"**
3. Key: `ANTHROPIC_API_KEY`
4. Value: `sua_chave_aqui` (obtenha em https://console.anthropic.com/)

#### 6. Deploy!

1. Clique em **"Create Web Service"**
2. Aguarde 3-5 minutos (primeira vez demora mais)
3. Quando ver **"Live"** → está no ar! 🎉

#### 7. Acessar seu Sistema

Seu sistema estará em:
```
https://financeiro-ia-system.onrender.com
```

#### 8. Configurar URL Personalizada (Opcional)

1. Vá em **"Settings"** → **"Custom Domains"**
2. Adicione seu domínio próprio (se tiver)

---

## 🚂 Deploy no Railway.app

### ⭐ Por que Railway?
- ✅ Extremamente fácil
- ✅ $5 de crédito grátis/mês
- ✅ Deploy em segundos
- ✅ Interface moderna

### 📝 Passo a Passo

#### 1. Criar Conta
1. Acesse: https://railway.app
2. Clique em **"Login"**
3. Escolha **"Login with GitHub"**

#### 2. Criar Novo Projeto
1. Clique em **"New Project"**
2. Selecione **"Deploy from GitHub repo"**

#### 3. Conectar Repositório
1. Procure: `financeiro-ia-system`
2. Clique no repositório

#### 4. Deploy Automático!
Railway detecta automaticamente Python e faz o deploy! 🚀

#### 5. Adicionar Variável de Ambiente (Opcional)
1. Clique no seu service
2. Vá em **"Variables"**
3. Adicione:
   - `ANTHROPIC_API_KEY=sua_chave`

#### 6. Gerar URL Pública
1. Clique em **"Settings"**
2. Ative **"Generate Domain"**
3. Copie a URL: `seu-projeto.up.railway.app`

---

## 🐍 Deploy no PythonAnywhere

### ⭐ Por que PythonAnywhere?
- ✅ Especializado em Python
- ✅ Plano gratuito vitalício
- ✅ Console SSH incluso
- ✅ Sem cartão de crédito

### 📝 Passo a Passo

#### 1. Criar Conta
1. Acesse: https://www.pythonanywhere.com
2. Clique em **"Pricing & signup"**
3. Escolha **"Create a Beginner account"** (Grátis)

#### 2. Fazer Upload do Código

**Opção A: Via Git (Recomendado)**
1. Abra o **"Bash Console"**
2. Execute:
```bash
git clone https://github.com/seu-usuario/financeiro-ia-system.git
cd financeiro-ia-system
```

**Opção B: Upload Manual**
1. Vá em **"Files"**
2. Crie pasta `financeiro-ia-system`
3. Faça upload de todos os arquivos

#### 3. Instalar Dependências
No Bash Console:
```bash
cd financeiro-ia-system
pip3.10 install --user -r requirements.txt
```

#### 4. Criar Web App
1. Vá em **"Web"**
2. Clique **"Add a new web app"**
3. Escolha **"Manual configuration"**
4. Python version: **3.10**

#### 5. Configurar WSGI
1. Clique no link **"WSGI configuration file"**
2. Delete tudo e cole:
```python
import sys
import os

# Adiciona o diretório do projeto
project_home = '/home/seu_usuario/financeiro-ia-system'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Carrega a aplicação Flask
from app import app as application
```
3. Salve

#### 6. Configurar Virtualenv (Opcional)
1. Na aba **"Web"**
2. Em **"Virtualenv"**, adicione:
   `/home/seu_usuario/.local`

#### 7. Reload & Go!
1. Clique em **"Reload"**
2. Acesse: `seu-usuario.pythonanywhere.com`

---

## 🤖 Configuração da IA (Opcional)

### Por que configurar?
- ✅ Classificação mais precisa
- ✅ Sugestões inteligentes de centro de custo
- ✅ Melhor interpretação de lançamentos

### Como obter chave da API

1. **Acesse**: https://console.anthropic.com/
2. **Crie uma conta** (pode usar Google)
3. **Vá em "API Keys"**
4. **Clique em "Create Key"**
5. **Copie a chave** (começa com `sk-ant-...`)

### Como adicionar no sistema

**Render.com:**
- Settings → Environment → Add Environment Variable
- Key: `ANTHROPIC_API_KEY`
- Value: sua chave

**Railway.app:**
- Seu serviço → Variables → New Variable
- `ANTHROPIC_API_KEY=sua_chave`

**PythonAnywhere:**
- Web → Environment variables
- `ANTHROPIC_API_KEY=sua_chave`

### Custos da API Claude

- **Gratuito**: Você pode usar sem chave (IA básica)
- **Com chave**: Paga-se por uso
  - Claude Sonnet: ~$3 por 1 milhão de tokens
  - Para extratos: ~$0.01 por 100 lançamentos
  - **Muito barato!**

---

## 🔧 Resolução de Problemas

### ❌ "Application Error" ou "Build Failed"

**Causa**: Falta de dependências

**Solução**:
1. Verifique se `requirements.txt` existe
2. Confirme que o Build Command está correto:
   ```
   pip install -r requirements.txt
   ```

### ❌ "Module not found"

**Causa**: Biblioteca não instalada

**Solução**:
- Adicione a biblioteca no `requirements.txt`
- Faça novo deploy

### ❌ "Port already in use"

**Causa**: Porta fixa no código

**Solução**:
- Certifique-se que `app.py` usa `$PORT`:
  ```python
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
  ```

### ❌ Sistema muito lento

**Causa**: Plano gratuito com recursos limitados

**Soluções**:
- Use Render.com (melhor performance grátis)
- Ou upgrade para plano pago (~$7/mês)

### ❌ "IA não está funcionando"

**Verificar**:
1. Se `ANTHROPIC_API_KEY` está configurada
2. Se a chave é válida
3. Se há créditos na conta Anthropic

**Nota**: Sistema funciona sem IA, mas com regras básicas.

### 🆘 Precisa de Ajuda?

1. **Verifique os logs** na plataforma de deploy
2. **Teste localmente** primeiro: `python app.py`
3. **Revise este guia** passo a passo

---

## ✅ Checklist Final

Antes de considerar concluído:

- [ ] Sistema está acessível na URL
- [ ] Upload de arquivo funciona
- [ ] Processamento gera resultados
- [ ] Tabela é exibida corretamente
- [ ] Exportação gera arquivo Excel
- [ ] Arquivo exportado abre no Excel
- [ ] Formato está correto para ERP

---

## 🎉 Parabéns!

Seu sistema está no ar e funcionando! 🚀

**Próximos passos:**
1. Compartilhe a URL com sua equipe
2. Teste com extratos reais
3. Ajuste regras de classificação conforme necessário
4. Aproveite a economia de tempo! ⏰

---

**Desenvolvido com ❤️ e 🤖**
