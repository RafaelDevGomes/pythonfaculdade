print('Olá! seja bem vindo ao sistema da epic games ni- cria!')

idade = int(input('Digite sua idade: '))
pontuacao = int(input('Digite sua pontuação: '))
temp_jogo = float(input('Digite seu tempo de jogo: '))

if idade >= 18 and pontuacao >= 1000 and temp_jogo >= 2.5:
    print(f'Caramba gordao! você não sai da cadeira! seus feitos são impressionantes! {idade} anos, {pontuacao}pts e {temp_jogo} anos!')

elif idade >= 18 and pontuacao >= 500 and temp_jogo >= 1:
    print(f'Um jogador mediano de respeito! seus feitos são: {idade} anos, {pontuacao}pts e {temp_jogo} anos!')

elif idade <= 18 and pontuacao >= 500:
    print(f'Jovem talento! seus feitos são: {idade} anos, {pontuacao}pts e {temp_jogo} anos!')

else: 
    print(f'Hmpft...New gens.. com feitos de: {idade} anos, {pontuacao}pts e {temp_jogo} anos!')