idade = int(input('digite sua idade: '))
peso = int(input('digite seu peso: '))
temp_treino = int(input('a quanto tempo treina? '))


if idade >= 18 and peso <= 50 and temp_treino >= 1:
    print('Você pode treinar sozinho com uma planilha mediana.')

elif idade >= 18 and peso >= 80 and temp_treino >= 3:
    print('Você pode treinar sozinho com igual um trator! amassa')

else: 
    print('pode treinar acompanhado apenas de um responsável.') 