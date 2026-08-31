#Transformando o ex3 em um menu interativo.

#Dados, aqui na variável 'dados', são definidos como uma string de múltiplas linhas, assim como definido pelas três aspas (""")
dados = """ 
ana@gmail.com;Notebook;4500;SP 
carlos@gmail.com;Mouse;80;RJ 
ana@gmail.com;Teclado;250;SP 
maria@gmail.com;Monitor;1200;MG 
carlos@gmail.com;Headset;350;RJ 
joao@gmail.com;Notebook;4500;PR 
maria@gmail.com;Mouse;80;MG 
""" 

#Vamos filtar a 'dados' para a 'dado', tirando os espaços desnecessários com o .strip()
dado = dados.strip()

#E agora, vamos separar as linhas dessa string numa lista, a 'linhas, assim podemos separar melhor cada campo, melhorando a classificação
linhas = dado.splitlines()

#Criada a lista 'registros' para armazenar cada campo existente, como exemplo: id, contato, nome. Então a 'registros' desse exemplo seria registros = [id, contato, nome] 
registros = []

#Criada a lista 'preços', que irá armazenar o campo referente ao preço gasto com os produtos deste exercício
precos = []

#Feita uma linha de repetição com for in, para cada item em 'linhas'
for linha in linhas:

    #'campos' vai receber cada campo de informação separadamente, com .split(";"), que vai separar a string em outras strings menores fazendo a deleção do caractér ;
    campos = linha.split(";")

    #'email', 'produto', 'preco' e 'estado' recebem os campos respectivos à suas posições na lista 'campos', e sem espaços extras, nem letras maiúsculas (Exceto 'preco' e 'estado'), com os .strip() e .lower(). 'preco' recebe um valor flutuante, que aceita casas decimais e apenas números, com o campo estando dentro do float()
    email = campos[0].strip().lower()
    produto = campos[1].strip().lower()
    preco = float(campos[2].strip())
    estado = campos[3].strip()

    #É criada uma lista 'registro' que guarda todos os campos de uma linha. Essa lista entra como um item na lista 'registros' com o .append()
    registro = [email, produto, preco, estado]
    registros.append(registro)

    #O 'preco' do produto é guardado na lista 'precos' com o .append()
    precos.append(preco)

#É criada a função que futuramente poderá ser chamada, a exibir_pedidos(), onde... o nome é autoexplanatório
def exibir_pedidos():

    #Uma repetição for in. Para cada item em registros, ele imprimira uma mensagem que evidenciará o email do cliente, o produto que ele comprou, o valor da compra, e o estado onde foi realizada a compra
    for registro in registros:
        print("Cliente:", registro[0], "|Produto:", registro[1], "|Valor: R$", registro[2], "|Estado:", registro[3])

