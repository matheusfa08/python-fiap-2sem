#Transformando o ex3 em um menu interativo.
dados = """ 
ana@gmail.com;Notebook;4500;SP 
carlos@gmail.com;Mouse;80;RJ 
ana@gmail.com;Teclado;250;SP 
maria@gmail.com;Monitor;1200;MG 
carlos@gmail.com;Headset;350;RJ 
joao@gmail.com;Notebook;4500;PR 
maria@gmail.com;Mouse;80;MG 
""" 

dado = dados.strip()
linhas = dado.splitlines()

registros = []
precos = []

for linha in linhas:
    campos = linha.split(";")
    email = campos[0].strip().lower()
    produto = campos[1].strip().lower()
    preco = float(campos[2].strip())
    estado = campos[3].strip()
    registro = [email, produto, preco, estado]
    registros.append(registro)
    precos.append(preco)

def exibir_pedidos():
    for registro in registros:
        print("\nCliente:", registro[0], "|Produto:", registro[1], "|Valor: R$", registro[2], "|Estado:", registro[3])

def exibir_analises_financeiras():
    print("\nAnálises dos pedidos cadastrados:")
    print("\nTotal de pedidos:", len(registros), "Pedidos")
    print("Faturamento total: R$", sum(precos))
    preco_medio = (min(precos)+max(precos))/2
    print("Ticket médio: R$", preco_medio)
    print("Maior venda: R$", max(precos))
    print("Menor venda: R$", min(precos))
    print("\nAnálises adicionais")
    produtos = []
    for registro in registros:
        produtos.append(registro[1])
    quantidade_maxima = 0
    for produto in produtos:
        quantidade = produtos.count(produto)
        if quantidade > quantidade_maxima:
            quantidade_maxima = quantidade
            produto_mais_vendido = produto
    produtos_mais_vendidos = []
    print("\nMáximo de vendas por produto: ", quantidade_maxima, "vendas")
    for produto in produtos:
        if quantidade == produtos.count(produto):
            if produto not in produtos_mais_vendidos:
                produtos_mais_vendidos.append(produto)
                print("Produto:", produto.capitalize(), "|Quantidade de vendas:", produtos.count(produto))
    emails = []
    for registro in registros:
        emails.append(registro[0])
    quantidade_maxima = 0
    for email in emails:
        quantidade = emails.count(email)
        if quantidade > quantidade_maxima:
            quantidade_maxima = quantidade
            email_que_mais_comprou = email
    print("\nMáxima de compras por cliente: ", quantidade_maxima, "compras")
    emails_mais_compradores = []
    for email in emails:
        if quantidade == emails.count(email):
            if email not in emails_mais_compradores:
                print("Email:", email, "|Quantidade de compras:", emails.count(email))
                emails_mais_compradores.append(email)
    estados = []
    for registro in registros:
        estados.append(registro[3])
    quantidade_maxima = 0
    for estado in estados:
        quantidade = estados.count(estado)
        if quantidade > quantidade_maxima:
            quantidade_maxima = quantidade
            estado_com_mais_vendas = estado
    print("\nMáximo de vendas por estado: ", quantidade_maxima, "vendas")
    estados_mais_vendidos = []
    for estado in estados:
        if quantidade == estados.count(estado):
            if estado not in estados_mais_vendidos:
                print("Estado:", estado, "|Quantidade de vendas:", estados.count(estado))
                estados_mais_vendidos.append(estado)
    precos_ordenados = sorted(precos)
    print("\nPreços dos pedidos em ordem crescente:")
    for preco in precos_ordenados:
        print("R$", preco)

def buscar_pedidos():
    while True:
        op = input("\nDeseja ver os pedidos por:\n1 - Email\n2 - Produto\n3 - Estado\n4 - Sair\nEscolha uma opção: ").strip()
        match op:
            case "1":
                email_busca = input("\nDigite o cliente que deseja buscar: ").strip().lower()
                encontrado = False
                for registro in registros:
                    if registro[0] == email_busca:
                        print("Cliente:", registro[0], "|Produto:", registro[1], "|Valor: R$", registro[2], "|Estado:", registro[3])
                        encontrado = True
                if not encontrado:
                    print("Cliente não encontrado.")
            case "2":
                produto_busca = input("\nDigite o produto que deseja buscar: ").strip().lower()
                encontrado = False
                for registro in registros:
                    if registro[1] == produto_busca:
                        print("Cliente:", registro[0], "|Produto:", registro[1], "|Valor: R$", registro[2], "|Estado:", registro[3])
                        encontrado = True
                if not encontrado:
                    print("Produto não encontrado.")
            case "3":
                estado_busca = input("\nDigite o estado que deseja buscar: ").strip().upper()
                encontrado = False
                for registro in registros:
                    if registro[3] == estado_busca:
                        print("Cliente:", registro[0], "|Produto:", registro[1], "|Valor: R$", registro[2], "|Estado:", registro[3])
                        encontrado = True
                if not encontrado:
                    print("Estado não encontrado.")
            case "4":
                print("Saindo...")
                break
            case _:
                print("⚠ Opção inválida.")

def adicionar_pedido():
    while True:
        op = input("\nDeseja adicionar algum novo pedido?\n1 - Sim\n2 - Não\nEscolha uma opção: ").strip()
        match op:
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
            case "2":
                print("Saindo...")
                break

def main():
    while True:
        print("\n=======ANALISADOR DE PEDIDOS=======")
        op = input("\nEscolha uma opção:\n1 - Exibir pedidos\n2 - Exibir análises financeiras\n3 - Buscar pedidos\n4 - Adicionar pedido\n5 - Sair\nDigite o número da opção desejada: ").strip()
        match op:
            case "1":
                exibir_pedidos()
            case "2":
                exibir_analises_financeiras()
            case "3":
                buscar_pedidos()
            case "4":
                adicionar_pedido()
            case "5":
                print("Saindo...")
                break
            case _:
                print("⚠ Opção inválida.")

main()