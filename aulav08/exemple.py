import oracledb
from flask import Flask, request, redirect, url_for, render_template_string
# ============================================================
# CONFIGURAÇÕES DO BANCO DE DADOS ORACLE
# ============================================================
USUARIO = "rm570933"
SENHA = "200308"
HOST = "oracle.fiap.com.br"
PORTA = 1521
SERVICE_NAME = "ORCL"
# ============================================================
# CRIAÇÃO DO DSN
# ============================================================
dsn = oracledb.makedsn(
    HOST,
    PORTA,
    service_name=SERVICE_NAME
)
# ============================================================
# CLASSE DE CONEXÃO COM O BANCO
# ============================================================
class BancoDados:
    def conectar(self):
        return oracledb.connect(
            user=USUARIO,
            password=SENHA,
            dsn=dsn
        )
# ============================================================
# CLASSE PET
# Representa um registro da tabela PETSHOP
# ============================================================
class Pet:
    def __init__(self, id_pet, tipo_pet, nome_pet, idade):
        self.id_pet = id_pet
        self.tipo_pet = tipo_pet
        self.nome_pet = nome_pet
        self.idade = idade
# ============================================================
# CLASSE DAO
# Responsável pelas operações no banco de dados
# ============================================================
class PetDAO:
    def __init__(self):
        self.banco = BancoDados()
    # --------------------------------------------------------
    # INCLUIR
    # --------------------------------------------------------
    def incluir(self, pet):
        conn = None
        cursor = None
        try:
            conn = self.banco.conectar()
            cursor = conn.cursor()
            sql = """
                INSERT INTO PETSHOP
                (
                    ID_PET,
                    TIPO_PET,
                    NOME_PET,
                    IDADE
                )
                VALUES
                (
                    :id_pet,
                    :tipo_pet,
                    :nome_pet,
                    :idade
                )
            """
            cursor.execute(
                sql,
                {
                    "id_pet": pet.id_pet,
                    "tipo_pet": pet.tipo_pet,
                    "nome_pet": pet.nome_pet,
                    "idade": pet.idade
                }
            )
            conn.commit()
            return True, "Pet cadastrado com sucesso!"
        except oracledb.Error as erro:
            if conn:
                conn.rollback()
            return False, f"Erro ao cadastrar: {erro}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    # --------------------------------------------------------
    # CONSULTAR TODOS
    # --------------------------------------------------------
    def consultar_todos(self):
        conn = None
        cursor = None
        try:
            conn = self.banco.conectar()
            cursor = conn.cursor()
            sql = """
                SELECT
                    ID_PET,
                    TIPO_PET,
                    NOME_PET,
                    IDADE
                FROM PETSHOP
                ORDER BY ID_PET
            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            lista_pets = []
            for registro in registros:
                pet = Pet(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3]
                )
                lista_pets.append(pet)
            return lista_pets
        except oracledb.Error as erro:
            print("Erro ao consultar:", erro)
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    # --------------------------------------------------------
    # CONSULTAR POR ID
    # --------------------------------------------------------
    def consultar_por_id(self, id_pet):
        conn = None
        cursor = None
        try:
            conn = self.banco.conectar()
            cursor = conn.cursor()
            sql = """
                SELECT
                    ID_PET,
                    TIPO_PET,
                    NOME_PET,
                    IDADE
                FROM PETSHOP
                WHERE ID_PET = :id_pet
            """
            cursor.execute(
                sql,
                {
                    "id_pet": id_pet
                }
            )
            registro = cursor.fetchone()
            if registro:
                return Pet(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3]
                )
            return None
        except oracledb.Error as erro:
            print("Erro ao consultar:", erro)
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    # --------------------------------------------------------
    # ALTERAR
    # -------------------------------------------------------
    def alterar(self, pet):
        conn = None
        cursor = None
        try:
            conn = self.banco.conectar()
            cursor = conn.cursor()
            sql = """
                UPDATE PETSHOP
                SET
                    TIPO_PET = :tipo_pet,
                    NOME_PET = :nome_pet,
                    IDADE = :idade
                WHERE
                    ID_PET = :id_pet
            """
            cursor.execute(
                sql,
                {
                    "tipo_pet": pet.tipo_pet,
                    "nome_pet": pet.nome_pet,
                    "idade": pet.idade,
                    "id_pet": pet.id_pet
                }
            )
            conn.commit()
            return True, "Pet alterado com sucesso!"
        except oracledb.Error as erro:
            if conn:
                conn.rollback()
            return False, f"Erro ao alterar: {erro}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    # --------------------------------------------------------
    # EXCLUIR
    # --------------------------------------------------------
    def excluir(self, id_pet):
        conn = None
        cursor = None
        try:
            conn = self.banco.conectar()
            cursor = conn.cursor()
            sql = """
                DELETE FROM PETSHOP
                WHERE ID_PET = :id_pet
            """
            cursor.execute(
                sql,
                {
                    "id_pet": id_pet
                }
            )
            conn.commit()
            return True, "Pet excluído com sucesso!"
        except oracledb.Error as erro:
            if conn:
                conn.rollback()
            return False, f"Erro ao excluir: {erro}"
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
# ============================================================
# CRIAÇÃO DA APLICAÇÃO FLASK
# ============================================================
app = Flask(__name__)
dao = PetDAO()
# ============================================================
# HTML PRINCIPAL
# ============================================================
HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Pet Shop - CRUD Oracle</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 30px;
        }
        .container {
            width: 90%;
            max-width: 1000px;
            margin: auto;
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px #ccc;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        h2 {
            color: #555;
            border-bottom: 1px solid #ddd;
            padding-bottom: 8px;
        }

        form {
            margin-bottom: 20px;
        }
        input, select {
            padding: 10px;
            margin: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            padding: 10px 15px;
            background-color: #333;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #555;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }

        th {
            background-color: #333;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f5f5f5;
        }

        .mensagem {
            padding: 15px;
            margin-bottom: 20px;
            background-color: #e8f5e9;
            border-radius: 5px;
            color: #2e7d32;
        }

        .erro {
            padding: 15px;
            margin-bottom: 20px;
            background-color: #ffebee;
            border-radius: 5px;
            color: #c62828;
        }

        a {
            text-decoration: none;
            color: white;
        }
        .btn-excluir {
            background-color: #c62828;
        }

        .btn-editar {
            background-color: #1565c0;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>🐾 PET SHOP</h1>
    {% if mensagem %}
        <div class="mensagem">
            {{ mensagem }}
        </div>
    {% endif %}
    {% if erro %}
        <div class="erro">
            {{ erro }}
        </div>
    {% endif %}
    <!-- ================================================== -->
    <!-- CADASTRO -->
    <!-- ================================================== -->
    <h2>➕ Cadastrar Pet</h2>
    <form action="/cadastrar" method="POST">
        <input
            type="number"
            name="id_pet"
            placeholder="ID do Pet"
            required
        >
        <select name="tipo_pet" required>
            <option value="">Tipo do Pet</option>
            <option value="Cachorro">Cachorro</option>
            <option value="Gato">Gato</option>
            <option value="Passaro">Pássaro</option>
            <option value="Outro">Outro</option>
        </select>
        <input
            type="text"
            name="nome_pet"
            placeholder="Nome do Pet"
            required
        >
        <input
            type="number"
            name="idade"
            placeholder="Idade"
            min="0"
            required
        >
        <button type="submit">
            Cadastrar
        </button>
    </form>
    <!-- ================================================== -->
    <!-- CONSULTA POR ID -->
    <!-- ================================================== -->
    <h2>🔎 Consultar Pet</h2>
    <form action="/consultar" method="GET">
        <input
            type="number"
            name="id_pet"
            placeholder="Digite o ID"
            required
        >
        <button type="submit">
            Consultar
        </button>
    </form>
    {% if pet_consultado %}
        <h3>Pet encontrado:</h3>
        <p>
            <strong>ID:</strong>
            {{ pet_consultado.id_pet }}
        </p>
        <p>
            <strong>Tipo:</strong>
            {{ pet_consultado.tipo_pet }}
        </p>
        <p>
            <strong>Nome:</strong>
            {{ pet_consultado.nome_pet }}
        </p>
        <p>
            <strong>Idade:</strong>
            {{ pet_consultado.idade }}
        </p>
    {% endif %}

    <!-- ================================================== -->
    <!-- LISTAGEM -->
    <!-- ================================================== -->
    <h2>📋 Pets cadastrados</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Tipo</th>
            <th>Nome</th>
            <th>Idade</th>
            <th>Ações</th>
        </tr>
        {% for pet in pets %}
        <tr>
            <td>
                {{ pet.id_pet }}
            </td>
            <td>
                {{ pet.tipo_pet }}
            </td>
            <td>
                {{ pet.nome_pet }}
            </td>
            <td>
                {{ pet.idade }}
            </td>
            <td>
                <a href="/editar/{{ pet.id_pet }}">
                    <button class="btn-editar">
                        Editar
                   </button>
                </a>
                <form
                    action="/excluir/{{ pet.id_pet }}"
                    method="POST"
                    style="display:inline;"
                    onsubmit="return confirm('Deseja realmente excluir este pet?');"
                >
                    <button
                        type="submit"
                        class="btn-excluir"
                    >
                       Excluir
                    </button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
</div>
</body>
</html>
"""
# ============================================================
# ROTA PRINCIPAL
# ============================================================
@app.route("/")
def index():
    pets = dao.consultar_todos()
    return render_template_string(
        HTML,
        pets=pets,
        mensagem=None,
        erro=None,
        pet_consultado=None
    )
