'''

* Enunciado
Formas de Pagamento Supermercado Sempre Bom
No Supermercado Sempre Bom, para maior comodidade, os clientes tem várias possibilidades de pagamento de suas compras. A tabela abaixo apresenta as opções disponíveis atualmente.

Código  Condição de Pagamento

D           À vista no dinheiro. Desconto de 10%
P           À vista no PIX. Desconto de 10%
C           No cartão, em 1 vez . Preço normal da compra
            No cartão, em 2 vezes. Juros de 5%

Elabore um programa que leia com entrada o valor total da compra e o código da opção de pagamento.
Se a opção de pagamento for C o programa deve perguntar em quantas vezes o cliente quer pagar, 1 ou 2. 
Como saída, calcule e apresente o valor final a ser pago, com até duas casas decimais.
'''
valor = float(input())
codigo = str(input().upper())
if codigo == "D" or codigo == "P":
	v = valor - valor*0.1
else:	
	if codigo == "C":
		c = int(input("quantas vezes no cartao?"))
		if c == 1:
			v = valor
		elif c == 2:
			v = valor + valor *0.05
print(round(v, 2))
