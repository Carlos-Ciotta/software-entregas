import requests
from models import Entrega

def get_all():
    url = 'https://api-production-72e9.up.railway.app/entrega/'
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # A resposta da API está no formato JSON
        data = response.json()
        tuplas = [tuple(d.values()) for d in data]
    else:
        print("Falha na solicitação. Código de status:", response.status_code)
        print("Conteúdo da resposta:", response.text)
    return tuplas

def get_by_id(id:int):
    url = f'http://api-production-72e9.up.railway.app/entrega/{id}'
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # A resposta da API está no formato JSON
        data = response.json()
        print("Dados da API:", data)
    else:
        print("Falha na solicitação. Código de status:", response.status_code)
        print("Conteúdo da resposta:", response.text)
    return data

def post(entrega_i:Entrega):
    url = 'https://api-production-72e9.up.railway.app/entrega/post'
    dados = entrega_i.__dict__

    response = requests.post(url, json=dados)

    if response.status_code == 200:
        data = response.json()
        print("Dados da API:", data)
    else:
        print("Falha na solicitação. Código de status:", response.status_code)
        print("Conteúdo da resposta:", response.text)

def put_status(id:int, status:str):
    url = f'http://api-production-72e9.up.railway.app/entregas/put/{id}'
    dados = {'status': status}

    response = requests.put(url, data=dados)

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # A resposta da API está no formato JSON
        data = response.json()
        print("Dados da API:", data)
    else:
        print("Falha na solicitação. Código de status:", response.status_code)
        print("Conteúdo da resposta:", response.text)

def put_dados(id:int, entrega_i:Entrega):
    url = f'http://api-production-72e9.up.railway.app/entregas/put/{id}'
    dados = {'nome_cliente' : entrega_i.nome_cliente,
             'logradouro':entrega_i.logradouro,
             'bairro':entrega_i.bairro,
             'telefone': entrega_i.telefone}

    response = requests.put(url, json = dados)

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # A resposta da API está no formato JSON
        data = response.json()
        print("Dados da API:", data)
    else:
        print("Falha na solicitação. Código de status:", response.status_code)
        print("Conteúdo da resposta:", response.text)

def delete_by_id(id:int):
    url = f'http://api-production-72e9.up.railway.app/entregas/delete/{id}'

    response = requests.delete(url)

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # A resposta da API está no formato JSON
        data = response.json()
        print("Dados da API:", data)
    else:
        print("Falha na solicitação. Código de status:", response.status_code)
        print("Conteúdo da resposta:", response.text)
