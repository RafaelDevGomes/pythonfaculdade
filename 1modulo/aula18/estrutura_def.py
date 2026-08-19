#as funções podem ou não receber propriedades
# def saudacao():
#     print('Seja Bem-Vindo(a)!!!!')

# # saudacao()
# # saudacao()
# # saudacao()
# # saudacao()

# #calcule o preço total de uma pizza onde será passado um dicionário com os tamanhos e valores. Além disso, o cliente pode solicitar ou não a borda recheada. Ao final, retorne o preço.

# #1.Pequena, Média ou Grande, qualquer pizza terá o mesmo valor dependendo do tamanho.
# #2.Se o cliente optar pela borda recheada, deverá ser acrescido no valor da pizza + R$8.00

def calcular_preco_pizza( tamanho, borda_recheada=False):
    "Calcule o preço da pizza"
    tabela = {"P": 25.00, "M": 28.50, "G": 31.90}
    preco = tabela[tamanho]

    if borda_recheada:

        preco += 8.00

    return preco

print(calcular_preco_pizza("P",True))
print(calcular_preco_pizza("M"))
print(calcular_preco_pizza("G",True))


