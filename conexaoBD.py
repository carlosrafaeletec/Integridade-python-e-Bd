import pyodbc
import pandas as pd

def cadastrar_contato():
    lista = list()
    cursor = conexao.cursor()
    cursor.execute("SELECT id_contato FROM contato")
    data = cursor.fetchall()

    if data:
        for i in range(len(data)):
            ids = str(data[i][0]).replace('(', '').replace(')', '').replace(',', '')
            lista.append(int(ids))

    id_contato = int(input("ID: "))

    while id_contato in lista:
        id_contato = int(input(f"Valor do ID ja existente escolha um diferente de {lista}: "))

    nome = input("Nome: ")
    instagram = input("Instagram: ")
    email = input("Email: ")
    
    comando = f"INSERT INTO contato(id_contato, nome, instagram, email) VALUES ({id_contato}, '{nome}', '{instagram}', '{email}')"
    cursor.execute(comando)
    cursor.commit()
    
    print("\n registro gravado")

try:
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=localhost;"
        "Database=PythonSQL;"
        "User='sa';"
        "Password=123456;"
    )

    conexao = pyodbc.connect(dados_conexao)
    print("Conexão Bem Sucedida")

    cursor = conexao.cursor()
    cursor_cadastro = conexao.cursor()
    cursor_consulta = conexao.cursor()
    cursor_alteracao = conexao.cursor()
    cursor_exclusao = conexao.cursor()

except:
    print("Ocorreu algum erro no BD")
else:
    print("Conexão Bem Sucedida")
    
while True:
    print("""
      1 - Cadastrar Contato
      2 - Listar contatos
      3 - Consultar um registro
      4 - Editar um registro
      5 - Excluir um registro
      6 - Sair
    """)
    
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            cadastrar_contato()
        case 2:
            #consultar todos os registros
            lista_dados=list()

            cursor_consulta.execute("select * from contato")

            data = cursor_consulta.fetchall()

            if len(data) == 0:
                print("Não existem registros")
            else:

                for dt in data:
                    lista_dados.append(dt)

                lista_dados = sorted(lista_dados)
                print(lista_dados)
                dados_df = pd.DataFrame.from_records(
                    lista_dados, columns = ['id_contato', 'nome', 'instagram', 'email'], index = 'id_contato'
                )
                print(dados_df)

        case 3:
            #consultar parte dos registros
            lista_dados=list()
            id = int(input("Digite o ID: "))
            cursor_consulta.execute(f"select * from contato where id_contato = {id}")

            data = cursor_consulta.fetchall()

            if len(data) == 0:
                print("Não existe o registro")
            else:
                for dt in data:
                    lista_dados.append(dt)

                lista_dados = sorted(lista_dados)

                dados_df = pd.DataFrame.from_records(
                    lista_dados, columns = ['id_contato', 'nome', 'instagram', 'email'], index='id_contato'
                )
                print(dados_df)

        case 4:
            lista_dados=list()
            id_contato = int(input("Digite o ID do contato que deseja editar: "))
            nome = input("Novo nome: ")
            instagram = input("Novo Instagram: ")
            email = input("Novo Email: ")

            comando = f"UPDATE contato SET nome = '{nome}', instagram = '{instagram}', email = '{email}' WHERE id_contato = {id_contato}"

            cursor_alteracao.execute(comando)
            cursor_alteracao.commit()
            print("Registro atualizado com sucesso.")
        
        case 5:
            lista_dados=list()
            id_contato = int(input("Digite o ID do contato que deseja excluir: "))

            comando = f"DELETE contato WHERE id_contato = {id_contato}"

            cursor_alteracao.execute(comando)
            cursor_alteracao.commit()
            print("Registro excluido com sucesso.")
                    
        case 6:
            print('Saindo do programa...')
            break


''' Script SQLSERVER
create database PythonSQL
use PythonSQL;
create table contato(
	id_contato int primary key,
	nome varchar(30),
	instagram varchar(30),
	email varchar(30),
)
'''