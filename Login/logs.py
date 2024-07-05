from datetime import datetime
from connection import *


def log_abertura():
    
    data_hora = datetime.now()
    data = data_hora.strftime('%d/%m/%Y')
    hora = data_hora.strftime('%H:%M:%S')
    info = 'Inicio do Programa'

    abertura_info = f"INSERT INTO logs(data,hora,info) VALUES('{data}','{hora}','{info}')"
    myqueries.execute(abertura_info)
    mydatabase.commit()

def log_inicio_sessão():
    
    data_hora = datetime.now()
    data = data_hora.strftime('%d/%m/%Y')
    hora = data_hora.strftime('%H:%M:%S')
    info = 'Inicio do Programa'

    abertura_info = f"INSERT INTO logs(data,hora,info) VALUES('{data}','{hora}','{info}')"
    myqueries.execute(abertura_info)
    mydatabase.commit()
    
