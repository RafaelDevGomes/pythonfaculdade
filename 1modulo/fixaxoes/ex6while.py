dinheiro = 100

while dinheiro > 0:
    print('Bem vindo!')
    opcao = int(input('digite 1 para saque e 2 para deposito ou 3 para sair: '))

    if opcao == 1:
      saque = int(input('Digite o quanto quer sacar: '))
      dinheiro -= saque
      print(f'Saldo atual: {dinheiro}')

    elif opcao == 2:
        deposito = int(input('Digite o quanto quer depositar: '))
        dinheiro += deposito
        print(f'Saldo atual: {dinheiro}')

    elif opcao == 3:
     print('Até mais!')
     break 

else:
   print('Opção inválida!')     
    

     

