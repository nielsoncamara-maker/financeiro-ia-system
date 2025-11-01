# ❓ Perguntas Frequentes (FAQ)

## 📋 Geral

### O que é este sistema?
É uma aplicação web que automatiza o processo de conversão de extratos bancários para o formato de importação do seu ERP, usando Inteligência Artificial para classificar automaticamente os lançamentos.

### Preciso pagar para usar?
**Não!** O sistema pode ser hospedado gratuitamente em plataformas como Render.com, Railway.app ou PythonAnywhere. A IA básica já vem embutida sem custo adicional.

### Funciona com qual banco?
Atualmente otimizado para **extratos do Bradesco** (.XLS). Mas pode ser adaptado para outros bancos com pequenos ajustes.

### É seguro?
**Sim!** Todo o processamento é feito no servidor. Os arquivos são processados e deletados imediatamente após. Não armazenamos nenhum dado financeiro.

---

## 🤖 Sobre a IA

### A IA é obrigatória?
**Não!** O sistema funciona em dois modos:
- **Sem API key**: Usa regras básicas (já é muito útil!)
- **Com API key**: Usa IA avançada Claude (classificação ainda melhor)

### Como a IA classifica os lançamentos?
A IA analisa:
1. Descrição do lançamento
2. Se é crédito ou débito
3. Palavras-chave relevantes
4. Padrões financeiros conhecidos

E sugere automaticamente:
- Tipo de movimento (R ou P)
- CNPJ/CPF (Cliente ou Fornecedor Avulso)
- Centro de custo apropriado
- Observação clara

### Quanto custa usar a IA?
- **Sem chave API**: Grátis (usa regras básicas)
- **Com chave API Claude**: ~$0.01 por 100 lançamentos
  - Exemplo: 500 lançamentos = $0.05 (centavos!)

### A IA pode errar?
**Sim, raramente.** Por isso o sistema permite:
- Revisar todos os dados antes de exportar
- Editar qualquer campo manualmente
- Sempre use o bom senso e revise!

---

## 💻 Técnico

### Quais navegadores suportados?
Todos os modernos:
- ✅ Chrome / Edge (Recomendado)
- ✅ Firefox
- ✅ Safari
- ⚠️ Internet Explorer (não recomendado)

### Funciona no celular?
**Sim!** A interface é responsiva e funciona em:
- 📱 Smartphones
- 📱 Tablets
- 💻 Desktops

### Qual o tamanho máximo do arquivo?
- **Local**: Sem limite (depende da memória)
- **Render/Railway**: ~50MB
- **PythonAnywhere**: ~100MB

Na prática, extratos até 1000 lançamentos (~5MB) funcionam perfeitamente.

### Posso processar múltiplos arquivos?
Um de cada vez. Após exportar, você pode fazer upload de outro.

### Quanto tempo demora o processamento?
- **50 lançamentos**: ~3 segundos
- **500 lançamentos**: ~10 segundos
- **1000 lançamentos**: ~20 segundos

Depende também da velocidade do servidor.

---

## 🔧 Configuração

### Como faço para subir o sistema?
Siga o guia detalhado em `DEPLOY_GUIDE.md`. As opções mais fáceis são:
1. **Render.com** (mais recomendado)
2. **Railway.app** (mais rápido)
3. **PythonAnywhere** (mais estável)

### Preciso saber programar?
**Não!** O sistema está pronto. Basta:
1. Criar conta na plataforma
2. Conectar com GitHub
3. Fazer deploy
4. Usar!

### Posso personalizar o sistema?
**Sim!** Todo o código é aberto e editável:
- Cores e interface: `templates/index.html`
- Lógica de classificação: `app.py`
- Centros de custo: `app.py` (função `classificar_com_ia`)

### Como adiciono novos centros de custo?
Edite o arquivo `app.py`, função `classificar_com_ia()`:

```python
if 'sua_palavra_chave' in descricao_lower:
    centro_custo = '2.XX.XXX.XXXX'
    observacao = 'Sua descrição'
```

