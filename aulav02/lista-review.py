dados = "Ana;Notebook;4500"
#print(type(dados))
#Aqui vamos printar o tipo de dado que é o 'dados'

campos = dados.split(";")
#.split vai separar os dados em uma lista dependendo qual é a variável que vai separar, nesse caso ';'
#print(type(campos))
#print(campos)

nome = "  SEU NOME.... VAI SER JOSÉ   "
#print(nome.strip()) #.strip vai tirar os espaços dos cantos
#print(nome.strip().lower()) #.lower vai deixar tudo em minúsculo

#Aqui, vamos botar """ para criar um "mini-banco de dados"
dados = """
matheus@gmail.ex;Notebook;4500
carlosed@gmail.com;Mouse;100
evandro@outlook.com;Teclado;250
mariana@gmail.com;Monitor;4000
kakakaleb@gmail.sense;Headset;850
noah@noah.noah;Notebook;11500
"""

#Vamos tratar esses dados de forma rústica:
dados = dados.strip()
linhas = dados.splitlines()
#print(linhas)
#print(len(linhas))

linha = linhas[0]
#print(linha)

campos = linha.split(";")
#print(campos)

email = campos[0].strip().lower()
produto = campos[1].strip().lower()
preco = float(campos[2].strip())
#print(type(preco))
#print(type(campos[2]))

#Registrando:
registro = [email, produto, preco]
#print(registro)

registros = []
registros.append(registro)
#print(registros)

#Registros múltiplos:
for linha in linhas:
    campos = linha.split(";")
    email = campos[0].strip().lower()
    produto = campos[1].strip().lower()
    preco = float(campos[2].strip())
    registro = [email, produto, preco]
    registros = []
    registros.append(registro)

    for registro in registros:
        print(registro)

    for registro in registros:
        print("Cliente:", registro[0], "\nProduto:", registro[1], "\nPreço:", registro[2])

    for registro in registros:
        precos = []
        precos.append(registro[2])
        len(precos) #Mostra quantidade de preços
        sum(precos) #Mostra a soma dos preços
        max(precos) #Mostra o máximo dentre os preços
        min(precos) #Mostar o mínimo dentre os preços
        media = (max(precos) + min(precos))/2
        print(media)
        precos_ordenados = sorted(precos) #Mostra os preços de forma ordenada
        print(precos_ordenados)

produto_busca = input("Digite o produto: ").strip().lower()
for registro in registros:
    if registro[1] == produto_busca:
            print("Produto:", registro[1], "\nValor:", registro[2])
    