# ============================================================
# ROTA - CADASTRAR
# ============================================================
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    try:
        id_pet = int(request.form["id_pet"])
        tipo_pet = request.form["tipo_pet"]
        nome_pet = request.form["nome_pet"]
        idade = int(request.form["idade"])
        pet = Pet(
            id_pet,
            tipo_pet,
            nome_pet,
            idade
        )
        sucesso, mensagem = dao.incluir(pet)
        pets = dao.consultar_todos()
        if sucesso:
            return render_template_string(
                HTML,
                pets=pets,
                mensagem=mensagem,
                erro=None,
                pet_consultado=None
            )
        else:
            return render_template_string(
                HTML,
                pets=pets,
                mensagem=None,
                erro=mensagem,
                pet_consultado=None
            )
    except ValueError:
        pets = dao.consultar_todos()
        return render_template_string(
            HTML,
            pets=pets,
            mensagem=None,
            erro="Digite valores numéricos válidos para ID e idade.",
            pet_consultado=None
        )
# ============================================================
# ROTA - CONSULTAR
# ============================================================
@app.route("/consultar")
def consultar():
    try:
        id_pet = int(request.args["id_pet"])
        pet = dao.consultar_por_id(id_pet)
        pets = dao.consultar_todos()
        if pet:
            return render_template_string(
                HTML,
                pets=pets,
                mensagem=None,
                erro=None,
                pet_consultado=pet
            )
        else:
            return render_template_string(
                HTML,
                pets=pets,
                mensagem=None,
                erro="Pet não encontrado.",
                pet_consultado=None
            )
    except ValueError:
        pets = dao.consultar_todos()
        return render_template_string(
            HTML,
            pets=pets,
            mensagem=None,
            erro="Digite um ID válido.",
            pet_consultado=None
        )
