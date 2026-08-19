#declarar uma função (def)
def calcular_total(nome, preco, desconto=0.10):
    valor_desconto = preco * desconto 
    total = preco - valor_desconto
    return print(f""" 
                 💵💵💵💵Recibo 💵💵💵💵
                 🙎Nome do cliente: {nome}
                 💸Valor do pedido: R$ {preco}
                 💷Desconto aplicado: R$ {desconto}
                🍕🍕total do pedido: R$ {total:.2f}
                """)

#invocação da função
calcular_total("Rafael",45.90)
calcular_total("Capitão pátria",38.50)
calcular_total("Abner",26.26)
calcular_total("Black noir",18.53)
