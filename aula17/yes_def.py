#declarar uma função (def)
def calcular_total(preco, desconto=0.10):
    valor_desconto = preco * desconto 
    total = preco - valor_desconto
    return print(f""" 
                 💵💵💵💵Recibo 💵💵💵💵
                 💸Valor do pedido: R$ {preco}
                 💷Desconto aplicado: R$ {desconto}
                🍕🍕total do pedido: R$ {total:.2f}
                """)

#invocação da função
calcular_total(45.90)
calcular_total(38.50)
calcular_total(26.26)
calcular_total(18.53)