---

## 📊 Uso do Sistema

### Como importo o extrato?
1. Acesse o sistema
2. Clique ou arraste o arquivo .XLS
3. Aguarde o processamento
4. Revise os dados
5. Clique em "Exportar para ERP"

### Posso editar os dados antes de exportar?
**Sim!** Campos em amarelo são editáveis:
- Clique no campo
- Digite o novo valor
- Pressione Enter

### O que significa cada tipo de movimento?
- **R** = Receber (entrada, crédito, cliente)
- **P** = Pagar (saída, débito, fornecedor)

### Por que todos vêm como "Cliente/Fornecedor Avulso"?
Por padrão, o sistema usa CNPJ/CPF avulso pois:
- Não temos cadastro de todos os clientes/fornecedores
- É mais seguro não assumir dados
- Você pode editar manualmente casos específicos
- No ERP, você pode fazer "de-para" depois

### Posso mudar o CNPJ/CPF padrão?
**Sim!** Edite em `app.py`:

```python
CLIENTE_AVULSO = {
    'cpf': '69216118334',  # Seu CPF
    'tipo': 'R'
}

FORNECEDOR_AVULSO = {
    'cnpj': '75882806000150',  # Seu CNPJ
    'tipo': 'P'
}
```

### Como adiciono minha conta bancária?
Edite em `app.py`:
```python
CONTA_BANCARIA = '237-2293-6721'  # Sua conta
```

---

## 🐛 Problemas e Soluções

### "Erro ao processar arquivo"
**Causas possíveis:**
1. Formato de arquivo errado
   - **Solução**: Use apenas .XLS ou .XLSX
2. Arquivo corrompido
   - **Solução**: Baixe novamente do banco
3. Formato diferente do Bradesco
   - **Solução**: Ajuste o código para seu banco

### Dados não aparecem corretos
**Verifique:**
1. Se o extrato tem o formato esperado
2. Se as datas estão no formato DD/MM/YYYY
3. Se valores estão com vírgula (R$ 1.234,56)

### Exportação não funciona
**Tente:**
1. Atualizar a página
2. Processar novamente
3. Verificar console do navegador (F12)
4. Verificar logs do servidor

### Sistema está lento
**Possíveis causas:**
1. Plano gratuito com recursos limitados
   - **Solução**: Upgrade ou troque de plataforma
2. Arquivo muito grande
   - **Solução**: Divida em arquivos menores
3. Muitos acessos simultâneos
   - **Solução**: Aguarde ou upgrade

### IA não está funcionando
**Verifique:**
1. Se `ANTHROPIC_API_KEY` está configurada
2. Se a chave é válida (começa com `sk-ant-`)
3. Se há créditos na conta Anthropic
4. Logs do servidor para erros

**Nota**: Sistema funciona sem IA usando regras básicas!

---

## 💼 Sobre o ERP

### Funciona com qual ERP?
O sistema gera um Excel no formato padrão que você enviou:
- Tipo Movimento
- Num Doc
- CNPJ/CPF Fonte
- Tipo Doc
- Data de Emissão
- Observação
- Conta Fin
- Centro Custo
- Valor
- Dt Venc
- Valor Pago
- Data Baixa
- Conta Bancária

Se seu ERP aceita importação via Excel nesse formato, vai funcionar!

### Como importo no ERP?
1. Exporte do sistema (arquivo .xlsx)
2. Abra seu ERP
3. Vá na função de importação
4. Selecione o arquivo gerado
5. Confirme a importação

Cada ERP tem seu processo específico. Consulte o manual do seu sistema.

### Posso importar múltiplas vezes?
**Cuidado!** Pode gerar duplicação. Recomenda-se:
1. Processar todos os extratos do período
2. Revisar e consolidar
3. Importar uma única vez

### Como evito duplicações?
Antes de importar, verifique:
- Datas já importadas
- Números de documentos duplicados
- Valores idênticos nas mesmas datas

Muitos ERPs têm validação automática de duplicatas.

---

