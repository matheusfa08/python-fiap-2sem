#Vamos criar uma lista
#Lista principal que armazena todos os produtos cadastrados no sistema.
#Cada elemento dessa lista será um dicionário representando um produto.
produtos = []

#Criamos a lista ids para mais tarde
#Lista auxiliar que guarda apenas os IDs já cadastrados.
#Ela existe para facilitar a verificação de duplicidade (in ids),
#sem precisar percorrer o dicionário completo toda vez.
ids = []

#Vamos fazer o CRUD
#Começando pelo CREATE, vamos fazer uma função
#Função responsável pelo CADASTRO (CREATE) de um novo produto.
#Fica em loop até que o usuário informe todos os dados corretamente
#e o produto seja cadastrado com sucesso (break no final).
def cadastrar_produto():
    while True:
        print("\n======CADASTRO======")

        #Criamos a variável id, que tenta receber um número inteiro definido pelo usuário. Se ele não for um número inteiro, e se ele for vazio, eles exibem mensagem de erro. Ao mesmo tempo, se o id estiver na lista de ids, ele mostra uma mensagem de erro e mostra os ids já registrados
        #try/except captura o erro caso o usuário digite algo que não seja um número inteiro (ValueError).
        try:
            id = int(input("Digite o número de identificação do produto que deseja cadastrar:\n-> ").strip())
            #Verifica se o ID já existe na lista de ids (regra de negócio: não pode haver ID duplicado).
            #Se existir, avisa o usuário, mostra os ids já usados e volta para o início do loop (continue).
            if id in ids:
                print("------------------------------")
                print(f"⚠️ ID não pode ser repetido: {ids} ⚠️")
                continue
        except ValueError:
                #Caso a conversão para int falhe (texto vazio ou não numérico), exibe erro e reinicia o loop.
                print("------------------------------")
                print("⚠️ ID tem que ser um valor numérico inteiro ⚠️")
                continue

        #Criamos a variável nome, que recebe uma String definida pelo usuário que terá seus espaços vazios retirados e tudo em minúsculo, por conta do .strip() e .lower(). Se ele for vazio, retorna mesagem de erro
        #.strip() remove espaços em branco extras no início/fim; .lower() padroniza para minúsculo.
        nome = input("Digite o nome do produto que deseja cadastrar:\n-> ").strip().lower()
        #Valida se o nome não ficou vazio após o strip.
        if nome == "":
            print("------------------------------")
            print("⚠️ Nome não pode ser vazio ⚠️")
            continue
        
        #Criamos a variável categoria, que recebe uma String definida pelo usuário que terá seus espaços vazios retirados e tudo em minúsculo, por conta do .strip() e .lower(). Se ele for vazio, retorna mesagem de erro
        #Mesma lógica de padronização e validação aplicada ao nome.
        categoria = input("Digite a categoria do produto que deseja cadastrar:\n-> ").strip().lower()
        #Valida se a categoria não ficou vazia.
        if categoria == "":
            print("------------------------------")
            print("⚠️ Categoria não pode ser vazio ⚠️")
            continue

        #Criamos a variável preco, que recebe uma float (Pode se digitar esse valor com ',' ao invés de '.') e se ele for menor ou igual a zero, ele vai exibir uma mensagem de erro. E se ele receber um texto decorrido, ele vai dar uma mensagem de erro
        #.replace(",", ".") permite que o usuário digite o preço no formato brasileiro (vírgula) e converte para o formato aceito pelo float().
        try:
            preco = float(input("Digite o preço do produto que deseja cadastrar:\n-> ").strip().replace(",", "."))
            #Regra de negócio: preço deve ser maior que zero.
            if preco <= 0:
                print("------------------------------")
                print("⚠️ Preço inválido. Ele não pode ser menor ou igual a 0 ⚠️")
                continue
        except ValueError:
            #Caso o valor digitado não possa ser convertido para float, exibe erro.
            print("------------------------------")
            print("⚠️ Preço inválido. O preço deve ser numérico ⚠️")
            continue

        #Criamos a variável estoque, que tenta receber um número inteiro definido pelo usuário. Se ele não for um número inteiro, e se ele for vazio, eles exibem mensagem de erro. Caso ele seja menos que zero, ele também exibe uma mensagem de erro
        #Mesma lógica de tratamento usada no ID, mas aqui aceitando o valor zero (estoque pode ser 0, só não pode ser negativo).
        try:
            estoque = int(input("Digite o estoque do produto que deseja cadastrar:\n-> ").strip())
            #Regra de negócio: estoque não pode ser negativo.
            if estoque < 0:
                print("------------------------------")
                print("⚠️ Estoque inválido. Ele não pode ser menor que 0 ⚠️")
                continue
        except ValueError:
            #Caso o valor digitado não possa ser convertido para int, exibe erro.
            print("------------------------------")
            print("⚠️ Estoque tem que ser um valor numérico inteiro ⚠️")
            continue

        #Monta o dicionário que representa o novo produto, com todas as informações coletadas acima.
        novo_produto = {
            "id": id,
            "nome": nome,
            "categoria": categoria,
            "preço": preco,
            "estoque": estoque
        }

        #Adiciona o novo produto na lista principal de produtos.
        produtos.append(novo_produto)
        #Adiciona o ID na lista auxiliar de ids, para futuras validações de duplicidade.
        ids.append(id)
        print("------------------------------")
        print("✅ Produto cadastrado! ✅")
        #Encerra o loop de cadastro, pois o produto foi cadastrado com sucesso.
        break
    
