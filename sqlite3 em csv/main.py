import sqlite3 as sql
import csv

conexao = sql.connect('matriculas.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS matricula (
               nome VARCHAR(100),
               email VARCHAR(100),
               CPF VARCHAR(20) PRIMARY KEY)''')

cursor.execute('SELECT * FROM matricula')
tabela_inteira = cursor.fetchall()
#print(tabela_inteira) --> [('saulo', 'saulo@email', '11987002466')...]
try:
    with open('arquivo.csv', 'x', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['nome', 'email', 'cpf'])
except FileExistsError:
    pass 

with open('arquivo.csv', 'a', newline = '', encoding = 'utf-8') as arquivo:
    writer = csv.writer(arquivo)
    for tupla_pessoa in tabela_inteira:
        writer.writerow(tupla_pessoa)


'''while True:
    nome = input('digite seu nome: ')
    email = input('digite seu email: ')
    cpf = input('digite seu cpf: ')

    cursor.execute('INSERT INTO matricula (nome, email, cpf) VALUES(?, ?, ?)', (nome, email, cpf))
    conexao.commit()
    print('Usuario cadastrado')'''
    

'''try:
    with open('arquivo.csv', 'x', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['mes', 'valor_total', 'valor_dividido', 'pessoas'])
except FileExistsError:
    pass 

with open('arquivo.csv', 'a', newline = '', encoding = 'utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow([mes, total, dividido, quantidade_pessoas])
'''