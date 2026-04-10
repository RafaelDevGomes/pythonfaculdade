idade = int(input("Informe a sua idade: "))
cadastro = input("O senhor possui cadastro? ")
            
carro = input("Tipo de veiculo? ")
vip = input("O senhor possui cadastro vip? ")

if idade < 18:
   print("Entrada negada.")

elif carro == "grande":
   print("Estacione no estacionamento D")

elif vip == "sim":
   print("Passe automaticamente para o estacionamento E")

elif cadastro == "sim":
   print("Passe direto para o estacionamento A")

else:
   print("Pode entrar!")
