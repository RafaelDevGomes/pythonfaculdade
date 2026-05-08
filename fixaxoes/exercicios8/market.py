quantidade = 0
total = 0

print("----💸💸💸CAIXA REGISTRADORA----💸💸💸")

preco = float(input('Digite o preço do produto(0 para encerrar): R$ '))

while preco != 0:
    total += preco 
    quantidade += 1
    
    preco = float(input('Digite o preço do produto(0 para encerrar): R$ '))

print('-----RESULTADOS-----')
print(f'a quantidade de produtos é {quantidade}')
print(f'o preço total é: R${total}')