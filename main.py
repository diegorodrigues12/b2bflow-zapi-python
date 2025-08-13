from supabase import create_client
import requests
import os
from dotenv import load_dotenv

load_dotenv() 

# Pega as variáveis do ambiente
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

# Verifica se todas as variáveis foram definidas
if not all([SUPABASE_URL, SUPABASE_KEY, ZAPI_INSTANCE_ID, ZAPI_TOKEN]):
    print("Variáveis de ambiente faltando.")
    exit(1)

# Conecta ao Supabase
try:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    print(f"Erro ao conectar Supabase: {e}")
    exit(1)

# Função para buscar contatos na tabela 'contatos'
def buscar_contatos():
    try:
        response = supabase.table("contatos").select("*").execute()
        return response.data or []
    except Exception as e:
        print(f"Erro ao buscar contatos: {e}")
        return []

# Função para enviar mensagem via Z-API
def enviar_mensagem(numero, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/send-text"
    headers = {
        "Client-Token": ZAPI_TOKEN,  # Token para autenticação
        "Content-Type": "application/json"
    }
    payload = {
        "phone": numero,            # Número do destinatário
        "message": f"Olá {nome}, tudo bem com você?"
    }
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        if resp.status_code == 200:
            print(f"Mensagem enviada para {nome} ({numero})")
        else:
            print(f"Erro ao enviar para {nome}: {resp.status_code} - {resp.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição para {nome}: {e}")

# Fluxo principal
if __name__ == "__main__":
    print("Buscando contatos no Supabase...")
    contatos = buscar_contatos()

    if not contatos:
        print("Nenhum contato encontrado.")
    else:
        print(f"{len(contatos)} contato(s) encontrado(s). Enviando mensagens...")
        for contato in contatos[:3]: 
            numero = contato.get('numero')
            nome = contato.get('nome_contato')
            if not numero or not nome:
                print(f"Contato inválido: {contato}")
                continue
            enviar_mensagem(numero, nome)
