#Importamos a biblioteca requests novamente
import requests

#A URL identifica o recurso/API que queremos consultar
url = "https://jsonplaceholder.typicode.com/users"

#Realize as tratativas de erros novamente
try:

    #get() vai pegar as informações, da API, como indicado pela 'url', e jogar na variável resposta. 'timeout' vai definir um limite de tantos segundos para pegar
    resposta = requests.get(url, timeout=0.1)

    #raise_for_status trás se o servidor encontrou algum erro HTTP
    resposta.raise_for_status()

    #json() transforma os dados recebidos em estruturas Python. Nesse caso, teremos uma lista de dicionários. E joga na variável 'usuarios'
    usuarios = resposta.json()

    #PARA GERAR UMA PÁGINA HTML COM OS ELEMENTOS DA API
    html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usuários da API</title>
</head>
<body>
    <h1>Usuários cadastrados</h1>
    <p>Dados obtidos por meio de uma API utilizando Python.</p>
    <hr>
</body>
</html>
"""

    for usuario in usuarios:
        id = usuario["id"]
        nome = usuario["name"]
        email = usuario["email"]
        telefone = usuario["phone"]
        cidade = usuario["address"]["city"]

        html += f"""
    <div>
        <h2>{nome}</h2>
        <p><strong>E-mail: <strong>{email}</p>
        <p><strong>Telefone: <strong>{telefone}</p>
        <p><strong>Cidade: <strong>{cidade}</p>
        <p><strong>ID:<strong>{id}</p>
    </div>
    <hr>
"""

    with open("usuários.html", "w", encoding="uft-8") as arquivo:
        arquivo.write(html)

    print("\nPágina criada com sucesso")

    print("\nArquivo gerado: usuarios.html")

except requests.exceptions.ConnectionError:
    print("\nErro de conexão")