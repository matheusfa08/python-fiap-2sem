# Importação das bibliotecas necessárias para mexer no OracleDB e pega suas informaões 
import oracledb
import pandas as pd

# Credenciais do OracleDB
usuario = "rm570933"
senha = "200308"
host = "oracle.fiap.com.br"
porta = 1521
service_name = "ORCL"

# Criando o DSN (Data Source Name)
dsn = oracledb.makedsn(
    host=host,
    port= porta,
    service_name=service_name
)

# Se conectando ao Banco de Dados
try:
    conn = oracledb.connect(
        user = usuario,
        password = senha,
        dsn = dsn
    )

    print("==================================================")
    print("         Conexão Realizada com Sucesso!           ")
    print("==================================================")

# Caso ocorra algum erro com os dados de cadastro no Banco de Dados por parte do DEV
except oracledb.Error as erro:
    print("Erro ao conectar ao OracleDB:")
    print(erro)
    # Encerra o programa caso não consiga conectar
    exit()

# Criando Cursor
cursor = conn.cursor()
print("         Cursor Criado com Sucesso!           ")

# =========================================================================
# INSERT NO PYTHON - INSERT NO PYTHON - INSERT NO PYTHON - INSERT NO PYTHON
# =========================================================================

# Inclusão de um PET numa tabela chamada "petshop"
print("\n==================================================")
print("                 Cadastro de pet                  ")
print("==================================================")
# Entrada dos dados pelo usuário
tipo_pet = input("Digite o tipo do pet: ")
nome_pet = input("Digite o nome do pet: ")
idade_pet = int(input("Digite a idade do pet: "))
# Comando SQL
sql = """
    insert into petshp(
        tipo_pet,
        nome_pet,
        idade_pet
    )
    values
    (
        :tipo_pet,
        :nome_pet,
        :idade_pet
    )
"""
# Executando o "Insert"
cursor.execute( #Necessita do código SQL que foi feito e das variáveis que foram passadas nela
    sql,
    tipo_pet = tipo_pet,
    nome_pet = nome_pet,
    idade_pet = idade_pet
)
conn.commit() # Serve para executar o commit(Feature salva a execução e a cadastra, permitindo o ROLLBACK)
print("\nPet cadastrado com sucesso!")

# Encerrando conexões
cursor.close()
conn.close()
print("\nConexão encerrada")
print("Programa Finalizado")