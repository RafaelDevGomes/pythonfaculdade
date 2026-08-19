nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
nota = int(input("Digite sua nota: "))


if nota == 10:
    print(f"MEUS PARÁBENS {nome}! SUA NOTA FOI EXCELENTE! UM {nota} EXEMPLAR!")

if nota >= 7:
    print(f"parábens {nome}! sua nota foi: {nota}!")

else:
    print(f"você ficou de recuperação {nome}, sua nota foi: {nota}")