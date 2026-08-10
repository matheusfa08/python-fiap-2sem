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
    print("Email:", registro[0], "\nProduto:", registro[1], "\nValor: R$", registro[2], "\nEstado:", registro[3])

for registro in registros:
    print(len(registros), "Pedidos")
    precos.append(registro[2])
    print(sum(precos))
    print((min(precos)+max(precos))/2)
