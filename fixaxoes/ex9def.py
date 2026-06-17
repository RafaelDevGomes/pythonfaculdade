def calcular_media(notas):
    sum(notas)
    return sum(notas) / len(notas) # len é a quantidade de coisas colocadas na variavel (evitar ficar digitando toda hora a quantidade, apenas digitam o len e ta safe)
# ent geralmente usam isso pra fazer media ne sem precisar ficar declarando a quantidade de notas, eu precisaria apenas digitar as notas e usar o len na propria variavel notas?
media = calcular_media([10, 5, 3, 2, 6])
print(media)

if media >= 7:
    print("Parabéns! você passou!")

else: 
    print("Você está de recuperação!")