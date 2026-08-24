#Vamos criar uma lista
produtos = []

#Criamos a lista ids para mais tarde
ids = []

#Vamos fazer o CRUD
#Começando pelo CREATE, vamos fazer uma função
def cadastrar_produto():
    while True:
        print("\n======CADASTRO======")

        #Criamos a variável id, que tenta receber um número inteiro definido pelo usuário. Se ele não for um número inteiro, e se ele for vazio, eles exibem mensagem de erro. Ao mesmo tempo, se o id estiver na lista de ids, ele mostra uma mensagem de erro e mostra os ids já registrados
        try:
            id = int(input("Digite o número de identificação do produto que deseja cadastrar:\n-> ").strip())
            if id in ids:
                print("------------------------------")
                print(f"⚠️ ID não pode ser repetido: {ids} ⚠️")
                continue
        except ValueError:
                print("------------------------------")
                print("⚠️ ID tem que ser um valor numérico inteiro ⚠️")
                continue

        #Criamos a variável nome, que recebe uma String definida pelo usuário que terá seus espaços vazios retirados e tudo em minúsculo, por conta do .strip() e .lower(). Se ele for vazio, retorna mesagem de erro
        nome = input("Digite o nome do produto que deseja cadastrar:\n-> ").strip().lower()
        if nome == "":
            print("------------------------------")
            print("⚠️ Nome não pode ser vazio ⚠️")
            continue
        
        #Criamos a variável categoria, que recebe uma String definida pelo usuário que terá seus espaços vazios retirados e tudo em minúsculo, por conta do .strip() e .lower(). Se ele for vazio, retorna mesagem de erro
        categoria = input("Digite a categoria do produto que deseja cadastrar:\n-> ").strip().lower()
        if categoria == "":
            print("------------------------------")
            print("⚠️ Categoria não pode ser vazio ⚠️")
            continue

        #Criamos a variável preco, que recebe uma float (Pode se digitar esse valor com ',' ao invés de '.') e se ele for menor ou igual a zero, ele vai exibir uma mensagem de erro. E se ele receber um texto decorrido, ele vai dar uma mensagem de erro
        try:
            preco = float(input("Digite o preço do produto que deseja cadastrar:\n-> ").strip().replace(",", "."))
            if preco <= 0:
                print("------------------------------")
                print("⚠️ Preço inválido. Ele não pode ser menor ou igual a 0 ⚠️")
                continue
        except ValueError:
            print("------------------------------")
            print("⚠️ Preço inválido. O preço deve ser numérico ⚠️")
            continue

        #Criamos a variável estoque, que tenta receber um número inteiro definido pelo usuário. Se ele não for um número inteiro, e se ele for vazio, eles exibem mensagem de erro. Caso ele seja menos que zero, ele também exibe uma mensagem de erro
        try:
            estoque = int(input("Digite o estoque do produto que deseja cadastrar:\n-> ").strip())
            if estoque < 0:
                print("------------------------------")
                print("⚠️ Estoque inválido. Ele não pode ser menor que 0 ⚠️")
                continue
        except ValueError:
            print("------------------------------")
            print("⚠️ Estoque tem que ser um valor numérico inteiro ⚠️")
            continue

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
        break
    
#A seguir, vamos fazer o READ
def listar_produtos():
    print("\n========== PRODUTOS ==========")

    # Antes de percorrer a lista, verificamos se ela está vazia.
    # len() retorna a quantidade de elementos.
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
        #Para cada item na lista produtos, ele vai buscar os itens com as mesmas chaves dentro dos colchetes e vai mostrar seu valor, sendo perfeito para listar
        for produto in produtos:
            print(f"ID: {produto["id"]}|Nome: {produto["nome"]}|Categoria: {produto["categoria"]}|Preço: R${produto["preço"]:.2f}|Estoque: {produto["estoque"]} unidade(s)")