# ============================================================
# ROTA - EDITAR
# ============================================================
@app.route("/editar/<int:id_pet>", methods=["GET", "POST"])
def editar(id_pet):
    pet = dao.consultar_por_id(id_pet)
    if not pet:
        return redirect(url_for("index"))
    if request.method == "POST":
        tipo_pet = request.form["tipo_pet"]
        nome_pet = request.form["nome_pet"]
        idade = int(request.form["idade"])
        pet.tipo_pet = tipo_pet
        pet.nome_pet = nome_pet
        pet.idade = idade
        sucesso, mensagem = dao.alterar(pet)
        pets = dao.consultar_todos()
        return render_template_string(
            HTML,
            pets=pets,
            mensagem=mensagem if sucesso else None,
            erro=None if sucesso else mensagem,
            pet_consultado=None
        )
    HTML_EDICAO = """
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>

        <meta charset="UTF-8">

        <title>Editar Pet</title>

        <style>

            body {

                font-family: Arial;

                background-color: #f2f2f2;

                padding: 40px;

            }

            .container {

                background-color: white;

                max-width: 600px;

                margin: auto;

                padding: 30px;

                border-radius: 10px;

                box-shadow: 0 0 10px #ccc;

            }

            input, select {

                width: 100%;

                padding: 10px;

                margin: 8px 0;

                box-sizing: border-box;

            }

            button {

                padding: 12px;

                background-color: #333;

                color: white;

                border: none;

                border-radius: 5px;

                cursor: pointer;

            }

            a {

                text-decoration: none;

                color: #333;

            }

        </style>

    </head>


    <body>


    <div class="container">


        <h1>✏️ Editar Pet</h1>


        <form method="POST">


            <label>ID</label>

            <input
                type="number"
                value="{{ pet.id_pet }}"
                disabled
            >


            <label>Tipo</label>

            <select name="tipo_pet" required>

                <option value="Cachorro"
                    {% if pet.tipo_pet == "Cachorro" %}
                        selected
                    {% endif %}
                >
                    Cachorro
                </option>


                <option value="Gato"
                    {% if pet.tipo_pet == "Gato" %}
                        selected
                    {% endif %}
                >
                    Gato
                </option>


                <option value="Passaro"
                    {% if pet.tipo_pet == "Passaro" %}
                        selected
                    {% endif %}
                >
                    Pássaro
                </option>


                <option value="Outro"
                    {% if pet.tipo_pet == "Outro" %}
                        selected
                    {% endif %}
                >
                    Outro
                </option>

            </select>


            <label>Nome</label>

            <input
                type="text"
                name="nome_pet"
                value="{{ pet.nome_pet }}"
                required
            >


            <label>Idade</label>

            <input
                type="number"
                name="idade"
                value="{{ pet.idade }}"
                min="0"
                required
            >


            <button type="submit">

                Salvar Alterações

            </button>


        </form>


        <br>


        <a href="/">

            ← Voltar

        </a>


    </div>


    </body>

    </html>

    """


    return render_template_string(
        HTML_EDICAO,
        pet=pet
    )


# ============================================================
# ROTA - EXCLUIR
# ============================================================

@app.route("/excluir/<int:id_pet>", methods=["POST"])

def excluir(id_pet):

    sucesso, mensagem = dao.excluir(id_pet)


    pets = dao.consultar_todos()


    return render_template_string(
        HTML,
        pets=pets,
        mensagem=mensagem if sucesso else None,
        erro=None if sucesso else mensagem,
        pet_consultado=None
    )


# ============================================================
# INICIAR APLICAÇÃO
# ============================================================

if __name__ == "__main__":

    print("=" * 50)

    print("SISTEMA PET SHOP")

    print("=" * 50)

    print("Banco de dados: Oracle FIAP")

    print("Usuário:", USUARIO)

    print("Servidor:", HOST)

    print("Porta:", PORTA)

    print("Service Name:", SERVICE_NAME)

    print("=" * 50)

    print("Acesse no navegador:")

    print("http://127.0.0.1:5000")

    print("=" * 50)


    app.run(debug=True)