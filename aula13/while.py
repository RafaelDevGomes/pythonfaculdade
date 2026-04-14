# crie um sistema onde o valor inicial é de R$1000 e o usuario consiga realizar um saque e ao final seja exibido o valor restante do saldo.

saldo = 1000
while saldo > 0:
    saque = float(input("digite o valor do saque: "))
    saldo -= saque
    print(f"saldo restante: {saldo}")