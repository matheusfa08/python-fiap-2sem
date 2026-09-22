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
print("Cursor Criado com Sucesso!")

# =========================================================================
# INSERT NO PYTHON - INSERT NO PYTHON - INSERT NO PYTHON - INSERT NO PYTHON
# =========================================================================

def incluir_pet():
    # Inclusão de um PET numa tabela chamada "petshop"
    print("\n==================================================")
    print("                 Cadastro de PET                  ")
    print("==================================================")
    # Entrada dos dados pelo usuário
    id_pet = input("Digite o ID do pet: ")
    tipo_pet = input("Digite o tipo do pet: ")
    nome_pet = input("Digite o nome do pet: ")
    idade_pet = int(input("Digite a idade do pet: "))
    try:
        # Comando SQL
        sql = """
            insert into petshop(
                id_pet,
                tipo_pet,
                nome_pet,
                idade_pet
            )
            values
            (
                :id_pet
                :tipo_pet,
                :nome_pet,
                :idade_pet
            )
        """
        # Executando o "Insert"
        cursor.execute( #Necessita do código SQL que foi feito e das variáveis que foram passadas nela
            sql,
            id_pet = id_pet,
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
    # Fazendo o tratamento de erro    
    except oracledb.Error as erro:
        print("Erro ao cadastrar o PET:")
        print(erro)

# =========================================================================
# SELECT NO PYTHON - SELECT NO PYTHON - SELECT NO PYTHON - SELECT NO PYTHON
# =========================================================================

def listar_pets():
    # Listagem de PETs numa tabela chamada "petshop"
    print("\n==================================================")
    print("                 Consulta de PETs                  ")
    print("==================================================")
    # Comando SQL
    sql = """
        select
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        from petshop
        order by id_pet
    """
    try:
        # Executando o "Select"
        cursor.execute(sql) # Dessa vez, só é necessário o comando, pois não temos nenhuma condição
        pets = cursor.fetchall() # Joga todos os dados do cursor na lista pets, que tem uma lista de infos
        if len(pets) == 0: # Caso a lista tenha 0 itens visiveis pelo index, ele dá uma mensagem erro
            print("\nNenhum pet cadastrado")
        else: # Caso a lista tenha algo
            for pet in pets: # Para cada lista dentro da lista, ele vai pegar o index de cada item nela
                print("\n-----------------------------")
                print(f"ID:     {pet[0]}")
                print(f"Tipo:   {pet[1]}")
                print(f"Nome:   {pet[2]}")
                print(f"Idade:  {pet[3]}")
                print("-----------------------------")
    # Tratativa de erro
    except oracledb.Error as erro:
        print("\nErro ao consultar os PETs:")
        print(erro)

def consultar_pet():
    # Consulta de PET numa tabela chamada "petshop", feita por ID
    print("\n==================================================")
    print("             Consulta de PET por ID               ")
    print("==================================================")
    id_pet = int(input("Digite o ID do PET: ")) # Input que será a variável no código SQL
    # Comando SQL
    sql = """
        select
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        from petshop
        where id_pet = :id_pet
    """
    try:
        # Executando o "Select"
        cursor.execute( # Necessário o código SQL e a variável que ele chama
            sql,
            id_pet = id_pet
        )
        pet = cursor.fetchall() # Coloca as informações dentro de uma lista chamada "pet"
        if pet is None: # Se não tiver nada na lista, retorna mensagem de erro
            print("\nPet não encontrado")
        else: #Se tiver, mostra as infos
            print("\nPet encontrado")
            print("\n-----------------------------")
            print(f"ID:     {pet[0]}")
            print(f"Tipo:   {pet[1]}")
            print(f"Nome:   {pet[2]}")
            print(f"Idade:  {pet[3]}")
            print("-----------------------------")
    # Tratativa de erro
    except oracledb.Error as erro:
        print("\nErro ao consultar os PETs:")
        print(erro)
        conn.rollback

# =========================================================================
# UPDATE NO PYTHON - UPDATE NO PYTHON - UPDATE NO PYTHON - UPDATE NO PYTHON
# =========================================================================

def alterar_pet():
    # Alteração de PETs numa tabela chamada "petshop"
    print("\n==================================================")
    print("                   Alterar PET                    ")
    print("==================================================")
    id_pet = input("Digite o ID do PET que deseja alterar")
    # Comando SQL
    sql = """
        select
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        from petshop
        where id_pet = :id_pet
    """
    try:
        # Executando o "Select"
        cursor.execute(sql) # Dessa vez, só é necessário o comando, pois não temos nenhuma condição
        pets = cursor.fetchone() # Joga todos os dados do cursor na lista pets, que tem uma lista de infos
        if len(pets) == 0: # Caso a lista tenha 0 itens visiveis pelo index, ele dá uma mensagem erro
            print("\nNenhum pet cadastrado")
        else: # Caso a lista tenha algo
            for pet in pets: # Para cada lista dentro da lista, ele vai pegar o index de cada item nela
                print("\n-----------------------------")
                print(f"ID:     {pet[0]}")
                print(f"Tipo:   {pet[1]}")
                print(f"Nome:   {pet[2]}")
                print(f"Idade:  {pet[3]}")
                print("-----------------------------")
    # Tratativa de erro
    except oracledb.Error as erro:
        print("\nErro ao alterar os PETs:")
        print(erro)

def menu():
    while True:
        print("===================")
        print("PetShop - DataBase")
        print("===================")
        print("1 - Inserir pet")
        print("2 - Alterar pet")
        print("3 - Buscar pet")
        print("4 - Listar pets")
        print("5 - Deletar pet")
        print("0 - Sair do Programa")
        print("===================")
        op = input("Digite uma opção:")

menu()