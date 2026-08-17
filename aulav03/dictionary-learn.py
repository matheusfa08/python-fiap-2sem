#Exemplo prático de dicionários
pedido = {
    "email": "ana@gmail.com",
    "produto": "Headset",
    "valor": 400,
    "estado": "SP"
}

#Facilidade: Saber qual a informação com mais facilidade, 'substituindo' o index com a chave
#Exemplos de aplicação:

print(f"Email da cliente: {pedido["email"]}")
print(f"Produto pedido: {pedido["produto"]}")
print(f"Valor do pedido: R${pedido["valor"]:.2f}")
print(f"Estado do cliente: {pedido["email"]}")