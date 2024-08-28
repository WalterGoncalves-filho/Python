'''
* Enunciado
Total do consumo de água
Escreva um programa que tenha como entrada um número inteiro que corresponde ao consumo de água de uma casa (medido em m3).
Como saída, imprima o total a ser pago na conta de água.

Este total é composto por uma parte fixa de R$20 (saneamento) mais uma parte que varia de acordo com o consumo do cliente:

R$ 2,00 por m3, se o consumo for menor que 10.
R$ 2,50 por m3, se o consumo for maior ou igual a 10 e menor que 20.
R$ 2,75 por m3, se o consumo for maior ou igual a 20 e menor que 40.
R$ 3,00 por m3, se o consumo for maior ou igual a 40.
 A saída deve ser arredondada para duas casas decimais.
 
'''
c = int(input())
a = 20 
if c < 10:
   c = c*2.0 + a
elif 10 <= c < 20:
   c = 2.5*c + a 
elif 20 <= c <40:
   c = 2.75*c + a 
elif c >= 40:
   c = 3.0*c + a 
print(round(c, 2))
