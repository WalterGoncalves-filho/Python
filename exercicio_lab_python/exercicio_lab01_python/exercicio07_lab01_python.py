#exercicio 7: 
#Conversão de Celsius para Fahrenheit
#Você está trabalhando em uma estação meteorológica e precisa fornecer as temperaturas em diferentes escalas para os visitantes. Crie um programa que receba a temperatura em graus Celsius e realize a conversão para Fahrenheit.
#considere as fórmulas de conversão:
#Fahrenheit = (Celsius * 9/5) + 32
#A saída deve ser arredondada para duas casas decimais.


celsius = float(input("Escala em C°: "))
fahrenheit = (celsius * 9/5) + 32

print(round(fahrenheit, 2))