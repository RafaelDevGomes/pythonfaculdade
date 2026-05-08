print('^^^^^^💡Bem vindo ao sistema da rede eletríca!🔦^^^^^^')
consumo = int(input('Digite o quanto a de Kwh a empresa consumiu nesse mês: '))
conta = int

if consumo < 0:
    print('valor inválido.')

elif consumo <= 100:
    conta = consumo * 0.40
    print(f'Você deve pagar: R${conta:.2f} por R$0.40 a kws')    

elif consumo <= 200:
    conta = consumo * 0.60
    print(f'Ta consumindo litros!! deve pagar: R${conta:.2f} por R$0.60 a kws')

elif consumo > 200:
    conta = consumo * 0.90
    print(f'É uma usina nuclear? deve pagar: R${conta:.2f} por R$0.90 a kws')

else:
    print('Digito inválido.')
