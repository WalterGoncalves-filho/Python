
#Enunciado:

'''
Conversor de temperatura
Escreva um programa que converta uma temperatura da escala Celsius para Fahrenheit ou vice-versa. Use a seguinte equação para conversão:

C=5/9(F-32)
   
Para isso, você deverá ler duas entradas:

escala em que a temperatura está representada: C para Celsius, ou F para Fahrenheit.
valor da temperatura.
Como saída, imprima:

a temperatura convertida para a outra escala, arredondada em duas casas decimais.
'''

convercao = str(input())
c_f = float(input())
if convercao == "F":
	c = (5*c_f - 160)/9
	print(round(c, 2))
else:
	f = (9*c_f + 160)/5
	print(round(f, 2))
	
