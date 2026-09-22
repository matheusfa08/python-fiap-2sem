# =============================
# CÓDIGO DA LESSON2.PY COMPLETO
# =============================

import oracledb
USUARIO = "rm570933"
SENHA = "200308"
HOST = "oracle.fiap.com.br"
PORTA = 1521
SERVICE_NAME = "ORCL"
# Criando o DSN
dsn = oracledb.makedsn(
    HOST,
    PORTA,
    service_name=SERVICE_NAME
)
# CONECTANDO AO BANCO DE DADOS
try:

    conn = oracledb.connect(
        user=USUARIO,
        password=SENHA,
        dsn=dsn
    )
    print("========================================")
    print("   CONEXÃO REALIZADA COM SUCESSO!")
    print("========================================")

except oracledb.Error as erro:
    print("Erro ao conectar ao Oracle:")
    print(erro)
    exit()


# Criando cursor
cursor = conn.cursor()
print("Cursor criado com sucesso!")


# ============================================================
# INCLUSÃO DE PET
# ============================================================

def incluir_pet():
    print("\n========================================")
    print("           CADASTRO DE PET")
    print("========================================")
    id_pet = int(input ("Digite o ID do pet: "))
    tipo_pet = input("Digite o tipo do pet: ")
    nome_pet = input("Digite o nome do pet: ")
    idade = int(input("Digite a idade do pet: "))
    sql = """
        INSERT INTO petshop
        (
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        )
        VALUES
        (
            :id_pet,
            :tipo_pet,
            :nome_pet,
            :idade
        )
    """
    try:
        cursor.execute(
            sql,
            id_pet = id_pet,
            tipo_pet=tipo_pet,
            nome_pet=nome_pet,
            idade=idade
        )
        conn.commit()
        print("\nPet cadastrado com sucesso!")
    except oracledb.Error as erro:
        print("\nErro ao cadastrar o pet:")
        print(erro)
        conn.rollback()
# ============================================================
# CONSULTA DE TODOS OS PETS
# ============================================================
def consultar_pets():
    print("\n========================================")
    print("            CONSULTA DE PETS")
    print("========================================")
    sql = """
        SELECT
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        FROM petshop
        ORDER BY id_pet
    """
    try:
        cursor.execute(sql)
        pets = cursor.fetchall()
        if len(pets) == 0:
            print("\nNenhum pet cadastrado.")
        else:
            for pet in pets:
                print("\n----------------------------------------")
                print(f"ID:       {pet[0]}")
                print(f"Tipo:     {pet[1]}")
                print(f"Nome:     {pet[2]}")
                print(f"Idade:    {pet[3]}")
                print("----------------------------------------")
    except oracledb.Error as erro:
        print("\nErro ao consultar os pets:")
        print(erro)
def consultar_pet():
    print("\n========================================")
    print("         CONSULTAR PET POR ID")
    print("========================================")
    id_pet = int(input("Digite o ID do pet: "))
    sql = """
        SELECT
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        FROM petshop
        WHERE id_pet = :id_pet
    """
    try:
        cursor.execute(
            sql,
            id_pet=id_pet
        )
        pet = cursor.fetchone()
        if pet is None:
            print("\nPet não encontrado.")
        else:
            print("\nPet encontrado!")
            print("----------------------------------------")
            print(f"ID:       {pet[0]}")
            print(f"Tipo:     {pet[1]}")
            print(f"Nome:     {pet[2]}")
            print(f"Idade:    {pet[3]}")
            print("----------------------------------------")
    except oracledb.Error as erro:
        print("\nErro ao consultar o pet:")
        print(erro)

# ============================================================
# ALTERAÇÃO DE PET
# ============================================================

def alterar_pet():
    print("\n========================================")
    print("             ALTERAR PET")
    print("========================================")
    id_pet = int(
        input("Digite o ID do pet que deseja alterar: ")
    )
    sql_consulta = """
        SELECT
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        FROM petshop
        WHERE id_pet = :id_pet
    """
    try:
        cursor.execute(
            sql_consulta,
            id_pet=id_pet
        )
        pet = cursor.fetchone()
        if pet is None:
            print("\nPet não encontrado.")
            return
        print("\nDados atuais:")
        print("----------------------------------------")
        print(f"ID:       {pet[0]}")
        print(f"Tipo:     {pet[1]}")
        print(f"Nome:     {pet[2]}")
        print(f"Idade:    {pet[3]}")
        print("----------------------------------------")
        tipo_pet = input("Digite o novo tipo do pet: ")
        nome_pet = input("Digite o novo nome do pet: ")
        idade = int(input("Digite a nova idade do pet: "))
        sql = """
            UPDATE petshop
            SET
                tipo_pet = :tipo_pet,
                nome_pet = :nome_pet,
                idade = :idade
            WHERE id_pet = :id_pet
        """
        cursor.execute(
            sql,
            tipo_pet=tipo_pet,
            nome_pet=nome_pet,
            idade=idade,
            id_pet=id_pet
        )
        conn.commit()
        print("\nPet alterado com sucesso!")
    except oracledb.Error as erro:
        print("\nErro ao alterar o pet:")
        print(erro)
        conn.rollback() #como se fosse um 'esc' desfaz as alterações se ocorrer por 'acidente'
# ============================================================
# EXCLUSÃO DE PET
# ============================================================
def excluir_pet():
    print("\n========================================")
    print("             EXCLUIR PET")
    print("========================================")
    id_pet = int(
        input("Digite o ID do pet que deseja excluir: ")
    )
    sql_consulta = """
        SELECT
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        FROM petshop
        WHERE id_pet = :id_pet
    """
    try:
        cursor.execute(
            sql_consulta,
            id_pet=id_pet
        )
        pet = cursor.fetchone()
        if pet is None:
            print("\nPet não encontrado.")
            return
        print("\nPet encontrado:")
        print("----------------------------------------")
        print(f"ID:       {pet[0]}")
        print(f"Tipo:     {pet[1]}")
        print(f"Nome:     {pet[2]}")
        print(f"Idade:    {pet[3]}")
        print("----------------------------------------")
        confirmacao = input("Deseja realmente excluir este pet? (S/N): ")
        if confirmacao.upper() == "S":
            sql = """
                DELETE FROM petshop
                WHERE id_pet = :id_pet
            """
            cursor.execute(
                sql,
                id_pet=id_pet
            )
            conn.commit()
            print("\nPet excluído com sucesso!")
        else:
            print("\nExclusão cancelada.")
    except oracledb.Error as erro:
        print("\nErro ao excluir o pet:")
        print(erro)
        conn.rollback()
# ============================================================
# MENU PRINCIPAL
# ============================================================
while True:
    print("\n========================================")
    print("            SISTEMA PETSHOP")
    print("========================================")
    print("1 - Incluir Pet")
    print("2 - Consultar todos os Pets")
    print("3 - Consultar Pet por ID")
    print("4 - Alterar Pet")
    print("5 - Excluir Pet")
    print("0 - Sair")
    print("========================================")
    opcao = input("Digite uma opção: ")
    if opcao == "1":
        incluir_pet()
    elif opcao == "2":
        consultar_pets()
    elif opcao == "3":
        consultar_pet()
    elif opcao == "4":
        alterar_pet()
    elif opcao == "5":
        excluir_pet()
    elif opcao == "0":
        print("\nEncerrando o sistema...")
        break
    else:
        print("\nOpção inválida!")
    input("\nPressione ENTER para continuar...")
# ============================================================
# ENCERRANDO A CONEXÃO
# ============================================================
cursor.close()
conn.close()
print("\nConexão encerrada.")
print("Programa finalizado.")