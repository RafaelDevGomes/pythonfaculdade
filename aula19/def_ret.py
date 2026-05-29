#função que exibe os valores, tamanhos e sabores das pizzas

def exibir_cardapio():
    print('==== CARDÁPIO DA PIZZARIA DO CÓDIGO ====')

    print(f"""
   🍕Marguerita - P: R$25, M: R$35, G: R$45🧑‍🍳 
   🍕Calabresa - P: R$28. M: R$37, G: R$46🧑‍🍳 
   🍕Frango - P: R$29. M: R$38, G: R$47🧑‍🍳 
    """)

# exibir_cardapio()

#função para aplicar desconto onde o preço e o percentual de desconto será passado no momento da invocação da função
valor_sem_desc = 40

# def aplicar_desconto(preco, percentual):
#     # preco * (1 - percentual /100)
#     return preco * percentual

# preco_final = valor_sem_desc - aplicar_desconto(valor_sem_desc, 0.10)
# print(f'''
#     Preço com desconto: R${preco_final:.2f}
#     Preço sem desconto: R${valor_sem_desc:.2f}
# ''')

#declarar função que receberá por padrão que a borda não é recheada. Além disso, irá receber o tamanho da pizza.
def fazer_pedido(sabor, tamanho="M", borda_recheada=False):
    borda = "com borda recheada" if borda_recheada else "sem borda"

    #VARIAVEL = valor se verdadeiro if condição logica else valor vai será falso.
    print(f'Pedido: {sabor} | {tamanho} | {borda}')
    

print(f'fazer_pedido("margherita")')
print(f'fazer_pedido("Frango", "G")')
print(f'fazer_pedido("Calabresa", "P", True)') 
 