## 🔐 Segurança e Privacidade

### Meus dados ficam salvos?
**Não!** O sistema:
1. Recebe o arquivo
2. Processa na memória
3. Retorna os resultados
4. **Deleta tudo**

Nada é armazenado permanentemente.

### A IA vê meus dados?
**Apenas se você configurar a API key.** E mesmo assim:
- Apenas a descrição do lançamento é enviada
- Sem valores, nomes completos ou CPF/CNPJ
- A Anthropic (empresa do Claude) não armazena dados

**Sem API key**: Zero dados enviados para fora.

### Posso usar em rede interna?
**Sim!** Você pode hospedar em seu próprio servidor:
1. Configure um servidor Python
2. Faça deploy local
3. Acesse apenas da sua rede

### Preciso de HTTPS?
**Recomendado** para produção. Todas as plataformas gratuitas já incluem SSL/HTTPS automaticamente.

---

## 🔄 Atualizações

### Como atualizo o sistema?
1. Faça as alterações no código
2. Commit no GitHub
3. A plataforma (Render/Railway) atualiza automaticamente

### Posso sugerir melhorias?
**Claro!** Abra uma "Issue" no GitHub ou contribua com código!

### Terá novas funcionalidades?
Possíveis futuras features:
- Suporte para mais bancos
- Machine Learning personalizado
- Relatórios e gráficos
- Integração direta com ERPs
- App mobile nativo

---

## 📞 Suporte

### Onde consigo ajuda?
1. **Documentação**: Leia todos os .md do projeto
2. **GitHub Issues**: Reporte problemas
3. **Logs**: Sempre verifique os logs do servidor

### Como reporto um bug?
1. Descreva o problema
2. Inclua mensagem de erro (se houver)
3. Informe: navegador, SO, tamanho do arquivo
4. Abra uma Issue no GitHub

### Posso contratar suporte?
Este é um projeto open-source. Para suporte profissional ou customizações, entre em contato com desenvolvedores especializados.

---

## 🎓 Aprendizado

### Quero entender o código
Ótimo! O sistema usa:
- **Backend**: Flask (Python) - API REST
- **Frontend**: HTML/CSS/JavaScript puro
- **Processamento**: Pandas (manipulação de Excel)
- **IA**: Anthropic Claude API

Arquivos principais:
- `app.py`: Toda a lógica do backend
- `templates/index.html`: Interface completa

### Posso usar como base para outro projeto?
**Sim!** A licença MIT permite uso comercial. Apenas mantenha os créditos.

### Como aprendo mais sobre Flask?
Recursos recomendados:
- Documentação oficial: https://flask.palletsprojects.com/
- Tutorial: https://www.youtube.com/results?search_query=flask+tutorial

### Como aprendo mais sobre IA?
Para usar a API Claude:
- Docs: https://docs.anthropic.com/
- Console: https://console.anthropic.com/

---

## ✅ Checklist de Sucesso

Antes de considerar que tudo está funcionando:

- [ ] Sistema está no ar e acessível
- [ ] Upload de arquivo funciona
- [ ] Processamento retorna dados
- [ ] Tabela exibe corretamente
- [ ] Campos são editáveis
- [ ] Exportação gera Excel
- [ ] Excel abre sem erros
- [ ] Formato está correto para ERP
- [ ] Importação no ERP funciona
- [ ] Dados conferem com extrato original

---

## 🎉 Dicas Finais

1. **Comece pequeno**: Teste com 10-20 lançamentos primeiro
2. **Revise sempre**: IA ajuda, mas você é o especialista
3. **Personalize**: Ajuste regras para seu negócio
4. **Automatize**: Use regularmente para economizar tempo
5. **Compartilhe**: Ensine sua equipe a usar

---

**Ainda tem dúvidas? Consulte os arquivos:**
- `README.md` - Visão geral
- `DEPLOY_GUIDE.md` - Como subir o sistema
- `DEMO.md` - Demonstração visual

**Sistema pronto para transformar seu dia a dia! 🚀**
