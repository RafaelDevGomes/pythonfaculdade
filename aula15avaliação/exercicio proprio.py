historico_escolar = []

print(f' --- 🏫 Bem vindo ao sistema da escola! --- ')

while True:
    print(f''' --- ✔️ Menu Principal ---
          [1] Adicionar Notas
          [2] Ver Notas
          [3] Calcular Média
          [4] Ver Situação
          [5] Sair
           ''')
    
    opcao = input('escolha a alternativa ')
    if opcao == '1':

        add_notas = float(input('digite o valor da nota: '))
        if 0 <= add_notas <= 10:
            historico_escolar.append(add_notas)
            print(f'{add_notas} ✔️ 😊sua nota foi adicionada com sucesso!')
        else:
            print('❌🍕nota negada, insira um numero de 0 a 10.')  
            break   
        
    elif opcao == '2':
        input(f'💸💸💸💸{add_notas}')

    elif opcao == '3':
        media = add_notas / 2
        print(f'sua media é {media}')

    elif opcao == '4':
        if add_notas < 5:
            print('❌❌você está frito!')
        else:
            print('parabéns! 🍕🍕')    
    elif opcao == '5':
        print('👋👋👋obrigado por usar o sistema da escola!')
        break