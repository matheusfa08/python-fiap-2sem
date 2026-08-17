#============================================================
#PARTE 1 - LISTA
#============================================================

#Criamos uma lista representando um aluno.
#
#Cada informação ocupa uma posição (índice).

aluno_lista = [
    "Ana",
    20,
    "Sistemas de Informação"
]


#Os índices começam em 0.
#
#0 -> nome
#1 -> idade
#2 -> curso

print("Nome:", aluno_lista[0])

print("Idade:", aluno_lista[1])

print("Curso:", aluno_lista[2])


#============================================================
#PARTE 2 - DICIONÁRIO
#============================================================

#Agora representamos o mesmo aluno utilizando
#um dicionário.
#
#Diferentemente da lista, não precisamos lembrar
#qual é o índice de cada informação.
#
#Utilizamos CHAVE -> VALOR.

aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Sistemas de Informação"
}
#Para acessar uma informação, utilizamos sua chave.
print("\nNome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])

#============================================================
#PARTE 3 - ADICIONANDO E ALTERANDO INFORMAÇÕES
#============================================================

#Podemos adicionar uma nova informação ao dicionário.

aluno["email"] = "ana@email.com"

#Podemos alterar uma informação existente.

aluno["idade"] = 21

print("\nAluno atualizado:")

print(aluno)

#Podemos deletar um item (chave + valor)

del aluno["email"]

print(aluno)

#Podemos verificar as chaves

print("\nChaves")

print(aluno.keys())

#Podemos verificar os valores

print("\nValores")

print(aluno.values())

#Podemos verificar os itens

print("\nItens")

print(aluno.items())

#Podemos percorrer as chaves e valores usando uma estrutura de repetição for

print("\nDados dos alunos:")

for chave, valor in aluno.items():
    print(chave, ":", valor)

#Tratamento de erros - Try Except

print("\nConsulta dicionário\n")

#O código vai TENTAR pegar a variável 'chave' e caso tenha um erro de.. não existir a chave no dicionário, ele vai mandar uma menssagem de erro
try:
    chave = input("Digite a informação que deseja consultar -> ").strip().lower()
    print("Resultado:", aluno[chave])
except KeyError:
    print("Erro: Tal informação não existe no cadastro")

#Com .get()

print(aluno.get("telefone"))

#Com .get + tratativa dentro do próprio .get()

print(aluno.get("telefone", "Telefone não cadastrado"))

#Cada produto será representado por um dicionário

#Aqui, um exemplo de lista de dicionários

produtos = [
    {
    "nome": "Notebook",
    "preço": 4500,
    "quantidade": 10,
    "categoria": "Informática"
    },
    {
    "nome": "Mouse",
    "preço": 99.99,
    "quantidade": 2,
    "categoria": "Informática"
    },
    {
    "nome": "Teclado",
    "preço": 359.50,
    "quantidade": 20,
    "categoria": "Informática"
    }
]

#Um exemplo de como listar cada item
print("\n================LISTA DE PRODUTOS==================")
for produto in produtos:
    print(f"Nome: {produto['nome']}|Preço: R${produto['preço']:.2f}|Quantidade: {produto['quantidade']}|Categoria: {produto['categoria']}")

#Um exemplo de como fazer uma busca
print("\n================BUSCA DE PRODUTOS==================")
produto_busca = input("Digite um produto para buscar - > ").strip().lower().capitalize()
encontrado = False
for produto in produtos:
    if produto["nome"] == produto_busca:
        print(f"Nome: {produto['nome']}|Preço: R${produto['preço']:.2f}|Quantidade: {produto['quantidade']}|Categoria: {produto['categoria']}")
        encontrado = True
if not encontrado:
    print("Produto não encontrado")

#Um exemplo de como adicionar mais uma lista
print("\n================CADASTRO DE PRODUTOS==================")
novo_nome = input("Digite um nome válido - > ").strip().lower().capitalize()
if novo_nome == "":
    raise ValueError("O nome não pode ser vazio")
novo_preco = float(input("Digite um preço válido - > "))
if novo_preco <= 0:
    print("Preço não pode ser 0 ou menos")
nova_quantidade = int(input("Digite uma quantidade válida - > "))
if nova_quantidade < 0:
    print("Não pode se ter um estoque negativo")
nova_categoria = input("Digite uma categoria válida - > ").strip().lower().capitalize()
if novo_nome == "":
    raise ValueError("A categoria não pode ser vazia")

novo_produto = {
    "nome": novo_nome,
    "preço": novo_preco,
    "quantidade": nova_quantidade,
    "categoria": nova_categoria
}

produtos.append(novo_produto)

for produto in produtos:
    print(produto)