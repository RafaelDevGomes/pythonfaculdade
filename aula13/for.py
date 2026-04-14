# contar de 1 até 5
# for numero in range(1,1001):
#   print(f'eu sou o numero {numero}')

# exemplo tabuada ->

i = 5 # variavel no escopo global

for numero in range (1,11):
    total = i * numero  # variavel no escopo local
    print(f'5x {numero} = {total}')
    