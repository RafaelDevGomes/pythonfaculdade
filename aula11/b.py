idade = int(input("digite a idade para receber o emprestimo:"))
salario = int (input("digite o salario para receber o emprestimo:"))
tempo_servico = int (input("digite o tempo de serviço para receber o emprestimo:"))

if idade >= 18 and salario >= 2000 and tempo_servico >= 2:
    print(f"emprestimo aprovado com juros, sua idade é {idade}, seu salario é {salario} e seu tempo de serviço é {tempo_servico}")

elif idade >= 18 and salario >= 5000 and tempo_servico >= 2:
    print(f"emprestimo aprovado automaticamente, sua idade é {idade}, seu salario é {salario} e seu tempo de serviço é {tempo_servico}")
    
else:
    print(f"emprestimo negado, sua idade é {idade}, seu salario é {salario} e seu tempo de serviço é {tempo_servico}, bobao") 