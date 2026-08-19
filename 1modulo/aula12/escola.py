idade = int(input("digite a sua idade: "))
nota = float(input("digite a sua nota do bimestre: "))

aulasp = int(input("digite quantas aulas você esteve presente: "))
aulast = int(input("digite o número de aulas totais: "))

frequencia = (aulasp / aulast) * 100
print(f"frequência: {frequencia}%")


if idade < 18:
 print("você foi recusado na universidade por ser menor de idade.")

elif idade >= 18 and nota >= 6.0 and frequencia >= 75:
 print("você foi aprovado.")

elif nota >= 9.0:
 print("você foi aprovado automaticamente.")

else:
 print("você não foi aprovado.")