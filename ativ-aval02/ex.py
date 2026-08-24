# ============================================================
# CRUD DE PRODUTOS UTILIZANDO LISTA
# ============================================================
#
# CRUD representa quatro operações básicas:
#
# C = Create  -> Criar / Cadastrar
# R = Read    -> Ler / Consultar
# U = Update  -> Atualizar / Alterar
# D = Delete  -> Excluir
#
# Neste exemplo, vamos utilizar uma LISTA para armazenar
# os produtos cadastrados.
#
# ============================================================


# ============================================================
# LISTA PRINCIPAL
# ============================================================

# Criamos uma lista vazia.
#
# Ela será utilizada para armazenar todos os produtos
# cadastrados durante a execução do programa.

produtos = []


# ============================================================
# MENU PRINCIPAL
# ============================================================

# O while True mantém o programa funcionando continuamente.
#
# O programa somente será encerrado quando o usuário escolher
# a opção 6.

while True:

    # --------------------------------------------------------
    # EXIBIÇÃO DO MENU
    # --------------------------------------------------------

    print("\n========================================")
    print("          CRUD DE PRODUTOS")
    print("========================================")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("6 - Sair")

    print("========================================")


    # --------------------------------------------------------
    # LEITURA DA OPÇÃO
    # --------------------------------------------------------

    # O usuário informa uma opção.
    #
    # Utilizamos int() porque queremos trabalhar
    # com números inteiros.

    try:

        opcao = int(
            input("Escolha uma opção: ")
        )


        # ====================================================
        # CREATE
        # ====================================================
        #
        # Cadastrar um novo produto.
        #
        # Utilizamos append() para adicionar o produto
        # ao final da lista.
        #

        if opcao == 1:

            print("\n========== CADASTRO ==========")


            # Solicita o nome do produto.

            produto = input(
                "Digite o nome do produto: "
            ).strip()


            # Verifica se o usuário deixou o campo vazio.

            if produto == "":

                print(
                    "Erro: o nome do produto "
                    "não pode ser vazio."
                )


            else:

                # append() adiciona um novo elemento
                # ao final da lista.

                produtos.append(produto)


                print(
                    "Produto cadastrado com sucesso!"
                )


        # ====================================================
        # READ
        # ====================================================
        #
        # Exibe todos os produtos cadastrados.
        #

        elif opcao == 2:

            print("\n========== PRODUTOS ==========")


            # Antes de percorrer a lista, verificamos
            # se ela está vazia.
            #
            # len() retorna a quantidade de elementos.

            if len(produtos) == 0:

                print(
                    "Nenhum produto cadastrado."
                )


            else:

                # enumerate() permite obter:
                #
                # indice -> posição do elemento
                # produto -> valor armazenado
                #
                # Exemplo:
                #
                # 0 - Notebook
                # 1 - Mouse
                # 2 - Teclado

                for indice, produto in enumerate(produtos):

                    print(
                        indice,
                        "-",
                        produto
                    )


        # ====================================================
        # READ / BUSCA
        # ====================================================
        #
        # Procura um determinado produto na lista.
        #

        elif opcao == 3:

            print("\n========== BUSCA ==========")


            # Solicita o produto que será pesquisado.

            produto_busca = input(
                "Digite o produto que deseja buscar: "
            ).strip()


            # O operador "in" verifica se o produto
            # existe dentro da lista.

            if produto_busca in produtos:

                # index() retorna a posição do elemento
                # dentro da lista.

                indice = produtos.index(
                    produto_busca
                )


                print(
                    "Produto encontrado!"
                )

                print(
                    "Produto:",
                    produto_busca
                )

                print(
                    "Posição:",
                    indice
                )


            else:

                print(
                    "Produto não encontrado."
                )


        # ====================================================
        # UPDATE
        # ====================================================
        #
        #  
        #

        elif opcao == 4:

            print("\n========== ATUALIZAÇÃO ==========")


            # Solicita o produto que será alterado.

            produto_atual = input(
                "Digite o produto que deseja alterar: "
            ).strip()


            # Primeiro verificamos se o produto existe.

            if produto_atual in produtos:

                # Descobrimos a posição do produto.

                indice = produtos.index(
                    produto_atual
                )


                # Solicita o novo nome.

                novo_produto = input(
                    "Digite o novo nome do produto: "
                ).strip()


                # Verifica se o novo nome foi informado.

                if novo_produto == "":

                    print(
                        "Erro: o novo nome "
                        "não pode ser vazio."
                    )


                else:

                    # Utilizamos o índice para substituir
                    # o valor existente.
                    #
                    # Antes:
                    #
                    # produtos[1] = "Mouse"
                    #
                    # Depois:
                    #
                    # produtos[1] = "Mouse sem fio"

                    produtos[indice] = novo_produto


                    print(
                        "Produto atualizado com sucesso!"
                    )


            else:

                print(
                    "Produto não encontrado."
                )


        # ====================================================
        # DELETE
        # ====================================================
        #
        # Exclui um produto existente.
        #

        elif opcao == 5:

            print("\n========== EXCLUSÃO ==========")


            # Solicita o produto que será excluído.

            produto_excluir = input(
                "Digite o produto que deseja excluir: "
            ).strip()


            # Verificamos se o produto existe.

            if produto_excluir in produtos:

                # remove() procura o elemento e o exclui
                # da lista.

                produtos.remove(
                    produto_excluir
                )


                print(
                    "Produto excluído com sucesso!"
                )


            else:

                print(
                    "Produto não encontrado."
                )


        # ====================================================
        # SAIR
        # ====================================================

        elif opcao == 6:

            print(
                "\nPrograma encerrado."
            )


            # break interrompe o while True
            # e encerra o programa.

            break


        # ====================================================
        # OPÇÃO INVÁLIDA
        # ====================================================

        else:

            print(
                "Opção inválida!"
            )

            print(
                "Escolha uma opção de 1 a 6."
            )


    # ========================================================
    # TRATAMENTO DE ERROS
    # ========================================================

    # Caso o usuário digite algo que não seja um número,
    # por exemplo:
    #
    # abc
    #
    # a função int() provocará um ValueError.
    #
    # O except captura esse erro e evita que o programa
    # seja encerrado.

    except ValueError:

        print(
            "\nErro: digite apenas números "
            "de 1 a 6."
        )