#A seguir, vamos fazer o READ
#Função responsável por LISTAR (READ) todos os produtos cadastrados.
def listar_produtos():
    print("\n========== PRODUTOS ==========")

    # Antes de percorrer a lista, verificamos se ela está vazia.
    # len() retorna a quantidade de elementos.
    #Trata o caso de lista vazia, informando o usuário em vez de não mostrar nada.
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
        #Para cada item na lista produtos, ele vai buscar os itens com as mesmas chaves dentro dos colchetes e vai mostrar seu valor, sendo perfeito para listar
        #Percorre a lista de produtos (estrutura de repetição) e imprime todas as informações de cada um.
        #:.2f formata o preço com 2 casas decimais.
        for produto in produtos:
            print(f"ID: {produto["id"]}|Nome: {produto["nome"]}|Categoria: {produto["categoria"]}|Preço: R${produto["preço"]:.2f}|Estoque: {produto["estoque"]} unidade(s)")

#Função responsável por CONSULTAR (READ) um produto específico pelo ID.
def buscar_produto():
    print("\n========== BUSCA ==========")
    #Trata o caso de lista vazia antes mesmo de pedir o ID.
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
        try:
            # Solicita o produto que será pesquisado por ID.
            #.replace("-","") remove sinal de negativo, evitando erro de digitação com ID negativo.
            produto_busca = int(input("Digite o ID do produto que deseja buscar:\n-> ").strip().replace("-",""))
            #Verifica se o ID informado existe na lista de ids cadastrados.
            #Se não existir, avisa o usuário, mostra os ids disponíveis e sai da função (return).
            if produto_busca not in ids:
                print("------------------------------")
                print(f"⚠️ ID inválido, tente um desses: {ids} ⚠️")
                return
            #Percorre a lista de produtos até encontrar o produto com o ID buscado.
            for produto in produtos:
                if produto_busca == produto["id"]:
                    print("------------------------------")
                    print("✅ Produto encontrado, exibindo: ✅")
                    print("------------------------------")
                    #Exibe as informações do produto encontrado.
                    print(f"Nome: {produto["nome"]}|Categoria: {produto["categoria"]}|Preço: R${produto["preço"]:.2f}|Estoque: {produto["estoque"]} unidade(s)")
        except ValueError:
            #Caso o ID digitado não possa ser convertido para int, exibe erro.
            print("------------------------------")
            print("⚠️ ID inválido, use um valor numérico ⚠️")

