print("sistema de emprestimo bancario")

# entradas dos dados(variaveis)
idade = int(input("digite a idade para receber o emprestimo:"))
salario = float (input("digite o salario para receber o emprestimo:"))
tempo_servico = int (input("digite o tempo de serviço para receber o emprestimo:"))

if idade < 18 and salario < 2000 and tempo_servico < 2:
    print(f"negado com sucesso")
elif idade >= 18 and salario >= 5000 and tempo_servico >= 2:
    print(f"emprestimo aprovado.")
elif idade >= 18 and salario >= 2000 and tempo_servico >= 2:
    print(f"emprestimo aprovado com juros.")
else:
    print(f"negado com sucesso")
