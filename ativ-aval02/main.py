#Vamos criar uma lista
produtos = []

#Criamos a lista ids para mais tarde
ids = []

#Vamos fazer o CRUD
#Começando pelo CREATE, vamos fazer uma função
def cadastrar_produto():
    print("\n======CADASTRO======")

    #Criamos a variável id, que recebe um número inteiro definido pelo usuário. Se ele não for um número inteiro, e se ele for vazio, eles exibem mensagem de erro
    id = int(input("Digite o número de identificação o produto que deseja cadastrar: ").strip())
    if id in ids:
        print("------------------------------")
        print(f"⚠️ ID não pode ser repetido: {ids} ⚠️")
        print("------------------------------")
        return

    #Criamos a variável nome, que recebe uma String definida pelo usuário que terá seus espaços vazios retirados e tudo em minúsculo, por conta do .strip() e .lower(). Se ele for vazio, retorna mesagem de erro
    nome = input("Digite o nome do produto que deseja cadastrar: ").strip().lower()
    if nome == "":
        print("------------------------------")
        print("⚠️ Nome não pode ser vazio ⚠️")
        print("------------------------------")
        return
    
    #Criamos a variável categoria, que recebe uma String definida pelo usuário que terá seus espaços vazios retirados e tudo em minúsculo, por conta do .strip() e .lower(). Se ele for vazio, retorna mesagem de erro
    categoria = input("Digite a categoria do produto que deseja cadastrar: ").strip().lower()
    if categoria == "":
        print("------------------------------")
        print("⚠️ Categoria não pode ser vazio ⚠️")
        print("------------------------------")
        return

    #Criamos a variável preco, que recebe uma String d
    preco = input("Digite o preço do produto que deseja cadastrar: ").strip().replace(",", ".")
    if preco == "":
        print("------------------------------")
        print("⚠️ Preço não pode ser vazio ⚠️")
        print("------------------------------")
        return
    elif not preco.replace('.', '').isdigit():
        print("------------------------------")
        print("⚠️ Preço inválido. O preço deve ser numérico ⚠️")
        print("------------------------------")
        return
    preco = float(preco)
    if preco <= 0:
        print("------------------------------")
        print("⚠️ Preço inválido. Ele não pode ser menor ou igual a 0 ⚠️")
        print("------------------------------")
        return
    estoque = int(input("Digite o estoque do produto que deseja cadastrar: ").strip())
    novo_produto = {
        "id": id,
        "nome": nome,
        "categoria": categoria,
        "preço": preco,
        "estoque": estoque
    }
    produtos.append(novo_produto)
    ids.append(id)
    print("------------------------------")
    print("✅ Produto cadastrado! ✅")
    
#A seguir, vamos fazer o READ
def listar_produtos():
    print("\n========== PRODUTOS ==========")
    # Antes de percorrer a lista, verificamos se ela está vazia.
    # len() retorna a quantidade de elementos.
    
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
    # enumerate() permite obter:
    # indice -> posição do elemento
    # produto -> valor armazenado
    
        for indice, produto in enumerate(produtos):
            print(indice,"-",produto)

def buscar_produto():
    print("\n========== BUSCA ==========")
    # Solicita o produto que será pesquisado.
    produto_busca = input("Digite o produto que deseja buscar: ").strip()
        # O operador "in" verifica se o produto existe dentro da lista.
    if produto_busca in produtos:
        # index() retorna a posição do elemento
        # dentro da lista.
        indice = produtos.index(produto_busca)
        print("Produto encontrado!")
    
        print("Produto:",produto_busca)
    
        print("Posição:",indice)

    else:
        print("⚠️ Produto não encontrado. ⚠️")

#Agora, vamos fazer o Update, Atualiza um produto existente.
def alterar_produto():
    print("\n========== ATUALIZAÇÃO ==========")
    # Solicita o produto que será alterado.
    
    produto_atual = input("Digite o produto que deseja alterar: ").strip()
    
    # Primeiro verificamos se o produto existe.
    
    if produto_atual in produtos:
    # Descobrimos a posição do produto.
    
        indice = produtos.index(produto_atual)
        # Solicita o novo nome.
        
        novo_produto = input("Digite o novo nome do produto: ").strip()
        # Verifica se o novo nome foi informado.
        
        if novo_produto == "":
    
            print("⚠️ Erro: o novo nome não pode ser vazio. ⚠️")
        else:
        # Utilizamos o índice para substituir o valor existente.
        # Antes:
        # produtos[1] = "Mouse"
        # Depois:
        # produtos[1] = "Mouse sem fio"
    
            produtos[indice] = novo_produto
            print("✅ Produto atualizado com sucesso! ✅")
        
    else:   
        print("⚠️ Produto não encontrado. ⚠️")

def deletar_produto():
    print("\n========== EXCLUSÃO ==========")
    # Solicita o produto que será excluído.
    
    produto_excluir = input("Digite o produto que deseja excluir: ").strip()
    # Verificamos se o produto existe.
    
    if produto_excluir in produtos:
    
        # remove() procura o elemento e o exclui, da lista.
    
        produtos.remove(produto_excluir)
    
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")


#Vamos fazer a função que vai fazer o menu
def menu():
    while True:
        print("\n======MENU======")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Consultar produto")
        print("4 - Alterar produto")
        print("5 - Excluir produto")
        print("6 - Sair")
        print("------------------------------")
        op = input("Digite uma opção numérica do menu: ").strip()
        match (op):
            case "1":
                cadastrar_produto()

            case "2":
                listar_produtos()

            case "3":
                buscar_produto()

            case "4":
                alterar_produto()

            case "5":
                deletar_produto()

            case "6":
                print("------------------------------")
                print("👋 Até uma próxima!")
                print("Encerrando sistema...")
                break

            case _:
                print("------------------------------")
                print("⚠️ Opção inválida! ⚠️")
                print("Tente digitar uma opção equivalente ao número do menu")

menu()