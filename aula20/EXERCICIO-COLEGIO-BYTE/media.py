print("---- " \
    " 🏫📗Olá, seja bem vindo ao sistema do Colégio Byte.🏫📗 " \
    " ----")

def calcular_media (nota1, nota2, nota3):
    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
        return -1.0 
    media = (nota1*2 + nota2*3 + nota3*5) / 10    

    return round(media,1)

 
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = calcular_media(nota1, nota2, nota3)

print(f'Média: {media}')