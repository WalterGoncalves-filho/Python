#exercicio 6: 
#Conversão de Celsius para Kelvin
#Você está trabalhando em uma estação meteorológica e precisa fornecer as temperaturas em diferentes escalas para os visitantes. Crie um programa que receba a temperatura em graus Celsius e realize a conversão para Kelvin.
#Considere a fórmula de conversão:
#Kelvin = Celsius + 273.15
#A saída deve ser arredondada para duas casas decimais.

celsius = float(input("Escala em C°: "))
kelvin = celsius + 273.15


print(round(kelvin, 2))