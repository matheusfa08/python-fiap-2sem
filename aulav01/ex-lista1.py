produtos = []
estoque = []

def cadastrar_produto():
    print("===============\nQuantos produtos serão cadastrados?")
    x = int(input("Digite a quantidade: "))
    while x != 0: 
        produto = input("===============\nQual o nome do produto?\nDigite aqui: ").strip().lower()
        qntd = int(input("===============\nQual a quantidade no estoque? \nDigite aqui: "))
        produtos.append(produto)
        estoque.append(qntd)
        x = x - 1

def mostar_produto():
    if not produtos:
        print("===============\nNão há produtos cadastrados")

    else:
        print("=====LISTA DE PRODUTOS=====")
        for y in range(len(produtos)):
            produto = produtos[y]
            qntd = estoque[y]
            print(f"{produto}" + "........" + f"{qntd} unidade(s)")

def encontrar_produto():
    termo = input("===============\nDigite o produto para buscar: ").strip().lower()
 
    encontrado = False
 
    for y in range(len(produtos)):
        if termo in produtos[y]:
            print(f"✔ Encontrado: {produtos[y]} - {estoque[y]} unidade(s)")
            encontrado = True
 
    if not encontrado:
        print("===============\n❌ Produto não encontrado.")

def baixo_estocar():
    if not produtos:
        print("Não há produtos cadastrados")
        return

    encontrado = False

    print("=====PRODUTOS C/ ESTOQUE BAIXO=====")
    for y in range(len(estoque)):
        if (estoque[y] < 10):
            print(f"{produtos[y]} - {estoque[y]} unidade(s)")
            encontrado = True

    if not encontrado:
        print("===============\n✔ Nenhum produto com estoque baixo.")

def maior_estoque():
    if not produtos:
        print("Não há produtos cadastrados")
        return

    qntd = -1
    indice = -1

    print("=====PRODUTO C/ MAIOR ESTOQUE=====")
    for y in range(len(estoque)):
        if estoque[y] > qntd:
            qntd = estoque[y]
            indice = y

    print(f"{produtos[indice]} - {estoque[indice]} unidade(s)")

def atualizar_estoque():
    if not produtos:
        print("Não há produtos cadastrados")
        return

    termo = input("===============\nDigite o nome do produto para atualizar: ").strip().lower()

    encontrado = False

    for y in range(len(produtos)):
        if termo == produtos[y]:
            print(f"===============\nProduto encontrado: {produtos[y]} - {estoque[y]} unidade(s)")
            nova_qntd = int(input("Digite a nova quantidade em estoque: "))
            estoque[y] = nova_qntd
            print(f"===============\n✔ Estoque atualizado: {produtos[y]} - {estoque[y]} unidade(s)")
            encontrado = True
            break

    if not encontrado:
        print("❌ Produto não encontrado.")

def menu():
    while True:
        print("=====MENU=====")
        print("1 - Cadastrar produto")
        print("2 - Mostrar produtos cadastrados")
        print("3 - Consultar produto")
        print("4 - Consultar baixo estoque")
        print("5 - Consultar maior estoque")
        print("6 - Atualizar estoque")
        print("7 - Sair")

        op = input("Digite uma opção: ")

        match op:
            case "1":
                cadastrar_produto()
            case "2":
                mostar_produto()
            case "3":
                encontrar_produto()
            case "4":
                baixo_estocar()
            case "5":
                maior_estoque()
            case "6":
                atualizar_estoque()
            case "7":
                print("Encerrando sistema...")
                break
            case _:
                print("⚠ Opção inválida!")

menu()