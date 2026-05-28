tentativas = 5

while tentativas > 0:
    tentar = int(input('Digite a quantidade de tentativas: '))
    tentativas -= tentar
    print(f'Você ainda tem: {tentativas} restantes!')
    
if tentativas > 3:
    print('Continue!')
else:
    print('Suas tentativas acabaram, volte outro dia.')