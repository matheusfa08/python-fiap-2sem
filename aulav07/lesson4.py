from flask import Flask, request, redirect, url_for, render_template_string
import oracledb
# ============================================================
# CONFIGURAÇÕES DO ORACLE
# ============================================================
USUARIO = "rm570933"
SENHA = "200308"
HOST = "oracle.fiap.com.br"
PORTA = 1521
SERVICE_NAME = "ORCL"
# ============================================================
# CONFIGURAÇÃO DO FLASK
# ============================================================
app = Flask(__name__)
# ============================================================
# CRIANDO O DSN
# ============================================================
dsn = oracledb.makedsn(
   HOST,
   PORTA,
   service_name=SERVICE_NAME
)
# ============================================================
# FUNÇÃO PARA CONECTAR AO ORACLE
# ============================================================
def conectar():
   try:
      conn = oracledb.connect(
         user=USUARIO,
         password=SENHA,
         dsn=dsn
      )
      return conn
   except oracledb.Error as erro:
      print("Erro ao conectar ao Oracle:")
      print(erro)
      return None
# ============================================================
# HTML DA PÁGINA PRINCIPAL
# ============================================================
PAGINA_PRINCIPAL = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
 <meta charset="UTF-8">
 <title>Sistema PetShop</title>
 <style>
 body {
 font-family: Arial, sans-serif;
 background-color: #f2f2f2;
 margin: 0;
 padding: 30px;
 }
 .container {
 max-width: 1000px;
 margin: auto;
 background-color: white;
 padding: 30px;
 border-radius: 10px;
 }
 h1 {
 text-align: center;
 }
 h2 {
 margin-top: 30px;
 }
 form {
 margin-bottom: 20px;
 }
 input {
 padding: 10px;
 margin: 5px;
 }
 button {
 padding: 10px 15px;
 border: none;
 cursor: pointer;
 background-color: #333;
 color: white;
 }
 button:hover {
 background-color: #555;
 }
 table {
 width: 100%;
 border-collapse: collapse;
 margin-top: 20px;
 }
 th,
 td {
 border: 1px solid #cccccc;
 padding: 10px;
 text-align: center;
 }
 th {
 background-color: #333;
 color: white;
 }
 .editar {
 background-color: #555;
 color: white;
 padding: 8px;
 text-decoration: none;
 }
 .excluir {
 background-color: #222;
 }
 .mensagem {
 background-color: #eeeeee;
 padding: 15px;
 margin-bottom: 20px;
 }
 </style>
</head>
<body>
<div class="container">
 <h1> Sistema PetShop</h1>
 {% if mensagem %}
 <div class="mensagem">
 {{ mensagem }}
 </div>
 {% endif %}
 <!-- ================================================= -->
 <!-- CADASTRO -->
 <!-- ================================================= -->
 <h2>Cadastrar Pet</h2>
 <form action="/cadastrar" method="POST">
 <input
 type="number"
 name="id_pet"
 placeholder="ID"
 required
 >
 <input
 type="text"
 name="tipo_pet"
 placeholder="Tipo do Pet"
 required
 >
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
 <!-- ================================================= -->
 <!-- CONSULTA POR ID -->
 <!-- ================================================= -->
 <h2>Consultar Pet por ID</h2>
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
 <!-- ================================================= -->
 <!-- LISTAGEM -->
 <!-- ================================================= -->
 <h2>Pets Cadastrados</h2>
 {% if pets %}
 <table>
 <tr>
 <th>ID</th>
 <th>Tipo</th>
 <th>Nome</th>
 <th>Idade</th>
 <th>Alterar</th>
 <th>Excluir</th>
 </tr>
 {% for pet in pets %}
 <tr>
 <td>{{ pet[0] }}</td>
 <td>{{ pet[1] }}</td>
 <td>{{ pet[2] }}</td>
 <td>{{ pet[3] }}</td>
 <td>
 <a
 class="editar"
 href="/editar/{{ pet[0] }}"
 >
 Alterar
 </a>
 </td>
 <td>
 <form
 action="/excluir/{{ pet[0] }}"
 method="POST"
 onsubmit="return confirm('Deseja realmente excluir este pet?');"
 >
 <button
 class="excluir"
 type="submit"
 >
 Excluir
 </button>
 </form>
 </td>
 </tr>
 {% endfor %}
 </table>
 {% else %}
 <p>Nenhum pet cadastrado.</p>
 {% endif %}
