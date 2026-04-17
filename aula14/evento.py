while True:
    nome = input("Digite seu nome: (ou sair) ")
    
    if nome == "sair":
        print("sistema encerrado")
        break

    idade = float(input("digite sua idade: "))
    ingresso = input("Digite se possui ingresso: ")
    

    if idade <16 or ingresso =="n":
     print("Sistema encerrado.")

    else: 
     print("Bem vindo!")
