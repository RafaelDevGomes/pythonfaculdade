historico_escolar = []

print('Bem vindo ao sistema da escola.')

quantidade = int(input('Digite a quantidade de alunos: '))

while quantidade > 0:
    nome = input('Digite o nome do aluno: ')

    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = 'Aprovado'
    elif media >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'

    historico_escolar.append([nome, nota1, nota2, nota3, media, situacao])

    quantidade -= 1

print('Boletim da turma')

i = 0
while i < len(historico_escolar):
    aluno = historico_escolar[i]

    print("Nome:", aluno[0])
    print("Notas:", aluno[1], aluno[2], aluno[3])
    print("Média:", aluno[4])
    print("Situação:", aluno[5])
    print("----------------------")

    i += 1