</div>
</body>
</html>
"""
# ============================================================
# HTML DA PÁGINA DE ALTERAÇÃO
# ============================================================
PAGINA_EDITAR = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
 <meta charset="UTF-8">
 <title>Alterar Pet</title>
</head>
<body>
 <h1>Alterar Pet</h1>
 <form
 action="/editar/{{ pet[0] }}"
 method="POST"
 >
 <p>
 ID:
 <input
 type="number"
 value="{{ pet[0] }}"
 disabled
 >
 </p>
 <p>
 Tipo:
 <input
 type="text"
 name="tipo_pet"
 value="{{ pet[1] }}"
 required
 >
 </p>
 <p>
 Nome:
 <input
 type="text"
 name="nome_pet"
 value="{{ pet[2] }}"
 required
 >
 </p>
 <p>
 Idade:
 <input
 type="number"
 name="idade"
 value="{{ pet[3] }}"
 min="0"
 required
 >
 </p>
 <button type="submit">
 Salvar Alterações
 </button>
 </form>
 <br>
 <a href="/">
 Voltar
 </a>
</body>
</html>
"""
# ============================================================
# PÁGINA PRINCIPAL - CONSULTA DE TODOS
# ============================================================
@app.route("/")
def inicio():
   conn = conectar()
   if conn is None:
      return "Erro ao conectar ao Oracle."
   cursor = conn.cursor()
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
   except oracledb.Error as erro:
      print(erro)
      pets = []
   finally:
      cursor.close()
      conn.close()
   return render_template_string(
      PAGINA_PRINCIPAL,
      pets=pets
   )
# ============================================================
# INCLUSÃO
# ============================================================
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
   id_pet = request.form["id_pet"]
   tipo_pet = request.form["tipo_pet"]
   nome_pet = request.form["nome_pet"]
   idade = request.form["idade"]
   try:
      id_pet = int(id_pet)
      idade = int(idade)
   except ValueError:
      return "ID e idade devem ser números."
   conn = conectar()
   if conn is None:
      return "Erro de conexão."
   cursor = conn.cursor()
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
         id_pet=id_pet,
         tipo_pet=tipo_pet,
         nome_pet=nome_pet,
         idade=idade
      )
      conn.commit()
   except oracledb.Error as erro:
      conn.rollback()
      return f"Erro ao cadastrar: {erro}"
   finally:
      cursor.close()
      conn.close()
   return redirect(
      url_for("inicio")
   )
# ============================================================
# CONSULTA POR ID
# ============================================================
@app.route("/consultar")
def consultar():
   id_pet = request.args.get("id_pet")
   try:
      id_pet = int(id_pet)
   except (ValueError, TypeError):
      return "ID inválido."
   conn = conectar()
   if conn is None:
      return "Erro de conexão."
   cursor = conn.cursor()
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
   finally:
      cursor.close()
      conn.close()
   if pet is None:
      return """
      <h2>Pet não encontrado.</h2>
      <a href="/">
        Voltar
      </a>
      """
   return f"""
   <h1>Pet encontrado</h1>
   <p><strong>ID:</strong> {pet[0]}</p>
   <p><strong>Tipo:</strong> {pet[1]}</p>
   <p><strong>Nome:</strong> {pet[2]}</p>
   <p><strong>Idade:</strong> {pet[3]}</p>
   <a href="/">
     Voltar
   </a>
   """
# ============================================================
# ALTERAÇÃO
# ============================================================
@app.route(
 "/editar/<int:id_pet>",
 methods=["GET", "POST"]
)
def editar(id_pet):
 # --------------------------------------------------------
 # GET
 # Mostra os dados atuais no formulário
 # --------------------------------------------------------
   if request.method == "GET":
      conn = conectar()
      if conn is None:
         return "Erro de conexão."
      cursor = conn.cursor()
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
      finally:
         cursor.close()
         conn.close()
      if pet is None:
         return "Pet não encontrado."
      return render_template_string(
         PAGINA_EDITAR,
         pet=pet
      )
   # --------------------------------------------------------
   # POST
   # Recebe os novos dados
   # --------------------------------------------------------
   tipo_pet = request.form["tipo_pet"]
   nome_pet = request.form["nome_pet"]
   idade = request.form["idade"]
   try:
      idade = int(idade)
   except ValueError:
      return "Idade inválida."
   conn = conectar()
   if conn is None:
      return "Erro de conexão."
   cursor = conn.cursor()
   sql = """
   UPDATE petshop
   SET
     tipo_pet = :tipo_pet,
     nome_pet = :nome_pet,
     idade = :idade
   WHERE id_pet = :id_pet
   """
   try:
      cursor.execute(
         sql,
         tipo_pet=tipo_pet,
         nome_pet=nome_pet,
         idade=idade,
         id_pet=id_pet
      )
      conn.commit()
   except oracledb.Error as erro:
      conn.rollback()
      return f"Erro ao alterar: {erro}"
   finally:
      cursor.close()
      conn.close()
   return redirect(
      url_for("inicio")
   )
# ============================================================
# EXCLUSÃO
# ============================================================
@app.route(
 "/excluir/<int:id_pet>",
 methods=["POST"]
)
def excluir(id_pet):
   conn = conectar()
   if conn is None:
      return "Erro de conexão."
   cursor = conn.cursor()
   sql = """
   DELETE FROM petshop
   WHERE id_pet = :id_pet
   """
   try:
      cursor.execute(
         sql,
         id_pet=id_pet
      )
      conn.commit()
   except oracledb.Error as erro:
      conn.rollback()
      return f"Erro ao excluir: {erro}"
   finally:
      cursor.close()
      conn.close()
   return redirect(
      url_for("inicio")
   )
# ============================================================
# EXECUTANDO O SERVIDOR
# ============================================================
if __name__ == "__main__":
   app.run(
      debug=True
   )