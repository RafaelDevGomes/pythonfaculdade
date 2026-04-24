nota = 0.0
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
    opcao = input(' ➡️ escolha uma opção: ')
    if opcao == '1':
        add_notas = float(input('Digite o Valor da nota: '))
        if 0 < add_notas <= 10:
            historico_escolar = add_notas + nota
            historico_escolar = 'Notas: {nota: .1f}'
            historico_escolar.append(add_notas)
            
        else:
            print('❌Insira um numero de 1 até 10')
            continue
