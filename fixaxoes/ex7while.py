produtosestoque = 20
opcao = 0

while opcao != 4:

    print('Bem vindo ao sistema do mercado!')
    opcao = int(input("Digite 1 para vender produtos, digite 2 para adicionar novos produtos ao estoque, digite 3 para ver a quantidade atual do estoque ou 4 para sair. "))

    if opcao == 4:
        print('Obrigado pela atenção, va embora') 
        break
    
    elif opcao == 1:
        vender = int(input("Quantos produtos deseja vender? "))
        produtosestoque -= vender 
        if vender > produtosestoque:
            print("Não existem tantos produtos em estoque!")
        else:
            print(f"Você vendeu: {vender} e sobrou: {produtosestoque}")   

    elif opcao == 2:
        addestoque = int(input("Quantos produtos você deseja add? "))
        addestoque += produtosestoque
        print(f"Você tem {produtosestoque} e {addestoque} novos produtos")        

    elif opcao == 3:
        print(f"Vc tem: {produtosestoque} produtos no seu estoque") 

            

   