#Agora, vamos fazer o Update, Atualiza um produto existente.
#Função responsável por ALTERAR (UPDATE) um produto já cadastrado.
def alterar_produto():
    print("\n========== ATUALIZAÇÃO ==========")
    # Solicita o produto que será alterado.
    #Trata o caso de lista vazia antes de pedir o ID.
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
        try:
            # Solicita o produto que será pesquisado por ID.
            produto_att = int(input("Digite o ID do produto que deseja atualizar:\n-> ").strip().replace("-",""))
            #Verifica se o ID informado existe. Se não existir, avisa e encerra a função.
            if produto_att not in ids:
                print("------------------------------")
                print(f"⚠️ ID inválido, tente um desses: {ids} ⚠️")
                return
            #enumerate() percorre a lista trazendo também o índice (i) de cada produto,
            #necessário para conseguir substituir o produto na posição correta da lista (produtos[i]).
            for i, produto in enumerate(produtos):
                if produto_att == produto["id"]:
                        #Loop interno que garante que o usuário informe dados válidos para
                        #nome, categoria, preço e estoque antes de concluir a atualização.
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

                            #Monta um novo dicionário com o ID original (produto_att) preservado
                            #e os demais dados atualizados, atendendo à regra de que o ID não pode ser alterado.
                            novo_produto = {
                                "id": produto_att,
                                "nome": nome,
                                "categoria": categoria,
                                "preço": preco,
                                "estoque": estoque
                            }

                            #Substitui o produto antigo pelo novo na mesma posição (índice i) da lista.
                            produtos[i] = novo_produto

                            print("------------------------------")
                            print("✅ Produto atualizado! ✅")
                            #Encerra o loop interno, pois a atualização foi concluída com sucesso.
                            break
        except ValueError:
            #Caso o ID digitado não possa ser convertido para int, exibe erro.
            print("------------------------------")
            print("⚠️ ID inválido, use um valor numérico ⚠️")

#Função responsável por EXCLUIR (DELETE) um produto cadastrado.
def deletar_produto():
    print("\n========== EXCLUSÃO ==========")
    # Solicita o produto que será excluído.
    #Trata o caso de lista vazia antes de pedir o ID.
    if len(produtos) == 0:
        print("⚠️ Nenhum produto cadastrado. ⚠️")
    else:
        try:
            produto_excluir = int(input("Digite o ID do produto que deseja excluir:\n-> ").strip())
            # Verificamos se o produto existe.
            #Se o ID não existir na lista de ids, avisa o usuário e encerra a função.
            if produto_excluir not in ids:
                print("------------------------------")
                print(f"⚠️ ID inválido, tente um desses: {ids} ⚠️")
                return
            #Percorre a lista de produtos procurando o produto com o ID informado.
            for produto in produtos:
                if produto_excluir == produto["id"]:
                    # remove() procura o elemento e o exclui, da lista.
                    #Remove o dicionário do produto da lista principal.
                    produtos.remove(produto)
                    print("✅ Produto excluído com sucesso! ✅")
        except ValueError:
            #Caso o ID digitado não possa ser convertido para int, exibe erro.
            print("------------------------------")
            print("⚠️ ID inválido, use um valor numérico ⚠️")


#Vamos fazer a função que vai fazer o menu
#Função principal do sistema: exibe o menu e direciona para cada operação do CRUD
#de acordo com a opção escolhida pelo usuário. Fica em loop até a opção "6 - Sair".
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
        #match/case funciona como um switch: compara o valor de "op" com cada "case"
        #e executa a função correspondente à opção escolhida.
        match (op):
            case "1":
                #Opção 1: chama a função de cadastro (CREATE).
                cadastrar_produto()

            case "2":
                #Opção 2: chama a função de listagem (READ - todos).
                listar_produtos()

            case "3":
                #Opção 3: chama a função de consulta (READ - por ID).
                buscar_produto()

            case "4":
                #Opção 4: chama a função de alteração (UPDATE).
                alterar_produto()

            case "5":
                #Opção 5: chama a função de exclusão (DELETE).
                deletar_produto()

            case "6":
                #Opção 6: encerra o programa, saindo do loop do menu (break).
                print("------------------------------")
                print("👋 Até uma próxima!")
                print("Encerrando sistema...")
                break

            case _:
                #case "_" funciona como o "default": trata qualquer opção
                #que não seja 1, 2, 3, 4, 5 ou 6, avisando que é inválida.
                print("------------------------------")
                print("⚠️ Opção inválida! ⚠️")
                print("Tente digitar uma opção equivalente ao número do menu")

#Chamada da função menu(), que inicia efetivamente a execução do programa.
menu()
