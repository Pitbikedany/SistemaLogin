###################
# Daniel Lourenço #
#  Julho de 2024  #
###################

import hashlib
import pwinput
from connection import *
import os
from datetime import datetime
#funcao log de abertura
def log_abertura():
    
    #metodo para extrair data e hora do sistema
    data_hora = datetime.now()
    #formatacao da data
    data = data_hora.strftime('%d/%m/%Y')
    #formatacao da hora
    hora = data_hora.strftime('%H:%M:%S')
    #acao feita pelo user
    info = 'Inicio do Programa'

    #adicionar log na base de dados
    abertura_info = f"INSERT INTO logs(data,hora,info) VALUES('{data}','{hora}','{info}')"
    myqueries.execute(abertura_info)
    mydatabase.commit()

#log para inicio de sessao
def log_inicio_sessao():
    #metodo para extrair data e hora do sistema
    data_hora = datetime.now()
    #formatacao da data
    data = data_hora.strftime('%d/%m/%Y')
    #formatacao da hora
    hora = data_hora.strftime('%H:%M:%S')
    #acao feita pelo user
    info = f"Tentativa de Inicio de Sessão com Email: {email_user}, Password: {pw_user}"
   # print("|"+info+"|")

    #adicionar log na base de dados
    abertura_info = f"INSERT INTO logs(data,hora,info) VALUES('{data}','{hora}','{info}')"
    myqueries.execute(abertura_info)
    mydatabase.commit()

#log erro de inicio de sessao
def log_erro_inicio_sessao():
    
    #metodo para extrair data e hora da base de dados
    data_hora = datetime.now()
    #formatacao da data
    data = data_hora.strftime('%d/%m/%Y')
    #formatacao da hora
    hora = data_hora.strftime('%H:%M:%S')
    #acao feita pelo user
    info = f"Tentativa de Inicio de Sessão Falhada com Email: {email_user}, Password: {pw_user}"

    #adicionar log na base de dados
    abertura_info = f"INSERT INTO logs(data,hora,info) VALUES('{data}','{hora}','{info}')"
    myqueries.execute(abertura_info)
    mydatabase.commit()

#log de sucesso no inicio de sessao
def log_sucesso_inicio_sessao():
    
    #metodo para extrair data e hora
    data_hora = datetime.now()
    #formatacao da data
    data = data_hora.strftime('%d/%m/%Y')
    #formatacao da hora
    hora = data_hora.strftime('%H:%M:%S')
    #acao feita pelo user
    info = f"Tentativa de Inicio de Sessão realizada com Sucesso com Email: {email_user}, Password: {pw_user}"

    #adicionar log na base de dados
    abertura_info = f"INSERT INTO logs(data,hora,info) VALUES('{data}','{hora}','{info}')"
    myqueries.execute(abertura_info)
    mydatabase.commit()

#funcao quando esgotam as tentativas de login
def log_tentativas_inicio_sessao():

    #metodo para extrair data e hora do sistema
    data_hora = datetime.now()
    #formatacao da data
    data = data_hora.strftime('%d/%m/%Y')
    #formatacao da hora
    hora = data_hora.strftime('%H:%M:%S')
    #acao feita pelo user
    info = f"Tentativas de Inicio de Sessão Esgotadas com Email: {email_user}, Password: {pw_user}"

    #adicionar log na base de dados
    abertura_info = f"INSERT INTO logs(data,hora,info) VALUES('{data}','{hora}','{info}')"
    myqueries.execute(abertura_info)
    mydatabase.commit()

#log encerrar programa
def log_encerrar():
    
    #metodo para extrair data e hora do sistema
    data_hora = datetime.now()
    #formatacao da data
    data = data_hora.strftime('%d/%m/%Y')
    #formatacao da hora
    hora = data_hora.strftime('%H:%M:%S')
    #acao feita pelo user
    info = f"Programa Encerrado"   

    #adicionar log na base de dados
    abertura_info = f"INSERT INTO logs(data,hora,info) VALUES('{data}','{hora}','{info}')"
    myqueries.execute(abertura_info)
    mydatabase.commit()


#log para inicio do programa
log_abertura()
#while para contar as tentativas de inicio de sessão
tentativas = 3
while tentativas > 0:
    #variaveis para obter informacao para o login
    email_user = input('Email: ')
    pw_user = pwinput.pwinput(prompt='Password: ')
    #Log user tentou iniciar sessao
    log_inicio_sessao()
    #encriptação de password
    pw_encriptada = hashlib.sha1(pw_user.encode())
    pass_encript = pw_encriptada.hexdigest()

    #array para guardar informacoes da base de dados
    email = []
    password = []

    #query para saber todos os emails contidos na database
    email_check = f"SELECT email FROM users"
    myqueries.execute(email_check)
    values = myqueries.fetchall()

    #append dos emails da database num array
    for value in values:
        email.append(str(value[0]))

    #query para saber todas as passwords contidas na database
    pw_check = f"SELECT password FROM users"
    myqueries.execute(pw_check)
    values_pw = myqueries.fetchall()

    #append das passwords da database num array 
    for value_pw in values_pw:
        password.append(str(value_pw[0]))

    #contador para o email e password coicidirem na mesma posicao do array
    i = 0

        #while que vai percorrer o array do email para saber se os dados introduzidos correspondem
    while (i<=len(email)-1):
            
            # if para dar check ao email e password inseridos pelo user
            if email_user == email[i] and  pass_encript == password[i]:
                print('Login Efetuado com Sucesso')
                log_sucesso_inicio_sessao()
                tentativas = 0
            else: 
                tentativas -= 1
                if tentativas <=0:
                    print(f'Credenciais Erradas, não tem mais tentativas, tente novamente mais tarde')
                    pausa = input('Pressione ENTER para fechar o programa')
                    log_tentativas_inicio_sessao()
                    os.system('cls')
                else:
                    print(f'Credenciais Erradas, tem mais {tentativas} tentativas')
                    log_erro_inicio_sessao()
                    pausa = input('Pressione ENTER para tentar novamente')
                    os.system('cls')
            i+=1
log_encerrar()
