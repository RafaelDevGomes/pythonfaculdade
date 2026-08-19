# def registrar_cliente (nome, telefone, endereco):
#     print(f"=== DADOS DO CLIENTE ===")
#     print(f"Cliente: {nome}")
#     print(f"Telefone: {telefone}")
#     print(f"Endereço: {endereco}")

# registrar_cliente(
#     telefone = "2194820442",
#     nome = "Ana Lima",
#     endereco = "Rua das Pizzas, 42"
# )


# retorno de valores, "unpacking" - devolve uma tupla com os returns

def resumo_pedido (itens, desconto=0):
    subtotal = sum(itens)
    valor_desconto = subtotal * (desconto / 100)
    total = subtotal - valor_desconto
    return subtotal, valor_desconto, total # return 3 valores

sub, desc, tot = resumo_pedido([35.0, 12.0, 8.5], desconto=10)
print(f'sub total: R$ {sub:.2f}')
print(f'desconto: R$ {desc:.2f}')
print(f'total: R$ {tot:.2f}') 

#invocando e desempacotando a função/return 

