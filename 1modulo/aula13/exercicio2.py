emprestimo = 3000

while emprestimo > 0:
    saque = int(input("digite o valor do emprestimo: "))
    emprestimo -= saque
    print(f"possível emprestimo restante: {emprestimo}")