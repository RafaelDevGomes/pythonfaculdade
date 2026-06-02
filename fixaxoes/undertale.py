#Crie um mini jogo em Python com 3 rotas diferentes. O jogador deve escolher entre três caminhos no início do jogo. Cada rota leva a um chefe diferente.

# Regras do exercício:

# Crie uma variável que represente o jogador (com pelo menos vida).
# Crie 3 funções de rota (uma para cada caminho).
# Cada rota deve chamar uma função de chefe diferente.
# Cada chefe deve fazer alguma alteração no jogador (ex: tirar vida ou mostrar uma mensagem diferente).
# No final, mostre o estado do jogador (vida restante).

# Objetivo:

# Treinar uso de funções, organização do código e compartilhamento de dados entre partes do programa.

print('Olá humano! Bem vindo ao mundo subterráneo!')


vidas_jogador = 20

while True:
    print("""Humano, decida qual rota você desejará seguir:
    1 para rota pacifista
    2 para rota genocida
    3 para rota neutra   
    4 para sair (fechar o jogo)             
    """)
    opcao = input("Escolha seu destino, humano: ")
    
    if opcao == "4":
     print("ADEUS HUMANO!")
     break

    elif opcao == "1":
         print("Você é uma alma bondosa, porém ainda enfrentará desafios em seu caminho..")
         vida_boss_pacifista = 50 

         print(f'Um boss apareceu! ele tem {vida_boss_pacifista} de vida!')
        
         print("escolha seu ataque: girada/soco/facada/abraço gentil")
         acao = int(input("Ação: "))
         if acao == 1:
           vida_boss_pacifista -= 15
           print(f"Você tirou 15 de dano!")

         elif acao == 2:
           vida_boss_pacifista -= 20
           print("Essa doeu! você tirou 20 de vida do boss!")

         elif acao == 3:
           vida_boss_pacifista -= 50
           print("Você está indo para um caminho que não tem como ter volta.. o boss foi derrotado, mas a qual custo?")

         elif acao == 4:
           print("Você abraçou o boss.. ele acha estranho mas aprecia e te abraça de volta..")
           print("Ele some na escuridão das ruinas com um sorriso, você fez um amigo!")   

         else:
           print("Aconteceu algo? vc digitou algo inesperado.. tente novamente")

    elif opcao == "2":
        print("Você é uma má pessoa, você não é nem um monstro nem um humano.. você é uma aberração!")  
        vidas_jogador += 80
        vida_boss_genocida = 200

        print(f'Uma presa apareceu.. ele tem {vida_boss_genocida} de vida!')
        
        print("Escolha um ataque para usar contra o boss: facada/soco forte/porretada/encontrão")
        acao = int(input("Ação: "))
        if acao == 1:
          vida_boss_genocida -= 50
          print(f"ISSO! atinga-o mais algumas vezes! ele ainda tem {vida_boss_genocida}hp!")

        elif acao == 2:
          vida_boss_genocida -= 45
          print(f"BEMMM NO QUEIXO! temos que derrubar esse grandalhão! ainda tem {vida_boss_genocida}hp!")
        
        elif acao == 3:
          vida_boss_genocida -= 60
          print(f"HAHAHAHAHA bem na cabeça! continue atingindo ele até ele cair! ainda sobra {vida_boss_genocida}hp!")

        elif acao == 4:
           vida_boss_genocida -= 45
           print(f"Não foi seu melhor ataque.. mas da pro gasto! ainda sobram {vida_boss_genocida}hp!")

        else:
           print("É.. tudo bem com vc? vc digitou algo totalmente inesperado e bizarro! tente novamente")
     
    elif opcao == "3":
      print("Boa escolha humano.. porém nada nessa rota acontece feijoada.")
      break


    else:
     print("Bro, tu digitou algo errado, tenta dnv ai")
       