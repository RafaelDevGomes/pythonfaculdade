def total_junto(lista):
    return sum(lista)

def desconto_aplicado(total, desconto=0.30):
    return total - (total * desconto / 100)
    
precos = [693.21, 432.74, 792.35]   

total = total_junto(precos)
totalfinal = desconto_aplicado(total, 30)

print(f"O total é: {total}")
print(f"O valor com desconto aplicado é: {totalfinal}")