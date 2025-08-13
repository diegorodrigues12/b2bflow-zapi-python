# Projeto B2BFlow - Envio de Mensagens via Z-API e Supabase

Este projeto em Python lê contatos cadastrados no Supabase e envia uma mensagem personalizada para cada um via Z-API.

## Como configurar

### 1. Supabase
- Crie uma conta gratuita no [Supabase](https://supabase.com/).
- Crie um projeto e uma tabela chamada `contatos`.
- A tabela deve conter os campos:
  - `id`: chave primária (integer, auto-incremento ou UUID)
  - `numero`: string com o telefone no formato DDI + DDD + número, ex: `5511999999999`
  - `nome_contato`: string com o nome da pessoa

### 2. Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

SUPABASE_URL=https://nbuaopgobhaofbgepnie.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5idWFvcGdvYmhhb2ZiZ2VwbmllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUwNTU1MzIsImV4cCI6MjA3MDYzMTUzMn0.SJFqNkzPWCG-CdXh630Gd4atb2DuV5TlXAOxwZ79xvA
ZAPI_INSTANCE_ID=3E5A2DB41390F09CC0055AA063CFBDB5
ZAPI_TOKEN=EB09B01BDC38323D70D8E8E4


### 3. Executar o projeto

No terminal, instale as dependências (recomendo usar um ambiente virtual):

pip install -r requirements.txt

Depois, execute:
```bash
python main.py
