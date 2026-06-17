def somar_total(lista):
    return sum(lista)
    
def aplicar_desconto(total, desconto=0.20):
    return total - (total * desconto / 100)

precos = [21.5, 29.2, 46.1]

total = somar_total(precos)
final = aplicar_desconto(total, 20)

print(f"Total: {total}")
print(f"total com desconto: {final}")

