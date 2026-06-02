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
opcao = ""
girada = 15
soco = 20
facada = 50
abraço_gentil = 20

while opcao != 4:
    print("""Humano, decida qual rota você desejará seguir:
    1 para rota pacifista
    2 para rota genocida
    3 para rota neutra   
    4 para sair (fechar o jogo)             
    """)
    
if opcao == "4":
    print("ADEUS HUMANO!")
    

elif opcao == "1":
    print("Você é uma alma bondosa, porém ainda enfrentará desafios em seu caminho..")
    vida_boss_pacifista = 50 

    print(f'Um boss apareceu! ele tem {vida_boss_pacifista}')
    
   
    if girada: 
     print(f'Você deu {girada} de dano no Boss!')

    elif soco:
       print(f'Você deu {girada} de dano no Boss!')

    elif facada:
       print(f'Você deu {facada} de dano no Boss.. ele não parece estar bem.. você ganhou 10 de gold e ganhou a batalha.')   
    
    elif vida_boss_pacifista < 20:
       print(f'Você abraça o boss.. ele fica confuso mas gosta, o boss vai embora, você venceu!')
       

elif opcao == "2":
 vidas_jogador += 80
 print("Você é uma má pessoa, você não é nem um monstro nem um humano.. você é uma aberração!")  



