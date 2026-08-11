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

for registro in registros:
    print("Email:", registro[0], "\nProduto:", registro[1], "\nValor: R$", registro[2], "\nEstado:", registro[3],"\n")

for registro in registros:
    precos.append(registro[2])

print(len(registros), "Pedidos")
print("Soma dos preços: R$", sum(precos))
print("Média dos preços: R$", (min(precos)+max(precos))/2)
print("Menor preço: R$", min(precos))
print("Maior preço: R$", max(precos))

print("\nAgora vamos realizar buscas nos pedidos cadastrados.")

while True:
    op = input("Deseja ver os pedidos por:\n1 - Email\n2 - Produto\n3 - Estado\n4 - Sair\nEscolha uma opção: ").strip()
    match op:
        case "1":
            email_busca = input("\nDigite o email que deseja buscar: ").strip().lower()
            encontrado = False
            if not encontrado:
                print("Email não encontrado.")
            for registro in registros:
                if registro[0] == email_busca:
                    print("Email:", registro[0], "\nProduto:", registro[1], "\nValor: R$", registro[2], "\nEstado:", registro[3])
                    encontrado = True
        case "2":
            produto_busca = input("\nDigite o produto que deseja buscar: ").strip().lower()
            encontrado = False
            for registro in registros:
                if registro[1] == produto_busca:
                    print("Email:", registro[0], "\nProduto:", registro[1], "\nValor: R$", registro[2], "\nEstado:", registro[3])
                    encontrado = True
            if not encontrado:
                print("Produto não encontrado.")
        case "3":
            estado_busca = input("\nDigite o estado que deseja buscar: ").strip().upper()
            encontrado = False
            for registro in registros:
                if registro[3] == estado_busca:
                    print("Email:", registro[0], "\nProduto:", registro[1], "\nValor: R$", registro[2], "\nEstado:", registro[3])
                    encontrado = True
            if not encontrado:
                print("Estado não encontrado.")
        case "4":
            print("Saindo...")
            break
        case _:
            print("⚠ Opção inválida.")

print("\nVamos ver mais análises:")

print("\nProdutos mais vendidos:")
produtos = []

for registro in registros:
    produtos.append(registro[1])

maior_quantidade = 0

for produto in produtos:
    quantidade = produtos.count(produto)
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        produto_mais_vendido = produto

print("\nQuantidade de vendas:", maior_quantidade)

produtos_exibidos = []
 
for produto in produtos:
    quantidade = produtos.count(produto)
    if quantidade == maior_quantidade:
        # Verifica se o produto já foi exibido.
        # Isso evita imprimir o mesmo produto mais de uma vez.
        if produto not in produtos_exibidos:
            print(produto)
            produtos_exibidos.append(produto)

print("\nClientes que mais compraram:")
maior_quantidade = 0

emails = []

for registro in registros:
    emails.append(registro[0])

for email in emails:
    quantidade = emails.count(email)
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        cliente_mais_frequente = email

print("\nMaior quantidade de compras por cliente:", maior_quantidade)

for email in emails:
    quantidade = emails.count(email)
    if quantidade == maior_quantidade:
        if email not in produtos_exibidos:
            print(email)
            produtos_exibidos.append(email)

print("\nEstado com mais pedidos:")
estados = []

for registro in registros:
    estados.append(registro[3])

maior_quantidade = 0

for estado in estados:
    quantidade = estados.count(estado)
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        estado_mais_pedidos = estado

print("\nQuantidade de pedidos:", maior_quantidade)

estados_exibidos = []

for estado in estados:
    quantidade = estados.count(estado)
    if quantidade == maior_quantidade:
        if estado not in estados_exibidos:
            print(estado)
            estados_exibidos.append(estado)

print("\nPreços em ordem crescente:")
precos_ordem_crescente = sorted(precos)
print(precos_ordem_crescente)