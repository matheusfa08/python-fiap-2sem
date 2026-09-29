# =============================================================
# Importando as bibliotecas que são necessárias para o programa
# =============================================================

from flask import Flask, request, redirect, url_for, render_template_string
from html import escape
import oracledb
import datetime

# ==========================================
# Colocando os dados para acessar o DataBase
# ==========================================

USUARIO = "rm570933" 
SENHA = "200308" 
HOST = "oracle.fiap.com.br" 
PORTA = 1521 
SERVICE_NAME = "ORCL" 
 
dsn = oracledb.makedsn( 
    HOST, 
    PORTA, 
    service_name=SERVICE_NAME 
)

SQL_SELECT = """
    SELECT
        ID_PET, NOME_PET, TIPO_PET, RACA, IDADE,
        PESO, NOME_TUTOR, TELEFONE, DATA_CADASTRO
    FROM VIDAPET
"""
 
 
# ============================================================
# CONEXÃO
# ============================================================
 
def conectar_banco():
    try:
        conn = oracledb.connect(
            user=USUARIO,
            password=SENHA,
            dsn=dsn
        )
        return conn
 
    except oracledb.Error as erro:
        print("Erro ao conectar ao Oracle:", erro)
        return None
 
 
# ============================================================
# FUNÇÕES AUXILIARES DE ENTRADA
# ============================================================
 
def ler_texto(mensagem, obrigatorio=True, tamanho_max=None):
    while True:
        valor = input(mensagem).strip()
 
        if valor == "":
            if obrigatorio:
                print("Campo obrigatório.")
                continue
            return None
 
        if tamanho_max is not None and len(valor) > tamanho_max:
            print("Máximo de", tamanho_max, "caracteres.")
            continue
 
        return valor
 
 
def ler_inteiro(mensagem, minimo=0):
    while True:
        valor = input(mensagem).strip()
 
        try:
            numero = int(valor)
        except ValueError:
            print("Digite um número inteiro válido.")
            continue
 
        if numero < minimo:
            print("O valor deve ser maior ou igual a", minimo, ".")
            continue
 
        return numero
 
 
