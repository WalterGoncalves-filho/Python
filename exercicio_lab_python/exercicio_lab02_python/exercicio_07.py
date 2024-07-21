#Enunciado:

'''
COMPRA DE MORANGOS
Um supermercado tem uma grande variedade de produtos em seu hortifruti. 
Dentre as frutas, produtos mais comprados pelos consumidores, os morangos podem ser comprados com desconto. 
Cada um custa R$ 1,50, caso o cliente compre menos do que uma dúzia. Porém, na compra de doze morangos ou mais, eles saem pelo preço de R$ 1,35 cada.
Escreva um programa que leia o número de morangos comprados, calcule e escreva o valor total da compra. 
A saída deve conter duas casas decimais de precisão.
'''

a=int(input())

if a >= 12:
	b = a*1.35
else:
	b = a*1.50
print("{:.2f}".format(b))