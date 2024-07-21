# EXERCICIO 9:
from math import*
#Escreva um programa que leia o valor de um raio r, inserido via teclado.
#Como saída, determine as seguintes informações, nesta ordem:
#Área de um círculo com o raio r.
#Volume de uma esfera com raio r.
#Arredonde os resultados com até 03 casas decimais de precisão.
################################################################################################################################

#DICAS: 

#Importe o módulo math, para trabalhar com funções e constantes matemáticas.
#Área de um círculo de raio "r": 
#A=πr².
#Volume de uma esfera de raio "r": 
#V=4/3πr³.
#Use a constante "pi" do módulo math em seus cálculos. Não use o valor aproximado dela.
#Dentro do comando print, use o comando round(x, 3) para arredondar a resposta x com até três casas decimais.

#_______________________________________________________________________________________________________________________________

#entrada: 

r = float(input('valor de R: '))

# PARTE LÓGICA:

area = pi*r**2

volume = 4/3*pi*r**3

# SAÍDA: 

print(round(area, 3))

print(round(volume, 3))


