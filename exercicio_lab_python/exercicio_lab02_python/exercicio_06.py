#Enunciado:

'''
Restaurante do Zezinho - dinheiro curto
Além do serviço de buffet, o restaurante do Zezinho dispõe de sucos e salgados para a comunidade UFAM. A tabela de preços é a seguinte:

Item	Preço
Suco	R$ 3,00
Salgado	R$ 3,50
 

Você e seus amigos estão com pouco dinheiro, mas gostariam de fazer um lanche no restaurante do Zezinho. Escreva um programa que leia, nesta ordem:

A quantidade de sucos.
A quantidade de salgados.
O valor que vocês têm disponível.
Como saída, imprima:

O valor total do lanche arredondado para duas casas decimais. 
'Sim' se o valor disponível for suficiente ou 'Nao', caso contrário.
'''

suco = 3.00
salgado = 3.50

a=int(input())
b=int(input())
c=float(input())

total = a*suco+b*salgado

print("{:.1f}".format(total))
if c >= total:
	print("Sim")
else:
	print("Nao")