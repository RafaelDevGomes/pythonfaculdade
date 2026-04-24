saldo = 1000.00
historico = ["Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado","Deposito de 500 realizado"] # lista vazia

print(f'🏧 --- Bem vindo ao caixa eletrônico ---')

while True: # significa q pelomenos uma unica vez, essa variavel vai rodar
    print(f''' --- Menu Principal ---
          [1] depositar
          [2] Sacar
          [3] Ver Saldo
          [4] Ver Histórico
          [5] Sair  
         ''') 
    opcao = input(' ➡️ Escolha uma opção: ')

    #logica para a opção de depósito
    if opcao == '1': 
        valor_deposito = float(input(f'Deposite o valor desejado: R$'))
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            registro = f'deposito: +R$ {valor_deposito: .2f}'
            historico.append() # Append() adiciona algo a lista
            print('🆗 Depósito realizado com sucesso.')

        else:
            print('❌ Valor Inválido, o  depósito deve ser um número positivo.')

    elif opcao == '2':
        valor_saque = float(input(f'Saque o valor desejado: R$'))
        if valor_saque <= 0:
            print('❌ Valor invalido! o saque deve ser um valor positivo')
            
        elif valor_saque > saldo:
            print('❌ Saldo insuficiente para realizar a transação.')

        else: 
            saldo = saldo - valor_saque
            registro = f'Saque: -R$ {valor_saque: 2f}'
            historico.append(registro)
            print('🆗 Saque realizado com sucesso.')

    elif opcao == '3':
        print(f'💸{saldo: .2f}')

    elif opcao =='4':
        print(' --- Histórico de transações --- ')
        if not historico == True:
            print('❌ Nenhuma transação foi realizada ainda')
        else:
            for transacao in historico:
                print(transacao)

    elif opcao == '5':
        print('😁Obrigado por utilizar nosso caixa eletronico')
        break
else: 
    print('❌ Opção invalida, escolha algumas das opções acima')