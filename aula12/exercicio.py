idade = int(input("Bom dia, idade por favor: "))
salário = int(input("Informe seu salário: "))

nota_concurso = float(input("Informe sua nota do concurso: "))
consistencia = int(input("Informe a sua constência de trabalho: "))

if idade < 18:
    print("Você é menor de idade. GET OUT")

elif salário >= 3000 and nota_concurso >= 500 and consistencia >= 75:
    print(f"Você será promovido a um cargo maior e tem uma consistência de {consistencia}%.")

else: 
    print("Você é de maior mas não atende aos requisitos.")
