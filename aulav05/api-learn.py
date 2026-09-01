#Importamos a biblioteca que você instalou
import requests

#A URL identifica o recurso/API que queremos consultar
url = "https://jsonplaceholder.typicode.com/users"

#Realize as tratativas de erros
try:

    #get() vai pegar as informações, da API, como indicado pela 'url', e jogar na variável resposta. 'timeout' vai definir um limite de tantos segundos para pegar
    resposta = requests.get(url, timeout=10)

    #raise_for_status trás
    resposta.raise_for_status()

    #json() transforma os dados recebidos em estruturas Python. Nesse caso, teremos uma lista de dicionários. E joga na variável 'usuarios'
    usuarios = resposta.json()

    print("======USUÁRIOS DA API======")

    #Para percorrer essa lista de usuários da API, usamos 'for'. Cada elemento é um dicionário
    for usuario in usuarios:
        print("ID:", usuario["id"], "| Nome:", usuario["name"], "| E-mail:", usuario["email"])

    #Vamos buscar um usuário:
    #Crie a variável que eceberá o nome que o usuário deseja buscar
    nome_busca = input("Digite parte do nome que deseja buscar: ").strip().lower()

    #Criamos então uma variável booleana
    encontrado = False

    #Para a lista de usuários percorremos ela em busca de cada usuário
    for usuario in usuarios:

        #Criamos essa variável para tratar o nome na lista, já que não tinhamos controle sobre a chave nem o valor
        nome = usuario["name"].strip().lower()

        #Se a variável que o usuário digitar tiver algum elemento da variável nome (Semelhanças), o programa muda encontrado para verdadeiro, o que impossibilita a mensagem de "erro", e em seguida fornece TODAS as informações sobre o nome buscado
        if nome_busca in nome:
            encontrado = True
            print("\nUsuário encontrado:")
            print("ID:", usuario["id"])
            print("Nome:", usuario["name"])
            print("E-mail:", usuario["email"])
            print("Telefone:", usuario["phone"])
            print("Cidade:", usuario["address"]["city"])

    #Se a variável encontrado continuar falsa até o final do código, ele nos dará uma mensagem de "erro", pois nunca entramos na condição para se tornar verdadeira
    if encontrado == False:
        print("\nNenhum usuário encontrado.")

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
    print("\n⚠️ERRO DE INTERPRETAÇÃO⚠️\nNão foi possível interpretar os dados")