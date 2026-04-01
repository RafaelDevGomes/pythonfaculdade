# variaveis da pizzaria

pizza_sabor = input("Digite o sabor da pizza: [frango com requeijao], [calabresa], [portuguesa], [marguerita]: ")
pizza_tamanho = input("Digite o tamanho da pizza: [pequena], [média], [grande]: ")
dia_semana = input("Digite o dia da semana: [quarta-feira], [quinta-feira], [sexta-feira], [sabado], [domingo]: ")
taxa_frete = 2
#promoções -> estruturas condicionais 

print(f" o sabor escolhido da pizza é {pizza_sabor} o tamanho é {pizza_tamanho} e o dia da semana é {dia_semana}")

#comprar pizza de qualquer tamanho no sabado o refri é grátis
if dia_semana == "sabado":
    print(f"🍕pedido aceito com sucesso!")
    print(f"🥤o refri hoje é por conta da casa!")
#no domingo, qualquer pizza de qualquer tamanho no domingo, o frete e o refri é grátis
elif dia_semana == "domingo": 
    print(f"🍕pedido aceito com sucesso!")
    print(f"🥤o refri hoje é por conta da casa!")
#comprar uma pizza de calabresa no tamanho medio pra cima em qualquer dia, o frete é grátis
elif pizza_sabor == "calabresa" and pizza_tamanho == ["média", "grande"]:
    print(f"🍕pedido aceito com sucesso!")
    print(f"🚚o frete hoje é por conta da casa!")
