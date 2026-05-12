valor100kwh = 0.40
valor200kwh = 0.60
valoracima200kwh = 0.90

print(f'----- 😁Bem vindo ao Sistema de calculo de Energia eletrica😊 -----')

while True:
    input_kwa = input(f'digite a quantidade de KWS consumidos (ou "sair" para encerrar): ')
    if input_kwa.lower() == 'sair':
        print('Vlw falou!\n')
        break
    elif not input_kwa.isdigit():
        print('entrada inválida, digite um número válido ou "sair" para encerrar.\n')
        continue
    else:
        kwh = int(input_kwa)
        if kwh <= 100:
            valor_total = kwh * valor100kwh
            print('📈 a faixa de consumo é: 0 a 100 kwh.')
            print(f'O valor total da conta de energia é {valor_total:.2f}')
        elif kwh <= 200:
            valor_total = 100 * valor100kwh + (kwh - 100) * valor200kwh
            print('A faixa de consumo é: 0 a 200kwh.')
            print(f'O que vc gastou foi: {valor_total:.2f}')        
        else:
            valor_total = 100 * valor100kwh + 100 * valor200kwh + (kwh - 200) * valoracima200kwh
            print('A faixa de preço é: 0 a 300kwh.')
            print(f'O que vc gastou foi: {valor_total:.2f}')