#É criada a função que futuramente poderá ser chamada, a exibir_analises_financeiras(), onde o sistema fará cálculos e exibirá infomações que serão importantes na análise dos dados
def exibir_analises_financeiras():

    #Análises mais simples, feitas: 
    #   1º - lendo a quantidades de itens na lista, com len(), para retornar o total de pedidos;
    #   2º - somando os itens numéricos na lista, e retornando o faturamento total;
    #   3º - calculando a média e verificando qual o menor e maior preço, com auxílio da min() e max(), para pegar o menor e maior valor numérico da lista e os dividindo 
    #por 2;
    print("\nAnálises dos pedidos cadastrados:")
    print("\nTotal de pedidos:", len(registros), "Pedidos")
    print("Faturamento total: R$", sum(precos))
    preco_medio = (min(precos)+max(precos))/2
    print("Ticket médio: R$", preco_medio)
    print("Maior venda: R$", max(precos))
    print("Menor venda: R$", min(precos))

    #Análises mais complexas:
    print("\nAnálises adicionais:")

    #Listas para armazenar o campo referente aos produtos e para armazenar os produtos mais vendidos
    produtos = []
    produtos_mais_vendidos = []

    #Repetição for in, para percorrer a lista de registros e adicionar o campo referente aos produtos na lista produtos.
    for registro in registros:
        produtos.append(registro[1])

    #Criada uma variável que crescerá até atingir uma quantidade máxima, ao pecorrer uma lista com for in ele cria outra variável que crescerá com a quanidade de vezes que um item aparece na lista de produtos com ajuda do .count(), depois, se a variável que cresceu dentro da repetição for maior que a de fora, a 'quantidade_máxima' recebe a 'quantidade'
    quantidade_maxima = 0
    for produto in produtos:
        quantidade = produtos.count(produto)
        if quantidade > quantidade_maxima:
            quantidade_maxima = quantidade
    print("\nMáximo de vendas por produto: ", quantidade_maxima, "vendas")

    #Agora, tanto para mostrar o item que mais vendeu, quanto para caso tenham itens empatados, vamos usar um for in. Se a quantidade de itens, da repetição anterior, for igual a quantidade daquele item na lista, e se o item não estiver na lista de itens mais vendidos, ele vai adicionar à lista e vai mandar uma mensagem com o nome o produto e a quantidade de vendas com o qual empatou.
    for produto in produtos:
        if quantidade == produtos.count(produto):
            if produto not in produtos_mais_vendidos:
                produtos_mais_vendidos.append(produto)
                print("Produto:", produto.capitalize(), "|Quantidade de vendas:", produtos.count(produto))

    #Listas para armazenar o campo referente aos emails e para armazenar os emails que mais compraram
    emails = []
    emails_mais_compradores = []

    #Repetição for in, para percorrer a lista de registros e adicionar o campo referente aos emails na lista emails.
    for registro in registros:
        emails.append(registro[0])

    #Criada uma variável que crescerá até atingir uma quantidade máxima, ao pecorrer uma lista com for in ele cria outra variável que crescerá com a quanidade de vezes que um item aparece na lista de produtos com ajuda do .count(), depois, se a variável que cresceu dentro da repetição for maior que a de fora, a 'quantidade_maxima' recebe a 'quantidade' (PS: quantidade_maxima precisa ser zerado de novo, se não, ele continua com o valor anterior)
    quantidade_maxima = 0
    for email in emails:
        quantidade = emails.count(email)
        if quantidade > quantidade_maxima:
            quantidade_maxima = quantidade
    print("\nMáxima de compras por cliente: ", quantidade_maxima, "compras")

    #Agora, tanto para mostrar o email que mais comprou, quanto para caso tenham emails empatados, vamos usar um for in. Se a quantidade de itens, da repetição anterior, for igual a quantidade daquele item na lista, e se o item não estiver na lista de emails que mais compraram, ele vai adicionar à lista e vai mandar uma mensagem com o email e a quantidade de compras com o qual empatou.
    for email in emails:
        if quantidade == emails.count(email):
            if email not in emails_mais_compradores:
                emails_mais_compradores.append(email)
                print("Email:", email, "|Quantidade de compras:", emails.count(email))

    #Listas para armazenar o campo referente aos estados e para armazenar os estados que mais compraram
    estados = []
    estados_mais_compras = []

    #Repetição for in, para percorrer a lista de registros e adicionar o campo referente aos estados na lista estados.
    for registro in registros:
        estados.append(registro[3])

    #Criada uma variável que crescerá até atingir uma quantidade máxima, ao pecorrer uma lista com for in ele cria outra variável que crescerá com a quanidade de vezes que um item aparece na lista de produtos com ajuda do .count(), depois, se a variável que cresceu dentro da repetição for maior que a de fora, a 'quantidade_máxima' recebe a 'quantidade' (PS: quantidade_maxima precisa ser zerado de novo, se não, ele continua com o valor anterior)
    quantidade_maxima = 0
    for estado in estados:
        quantidade = estados.count(estado)
        if quantidade > quantidade_maxima:
            quantidade_maxima = quantidade
    print("\nMáximo de vendas por estado: ", quantidade_maxima, "vendas")

    #Agora, tanto para mostrar o estado que teve mais compras, quanto para caso tenham estados empatados, vamos usar um for in. Se a quantidade de itens, da repetição anterior, for igual a quantidade daquele item na lista, e se o item não estiver na lista de estados que tiveram mais compras, ele vai adicionar à lista e vai mandar uma mensagem com o estado e a quantidade de compras com o qual empatou.
    for estado in estados:
        if quantidade == estados.count(estado):
            if estado not in estados_mais_compras:
                estados_mais_compras.append(estado)
                print("Estado:", estado, "|Quantidade de vendas:", estados.count(estado))

    #Criada uma lista que contém os preços dos produtos de formas ordenadas, graças ao sorted()
    precos_ordenados = sorted(precos)
    print("\nPreços dos pedidos em ordem crescente:")

    #Repetição simples
    for preco in precos_ordenados:
        print("R$", preco)

