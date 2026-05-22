preco1 = 45.90
desconto1 = preco1 * 0.10
total1 = preco1 - desconto1
print(f"Total: R$ {total1:.2f}")

# Pedido 2 — código repetido!
preco2 = 38.50
desconto2 = preco2 * 0.10
total2 = preco2 - desconto2
print(f"Total: R$ {total2:.2f}")

def calcular_total(preco, desconto=0.10):
    return preco * (1 - desconto)

print(calcular_total(45.90))
print(calcular_total(38.50))