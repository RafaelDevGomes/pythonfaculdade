print("---Seja Bem Vindo ao sistema do colégio byte!---")

def calcular_media(notas):
    sum(notas)
    return sum(notas) / len(notas) 
#mais uma vez um exemplo de len, ele vai ler a quantidade e ficar safezudo

def verificar_nota(mensagem):
    while True:
        nota = float(input(mensagem))
        if 0 <= nota <= 10:
           return nota 
        print("NOTA INVALIDAAAAAA!!!! DIGITE UMA NOTA COERENTE!")

notas_aluno = []

nota1 = verificar_nota("Digite sua primeira nota: ")
nota2 = verificar_nota("Digite sua segunda nota: ")
nota3 = verificar_nota("Digite sua terceira nota: ")


notas_aluno.append(nota1)
notas_aluno.append(nota2)
notas_aluno.append(nota3)


media = calcular_media(notas_aluno)
print(f"sua media foi: {media:.2f}")

if media >= 7:
    print("Você passou, parabéns!")

else:
    print("Você está de recuperação!")


def determinar_situacao(media, honra = True):
    if media >= 7:
     print("Você verdadeiramente tem honra! 🎖") 
     situacao = "Aprovado ✅"
    
    elif media >= 5: 
     print("Você está de recuperação!")
     situacao = "Recuperação ⚠️"
    
    else:
     print("Reprovado.")
     situacao = "Reprovado ❌"
     
    if honra == True and media >= 9.0:
       print("Você passou e é o mais honrado! 🏅")
       mensagem_honra = "Menção honrosa."
        
    else:
       print("")
    return situacao, mensagem_honra

situacao, mensagem_honra = determinar_situacao(media)