#Criada a função buscar_pedidos()
def buscar_pedidos():

    #Repetição que só acaba caso teha aluma opção que tenha 'break'
    while True:

        #Variável que recebe um valor string
        op = input("\nDeseja ver os pedidos por:\n1 - Email\n2 - Produto\n3 - Estado\n4 - Sair\nEscolha uma opção: ").strip()

        #Match case, perfeito para fazer menus. Match seria algo como comparar, encontrar, checar. E case, aqui, é algo como caso, ou seja, caso a variável sejá algo 
        match op:

            #1º caso - variável email_busca recebe a string que o cliente deseja buscar, e enquanto isso a variável encontrado recebe falso. Agora, com uma repetição, pois pode se encontrar mais de um item no sistema, se o item da lista for igual ao que o cliente botou, então ele mostrará o que encontrou e encontrado recebe true. Se não, mostra mensagem negativa.
            case "1":
                email_busca = input("\nDigite o cliente que deseja buscar: ").strip().lower()
                encontrado = False
                for registro in registros:
                    if registro[0] == email_busca:
                        print("Cliente:", registro[0], "|Produto:", registro[1], "|Valor: R$", registro[2], "|Estado:", registro[3])
                        encontrado = True
                if not encontrado:
                    print("Cliente não encontrado.")

            #2º caso - variável produto_busca recebe a string que o cliente deseja buscar, e enquanto isso a variável encontrado recebe falso. Agora, com uma repetição, pois pode se encontrar mais de um item no sistema, se o item da lista for igual ao que o cliente botou, então ele mostrará o que encontrou e encontrado recebe true. Se não, mostra mensagem negativa.
            case "2":
                produto_busca = input("\nDigite o produto que deseja buscar: ").strip().lower()
                encontrado = False
                for registro in registros:
                    if registro[1] == produto_busca:
                        print("Cliente:", registro[0], "|Produto:", registro[1], "|Valor: R$", registro[2], "|Estado:", registro[3])
                        encontrado = True
                if not encontrado:
                    print("Produto não encontrado.")

            #3º caso - variável estado_busca recebe a string que o cliente deseja buscar, e enquanto isso a variável encontrado recebe falso. Agora, com uma repetição, pois pode se encontrar mais de um item no sistema, se o item da lista for igual ao que o cliente botou, então ele mostrará o que encontrou e encontrado recebe true. Se não, mostra mensagem negativa.
            case "3":
                estado_busca = input("\nDigite o estado que deseja buscar: ").strip().upper()
                encontrado = False
                for registro in registros:
                    if registro[3] == estado_busca:
                        print("Cliente:", registro[0], "|Produto:", registro[1], "|Valor: R$", registro[2], "|Estado:", registro[3])
                        encontrado = True
                if not encontrado:
                    print("Estado não encontrado.")

            #4º caso - Imprime uma mensagem falando que vai sair desse mini-sistema e encerra com break
            case "4":
                print("Saindo...")
                break

            #5º caso - O '_', sem as aspas, é usado para indicar qualquer outra opção que não foi pré-estabelecida
            case _:
                print("⚠ Opção inválida.")

#Criada a função adicionar_pedido()
def adicionar_pedido():

    #Repetição simples para menu
    while True:

        #Escolha de opção do menu
        op = input("\nDeseja adicionar algum novo pedido?\n1 - Sim\n2 - Não\nEscolha uma opção: ").strip()
        match op:

            #Caso o usuário digite '1', ele pergunta os novos campos para adicionar um registro, limpa, filtra, trata erros do usuário digitando... desculpa, mas isso daqui só é chatinho de comentar, um monte de tratativa de erro. A única coisa que vale falar sobre é o novo_preco, que recebe uma string, se ele detectar que é um caractér abc, ele volta e depois ele é transformado em valor flutuante. Ao fim das respostas, ele faz um novo registro com as variáveis novas, adiciona ao fim dos registros com .append(), preço também.
            case "1":
                novo_email = input("\nDigite o email do cliente: ").strip().lower()
                if novo_email == "":
                    print("⚠ Email inválido. O email não pode ser vazio")
                    continue
                novo_produto = input("Digite o produto: ").strip().lower()
                if novo_produto == "":
                    print("⚠ Produto inválido. O produto não pode ser vazio")
                    continue
                novo_preco = input("Digite o preço: ").strip()
                if not novo_preco.replace('.', '').isdigit():
                    print("⚠ Preço inválido. O preço deve ser numérico")
                    continue
                novo_preco = float(novo_preco)
                if novo_preco <= 0:
                    print("⚠ Preço inválido. O preço não pode ser negativo ou zero")
                    continue
                novo_estado = input("Digite o estado (sigla, como: SP, RJ, MG, etc.): ").strip().upper()
                if novo_estado == "":
                    print("⚠ Estado inválido. O estado não pode ser vazio")
                    continue
                if len(novo_estado) != 2:
                    print("⚠ Estado inválido. O estado deve ter 2 caracteres")
                    continue
                novo_registro = [novo_email, novo_produto, novo_preco, novo_estado]
                registros.append(novo_registro)
                precos.append(novo_preco)
                print("\nNovo pedido adicionado com sucesso!")

            #Caso que encerra o mini-menu
            case "2":
                print("Saindo...")
                break

#Função principal, com menu e chama outras funções
def main():

    #Repetição que sustenta o menu
    while True:
        print("\n=======ANALISADOR DE PEDIDOS=======")

        #Variável que recebe opção
        op = input("\nEscolha uma opção:\n1 - Exibir pedidos\n2 - Exibir análises financeiras\n3 - Buscar pedidos\n4 - Adicionar pedido\n5 - Sair\nDigite o número da opção desejada: ").strip()

        #Match case que chama as opões digitadas pelo cliente.
        match op:

            #Chama a função exibir_pedidos()
            case "1":
                exibir_pedidos()

            #Chama a função exibir_analises_financeiras()
            case "2":
                exibir_analises_financeiras()

            #Chama a função buscar_pedidos()
            case "3":
                buscar_pedidos()

            #Chama a função adicionar_pedido()
            case "4":
                adicionar_pedido()

            #Sai do sistema, encerrando ele de vez
            case "5":
                print("Saindo...")
                break

            #Tratativa de erro, caso ele digite qualquer outra coisa
            case _:
                print("⚠ Opção inválida.")

#Chama a função que fundamenta esse sistema
main()