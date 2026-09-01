#Importamos a biblioteca requests novamente
import requests

#Importamos a biblioteca pathlib, que vai nos ajudar a criar o arquivo HTML
from pathlib import Path

#importamos também a biblioteca webbrowser, que vai nos ajudar a abrir o HTML no navegador
import webbrowser

#A URL identifica o recurso/API que queremos consultar
url = "https://jsonplaceholder.typicode.com/users"

#Realize as tratativas de erros novamente
try:

    #get() vai pegar as informações, da API, como indicado pela 'url', e jogar na variável resposta. 'timeout' vai definir um limite de tantos segundos para pegar
    resposta = requests.get(url, timeout=10)

    #raise_for_status trás se o servidor encontrou algum erro HTTP
    resposta.raise_for_status()

    #json() transforma os dados recebidos em estruturas Python. Nesse caso, teremos uma lista de dicionários. E joga na variável 'usuarios'
    usuarios = resposta.json()

    #PARA GERAR UMA PÁGINA HTML COM OS ELEMENTOS DA API

    #Precisamos criar uma variável que vai recever um código HTML, que vai ser a estrutura base
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
"""

    #Percorremos essa lista de usuários da API para poder incrementar TODOS os usuários no HTML, para isso usamos o 'for' que vai pegar cada elemento da lista e jogar na sua respectiva variável. Como é um dicionário, a gente usa a chave para chegar no valor.
    for usuario in usuarios:
        id = usuario["id"]
        nome = usuario["name"]
        email = usuario["email"]
        telefone = usuario["phone"]
        cidade = usuario["address"]["city"]

        #Adicão de mais HTML na variável html por conta do += e como
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

    html += """
