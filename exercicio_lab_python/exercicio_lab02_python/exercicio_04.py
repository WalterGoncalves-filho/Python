#Enunciado

'''
Loja virtual de games - desconto
Uma loja de jogos eletrônicos na Internet está com um desconto na compra de dois jogos. Na compra do segundo jogo você ganha um desconto de 25% no valor do segundo jogo.

Dessa forma, escreva um programa que leia:

A quantidade de jogos (1 ou 2).
O preço do primeiro jogo.
O preço do segundo jogo, se for o caso.
Como saída, imprima:

o valor total da compra.
O valor de saída deve ser arredondado para duas casas decimais. 
'''

def desconto(a):
	b = a - (a* 0.25) 
	return b


quantdade_de_jogos = int(input("digite a quantidade de jogos: "))
if quantdade_de_jogos == 2:
	preco_do_1jogo = float(input("digite o preco do jogo 1:"))
	preco_do_2jogo =float(input("digite o preco do jogo 2 :"))
	valor = desconto(preco_do_2jogo)+preco_do_1jogo
	print("{:.2f}".format(valor))
else:
	preco_do_1jogo = float(input("digite o preco do jogo:"))
	print("{:.2f}".format(preco_do_1jogo))