def buscar_produto():
    print("\n========== BUSCA ==========")
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
        try:
            # Solicita o produto que será pesquisado por ID.
            produto_busca = int(input("Digite o ID do produto que deseja buscar:\n-> ").strip().replace("-",""))
            if produto_busca not in ids:
                print("------------------------------")
                print(f"⚠️ ID inválido, tente um desses: {ids} ⚠️")
                return
            for produto in produtos:
                if produto_busca == produto["id"]:
                    print("------------------------------")
                    print("✅ Produto encontrado, exibindo: ✅")
                    print("------------------------------")
                    print(f"Nome: {produto["nome"]}|Categoria: {produto["categoria"]}|Preço: R${produto["preço"]:.2f}|Estoque: {produto["estoque"]} unidade(s)")
        except ValueError:
            print("------------------------------")
            print("⚠️ ID inválido, use um valor numérico ⚠️")

#Agora, vamos fazer o Update, Atualiza um produto existente.
def alterar_produto():
    print("\n========== ATUALIZAÇÃO ==========")
    # Solicita o produto que será alterado.
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
        try:
            # Solicita o produto que será pesquisado por ID.
            produto_att = int(input("Digite o ID do produto que deseja atualizar:\n-> ").strip().replace("-",""))
            if produto_att not in ids:
                print("------------------------------")
                print(f"⚠️ ID inválido, tente um desses: {ids} ⚠️")
                return
            for i, produto in enumerate(produtos):
                if produto_att == produto["id"]:
                        while True:
                            nome = input("Digite o novo nome do produto:\n-> ").strip().lower()
                            if nome == "":
                                print("------------------------------")
                                print("⚠️ Nome não pode ser vazio ⚠️")
                                continue
                            
                            categoria = input("Digite a nova categoria do produto:\n-> ").strip().lower()
                            if categoria == "":
                                print("------------------------------")
                                print("⚠️ Categoria não pode ser vazio ⚠️")
                                continue

                            try:
                                preco = float(input("Digite o novo preço do produto:\n-> ").strip().replace(",", "."))
                                if preco <= 0:
                                    print("------------------------------")
                                    print("⚠️ Preço inválido. Ele não pode ser menor ou igual a 0 ⚠️")
                                    continue
                            except ValueError:
                                print("------------------------------")
                                print("⚠️ Preço inválido. O preço deve ser numérico ⚠️")
                                continue

                            try:
                                estoque = int(input("Digite o novo estoque do produto:\n-> ").strip())
                                if estoque < 0:
                                    print("------------------------------")
                                    print("⚠️ Estoque inválido. Ele não pode ser menor que 0 ⚠️")
                                    continue
                            except ValueError:
                                print("------------------------------")
                                print("⚠️ Estoque tem que ser um valor numérico inteiro ⚠️")
                                continue

                            novo_produto = {
                                "id": produto_att,
                                "nome": nome,
                                "categoria": categoria,
                                "preço": preco,
                                "estoque": estoque
                            }

                            produtos[i] = novo_produto

                            print("------------------------------")
                            print("✅ Produto atualizado! ✅")
                            break
        except ValueError:
            print("------------------------------")
            print("⚠️ ID inválido, use um valor numérico ⚠️")

def deletar_produto():
    print("\n========== EXCLUSÃO ==========")
    # Solicita o produto que será excluído.
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
        try:
            produto_excluir = int(input("Digite o ID do produto que deseja excluir:\n-> ").strip())
            # Verificamos se o produto existe.
            if produto_excluir not in ids:
                print("------------------------------")
                print(f"⚠️ ID inválido, tente um desses: {ids} ⚠️")
                return
            for produto in produtos:
                if produto_excluir == produto["id"]:
                    # remove() procura o elemento e o exclui, da lista.
                    produtos.remove(produto)
                    print("✅ Produto excluído com sucesso! ✅")
        except ValueError:
            print("------------------------------")
            print("⚠️ ID inválido, use um valor numérico ⚠️")


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
        op = input("Digite uma opção numérica do menu:\n-> ").strip()
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