</body>
</html>
"""

    #Ele cria o arquivo HTML, com o nome de 'usuários.html', e escreve todo  conteúdo da variável html dentro dele
    with open("usuários.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    #Para abrir esse arquivo no navegador, criamos uma variável que vai receber o caminho do arquivo no nosso sistema, e depois transformamos ele num caminho que o navegador consiga entender, com endereco_arquivo recebendo o caminho do arquivo em formato de URI. Por fim, usamos o webbrowser.open() para abrir o arquivo no navegador
    arquivo_path = Path("usuários.html").resolve()
    endereco_arquivo = arquivo_path.as_uri()
    webbrowser.open(endereco_arquivo)
    print("\nPágina criada com sucesso")
    print("\nAbrindo página no navegador...")

#Caso a internet seja o problema impedindo de consultar a API
except requests.exceptions.ConnectionError:
    print("\n⚠️ERRO DE CONEXÃO⚠️\nVerifique sua internet e tente novamente")

#Caso o tempo de conexão seja o problema (Vale pensar se o tempo de consultar a API é muito curta)
except requests.exceptions.Timeout:
    print("\n⚠️ERRO DE TIMEOUT⚠️\nA conexão demorou, tente novamente")

#Caso o HTTP da API esteja errada, ou não disponível no momento
except requests.exceptions.HTTPError as erro:
    print("\n⚠️ERRO HTTP⚠️", erro)

#Caso a chave que irá ser chamado não exista, como um 'nome' ao invés de 'name', ou um simples erro de digitação
except KeyError as erro:
    print("\n⚠️ERRO DE CHAVE⚠️\nCampo não encontrado na resposta:", erro)

#==========================================================================================================================================
# QUEBRA DE LINHA QUEBRA DE LINHA QUEBRA DE LINHA QUEBRA DE LINHA QUEBRA DE LINHA QUEBRA DE LINHA QUEBRA DE LINHA QUEBRA DE LINHA QUEBRA
#==========================================================================================================================================

#Agora, para o seguinte exercício, vamos criar uma outra página, mas apenas com os usuários que o usuário escrever a cidade. Exibe então a quantidade de usuários encontrados, e caso não encontre nenhum, exiba uma mensagem de erro

print("\nAgora vamos criar uma página HTML apenas com os usuários que moram na cidade que você digitar")

#Tratativas de erros pela milésima vez
try:
    #get() vai pegar as informações, da API, como indicado pela 'url', e jogar na variável resposta. 'timeout' vai definir um limite de tantos segundos para pegar
    resposta = requests.get(url, timeout=10)

    #raise_for_status trás se o servidor encontrou algum erro HTTP
    resposta.raise_for_status()

    #json() transforma os dados recebidos em estruturas Python. Nesse caso, teremos uma lista de dicionários. E joga na variável 'usuarios'
    usuarios = resposta.json()

    #Criamos uma variável que vai receber a cidade que o usuário deseja buscar
    cidade_busca = input("Digite a cidade que deseja buscar: ").strip().lower()

    #PARA GERAR UMA PÁGINA HTML COM OS ELEMENTOS DA API

    #Precisamos criar uma variável que vai recever um código HTML dessa nova página, que vai ser a estrutura base
    html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usuários da API</title>
</head>
<body>
    <h1>Usuários na cidade de {cidade_busca}</h1>
    <p>Dados obtidos por meio de uma API utilizando Python.</p>
    <hr>
"""

    #Criamos então uma boolean que vai nos ajudar a saber se encontramos algum usuário ou não
    encontrado = False

    #Criamos uma variável que vai contar a quantidade de usuários encontrados
    qtd_encontrados = 0

    #Criamos uma lista que vai receber os usuários encontrados
    lista_encontrados = []

    #Percorremos essa lista de usuários da API para poder incrementar TODOS os usuários no HTML, para isso usamos o 'for' que vai pegar cada elemento da lista e jogar na sua respectiva variável. Como é um dicionário, a gente usa a chave para chegar no valor. Nesse caso, jogamos na lista de encontrados os valores que forem igual a cidade que o usuário digitou, e além disso, a quantidade de itens encontrados aumenta.
    for usuario in usuarios:
        cidade = usuario["address"]["city"].strip().lower()

        if cidade_busca == cidade:
            encontrado = True
            qtd_encontrados += 1
            id = usuario["id"]
            nome = usuario["name"]
            telefone = usuario["phone"]
            email = usuario["email"]
            lista_encontrados.append({
                    "id": id,
                    "nome": nome,
                    "telefone": telefone,
                    "email": email
                })
            
    if encontrado:
        html += f"""
    <h2>Quantidade de usuários encontrados: {qtd_encontrados}</h2>
    <hr>
        """
    else:
        html += f"""
    <h2>Nenhum usuário encontrado na cidade</h2>
    <hr>
        """

        print(f"\nNenhum usuário encontrado na cidade de {cidade_busca}")

    for usuario in lista_encontrados:
        id = usuario["id"]
        nome = usuario["nome"]
        telefone = usuario["telefone"]
        email = usuario["email"]

        #Adição do HTML na variável html por conta do +=
        html += f"""
    <div>
        <h2>{nome}</h2>
        <p><strong>E-mail: <strong>{email}</p>
        <p><strong>Telefone: <strong>{telefone}</p>
        <p><strong>ID:<strong>{id}</p>
    </div>
    <hr>
    """

    html += """
</body>
</html>
    """

    #Ele cria o arquivo HTML, com o nome de 'usuários-cidade.html', e escreve todo  conteúdo da variável html dentro dele
    with open("usuários-cidade.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    #Para abrir esse arquivo no navegador, criamos uma variável que vai receber o caminho do arquivo no nosso sistema, e depois transformamos ele num caminho que o navegador consiga entender, com endereco_arquivo recebendo o caminho do arquivo em formato de URI. Por fim, usamos o webbrowser.open() para abrir o arquivo no navegador
    arquivo_path = Path("usuários-cidade.html").resolve()
    endereco_arquivo = arquivo_path.as_uri()
    webbrowser.open(endereco_arquivo)
    print("\nPágina criada com sucesso")
    print("\nAbrindo página no navegador...")

#Caso a internet seja o problema impedindo de consultar a API
except requests.exceptions.ConnectionError:
    print("\n⚠️ERRO DE CONEXÃO⚠️\nVerifique sua internet e tente novamente")

#Caso o tempo de conexão seja o problema (Vale pensar se o tempo de consultar a API é muito curta)
except requests.exceptions.Timeout:
    print("\n⚠️ERRO DE TIMEOUT⚠️\nA conexão demorou, tente novamente")

#Caso o HTTP da API esteja errada, ou não disponível no momento
except requests.exceptions.HTTPError as erro:
    print("\n⚠️ERRO HTTP⚠️", erro)

#Caso a chave que irá ser chamado não exista, como um 'nome' ao invés de 'name', ou um simples erro de digitação
except KeyError as erro:
    print("\n⚠️ERRO DE CHAVE⚠️\nCampo não encontrado na resposta:", erro)

#Caso a interpretação dos dados não seja possível, como digitar um '2' ao invés de 'Abóbora'. Erro do usuário
except ValueError:
    print("\n⚠️ERRO DE INTERPRETAÇÃO⚠️\nNão foi possível interpretar os dados do usuário")