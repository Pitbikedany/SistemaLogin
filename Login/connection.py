import mysql.connector
#conexao com a database
mydatabase = mysql.connector.connect(host="localhost", user="root", database="login_system")
myqueries = mydatabase.cursor()