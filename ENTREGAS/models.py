from datetime import datetime

class Entrega:
    def __init__(self, id = None, nome_cliente = None, logradouro= None, telefone= None, bairro= None):
        self.id = id
        self.nome_cliente = nome_cliente
        self.logradouro = logradouro
        self.telefone = telefone
        self.data = "NULL"
        self.hora = "NULL"
        self.status = "Aguardando"
        self.bairro = bairro
    
    def get_date():
        data_hora_atual = datetime.now()
        data = data_hora_atual.strftime("%d-%m-%Y")

        return data
    
    def get_time():
        data_hora_atual = datetime.now()
        hora = data_hora_atual.strftime("%H:%M:%S")

        return hora