def ler_peso(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
 
        if valor == "":
            return None
 
        try:
            peso = float(valor)
        except ValueError:
            print("Digite um peso válido.")
            continue
 
        if peso <= 0:
            print("O peso deve ser maior que zero.")
            continue
 
        if peso > 9999.99:
            print("O peso máximo é 9999.99.")
            continue
 
        return peso
 
 
def formatar_data(data):
    if data is None:
        return ""
    return data.strftime("%d/%m/%Y %H:%M")
 
 
def formatar_peso(peso):
    if peso is None:
        return "-"
    return f"{peso:.2f}"
 
 
# ============================================================
# FUNÇÕES AUXILIARES DE BANCO
# ============================================================
 
def buscar_pets(id_pet=None):
    """Retorna (lista_de_pets, sucesso). Se id_pet for informado, filtra por ele."""
    conn = conectar_banco()
 
    if conn is None:
        return [], False
 
    cursor = conn.cursor()
 
    try:
        if id_pet is None:
            cursor.execute(SQL_SELECT + " ORDER BY ID_PET")
        else:
            cursor.execute(
                SQL_SELECT + " WHERE ID_PET = :id_pet",
                id_pet=id_pet
            )
 
        return cursor.fetchall(), True
 
    except oracledb.Error as erro:
        print("Erro ao consultar:", erro)
        return [], False
 
    finally:
        cursor.close()
        conn.close()
 
 
def gerar_proximo_id():
    """Retorna o próximo ID (maior ID atual + 1) ou None em caso de erro."""
    conn = conectar_banco()
 
    if conn is None:
        return None
 
    cursor = conn.cursor()
 
    try:
        cursor.execute("SELECT NVL(MAX(ID_PET), 0) + 1 FROM VIDAPET")
        return int(cursor.fetchone()[0])
 
    except oracledb.Error as erro:
        print("Erro ao gerar o ID:", erro)
        return None
 
    finally:
        cursor.close()
        conn.close()
 
 
def executar_alteracao(sql, parametros):
    """Executa INSERT/UPDATE/DELETE com commit ou rollback. Retorna (sucesso, erro)."""
    conn = conectar_banco()
 
    if conn is None:
        return False, "Sem conexão com o Oracle."
 
    cursor = conn.cursor()
 
    try:
        cursor.execute(sql, parametros)
        conn.commit()
        return True, None
 
    except oracledb.Error as erro:
        conn.rollback()
        return False, erro
 
    finally:
        cursor.close()
        conn.close()
 
 
def exibir_pet(pet):
    print("-" * 50)
    print("ID:            ", pet[0])
    print("Nome:          ", pet[1])
    print("Tipo:          ", pet[2])
    print("Raça:          ", pet[3] or "-")
    print("Idade:         ", pet[4])
    print("Peso:          ", formatar_peso(pet[5]))
    print("Tutor:         ", pet[6])
    print("Telefone:      ", pet[7] or "-")
    print("Data cadastro: ", formatar_data(pet[8]))
    print("-" * 50)
 
 
# ============================================================
# CREATE
# ============================================================
 
def cadastrar_pet():
    print("\n--- CADASTRAR PET ---")
 
    nome_pet = ler_texto("Nome do pet: ", tamanho_max=100)
    tipo_pet = ler_texto("Tipo (cão, gato...): ", tamanho_max=30)
    raca = ler_texto("Raça (opcional): ", obrigatorio=False, tamanho_max=60)
    idade = ler_inteiro("Idade: ", minimo=0)
    peso = ler_peso("Peso (opcional): ")
    nome_tutor = ler_texto("Nome do tutor: ", tamanho_max=100)
    telefone = ler_texto("Telefone (opcional): ", obrigatorio=False, tamanho_max=20)
 
    sql = """
        INSERT INTO VIDAPET
            (NOME_PET, TIPO_PET, RACA, IDADE, PESO, NOME_TUTOR, TELEFONE)
        VALUES
            (:nome_pet, :tipo_pet, :raca, :idade, :peso, :nome_tutor, :telefone)
    """
 
    parametros = {
        "nome_pet": nome_pet,
        "tipo_pet": tipo_pet,
        "raca": raca,
        "idade": idade,
        "peso": peso,
        "nome_tutor": nome_tutor,
        "telefone": telefone
    }
 
    sucesso, erro = executar_alteracao(sql, parametros)
 
    if sucesso:
        print("Pet cadastrado com sucesso!")
    elif "ORA-00001" in str(erro):
        print("Erro: o ID gerado já foi usado por outro cadastro. Tente novamente.")
    else:
        print("Erro ao cadastrar:", erro)
 
 
# ============================================================
# READ
# ============================================================
 
def consultar_pets():
    print("\n--- TODOS OS PETS ---")
 
    pets, sucesso = buscar_pets()
 
    if not sucesso:
        return
 
    if len(pets) == 0:
        print("Nenhum pet cadastrado.")
        return
 
    for pet in pets:
        exibir_pet(pet)
 
 
def consultar_pet_por_id():
    print("\n--- CONSULTAR PET POR ID ---")
 
    id_pet = ler_inteiro("ID: ", minimo=1)
 
    pets, sucesso = buscar_pets(id_pet)
 
    if not sucesso:
        return
 
    if len(pets) == 0:
        print("Pet não encontrado.")
        return
 
    exibir_pet(pets[0])
 
 
# ============================================================
# UPDATE
# ============================================================
 
def alterar_pet():
    print("\n--- ALTERAR PET ---")
 
    id_pet = ler_inteiro("ID do pet: ", minimo=1)
 
    pets, sucesso = buscar_pets(id_pet)
 
    if not sucesso:
        return
 
    if len(pets) == 0:
        print("Pet não encontrado.")
        return
 
    atual = pets[0]
    exibir_pet(atual)
    print("Digite os novos dados (Enter mantém o valor atual).")
 
    nome_pet = ler_texto("Nome: ", obrigatorio=False, tamanho_max=100) or atual[1]
    tipo_pet = ler_texto("Tipo: ", obrigatorio=False, tamanho_max=30) or atual[2]
    raca = ler_texto("Raça: ", obrigatorio=False, tamanho_max=60) or atual[3]
 
    while True:
        texto_idade = input("Idade: ").strip()
 
        if texto_idade == "":
            idade = atual[4]
            break
 
        try:
            idade = int(texto_idade)
        except ValueError:
            print("Digite um número inteiro válido.")
            continue
 
        if idade < 0:
            print("A idade não pode ser negativa.")
            continue
 
        break
 
    peso = ler_peso("Peso: ")
    if peso is None:
        peso = atual[5]
 
    nome_tutor = ler_texto("Tutor: ", obrigatorio=False, tamanho_max=100) or atual[6]
    telefone = ler_texto("Telefone: ", obrigatorio=False, tamanho_max=20) or atual[7]
 
    sql = """
        UPDATE VIDAPET
        SET
            NOME_PET = :nome_pet,
            TIPO_PET = :tipo_pet,
            RACA = :raca,
            IDADE = :idade,
            PESO = :peso,
            NOME_TUTOR = :nome_tutor,
            TELEFONE = :telefone
        WHERE ID_PET = :id_pet
    """
 
    parametros = {
        "nome_pet": nome_pet,
        "tipo_pet": tipo_pet,
        "raca": raca,
        "idade": idade,
        "peso": peso,
        "nome_tutor": nome_tutor,
        "telefone": telefone,
        "id_pet": id_pet
    }
 
    sucesso, erro = executar_alteracao(sql, parametros)
 
    if sucesso:
        print("Pet alterado com sucesso!")
    else:
        print("Erro ao alterar:", erro)
 
 
# ============================================================
# DELETE
# ============================================================
 
def confirmar(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
 
        if resposta == "S":
            return True
        if resposta == "N":
            return False
 
        print("Responda com S ou N.")
 
 
def excluir_pet():
    print("\n--- EXCLUIR PET ---")
 
    id_pet = ler_inteiro("ID do pet: ", minimo=1)
 
    pets, sucesso = buscar_pets(id_pet)
 
    if not sucesso:
        return
 
    if len(pets) == 0:
        print("Pet não encontrado.")
        return
 
    pet = pets[0]
    print("ID:", pet[0], "| Nome:", pet[1], "| Tipo:", pet[2], "| Tutor:", pet[6])
 
    if not confirmar("Deseja realmente excluir? (S/N): "):
        print("Exclusão cancelada. O registro foi mantido.")
        return
 
    sql = "DELETE FROM VIDAPET WHERE ID_PET = :id_pet"
 
    sucesso, erro = executar_alteracao(sql, {"id_pet": id_pet})
 
    if sucesso:
        print("Pet excluído com sucesso!")
    else:
        print("Erro ao excluir:", erro)
 
 
# ============================================================
# RELATÓRIO HTML
# ============================================================
 
def gerar_html():
    print("\n--- GERAR RELATÓRIO HTML ---")
 
    pets, sucesso = buscar_pets()
 
    if not sucesso:
        print("Relatório não gerado.")
        return
 
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
 
    if len(pets) == 0:
        conteudo = "<p class=\"vazio\">Nenhum pet cadastrado.</p>"
    else:
        linhas = ""
 
        for pet in pets:
            linhas += (
                "<tr>"
                f"<td>{pet[0]}</td>"
                f"<td>{escape(str(pet[1]))}</td>"
                f"<td>{escape(str(pet[2]))}</td>"
                f"<td>{escape(pet[3] or '-')}</td>"
                f"<td>{pet[4]}</td>"
                f"<td>{formatar_peso(pet[5])}</td>"
                f"<td>{escape(str(pet[6]))}</td>"
                f"<td>{escape(pet[7] or '-')}</td>"
                f"<td>{formatar_data(pet[8])}</td>"
                "</tr>\n"
            )
 
        conteudo = f"""
        <table>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Tipo</th>
                <th>Raça</th>
                <th>Idade</th>
                <th>Peso (kg)</th>
                <th>Tutor</th>
                <th>Telefone</th>
                <th>Data de cadastro</th>
            </tr>
            {linhas}
        </table>
        """
 
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Relatório VidaPet</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 30px;
        }}
        .container {{
            max-width: 1100px;
            margin: auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
        }}
        h1 {{
            text-align: center;
        }}
        .data {{
            text-align: center;
            color: #666666;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #cccccc;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #333333;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .vazio {{
            text-align: center;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>VidaPet - Relatório de Pets</h1>
        <p class="data">Gerado em: {agora}</p>
        {conteudo}
    </div>
</body>
</html>
"""
    
    ARQUIVO_HTML = "relatório_pets.html"
    
    try:
        with open(ARQUIVO_HTML, "w", encoding="utf-8") as arquivo:
            arquivo.write(html)
 
        print("Arquivo", ARQUIVO_HTML, "gerado com sucesso!")
 
    except OSError as erro:
        print("Erro ao gravar o arquivo:", erro)
 
 
# ============================================================
# MENU
# ============================================================
 
def exibir_menu():
    print("\n===== VIDAPET =====")
    print("1 - Cadastrar pet")
    print("2 - Consultar todos os pets")
    print("3 - Consultar pet por ID")
    print("4 - Alterar pet")
    print("5 - Excluir pet")
    print("6 - Gerar relatório HTML")
    print("0 - Sair")
 
 
def menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "1":
            cadastrar_pet()
        elif opcao == "2":
            consultar_pets()
        elif opcao == "3":
            consultar_pet_por_id()
        elif opcao == "4":
            alterar_pet()
        elif opcao == "5":
            excluir_pet()
        elif opcao == "6":
            gerar_html()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")
 
 
if __name__ == "__main__":
    menu()