# EXERCICIO 8: 

#_____________________________________________________________________________________________________________________________

# Considere um triângulo de lados a, b, c. O semiperímetro (metade do perímetro) desse triângulo é definido por:
# s = (a+b+c)/2
# A área A do triângulo pode ser calculada pela seguinte fórmula:
# A = (s(s−a)(s−b)(s−c))**0.5
# Escreva um programa que leia os comprimentos dos lados de um triângulo. 
# Como saída, determine a sua área arredondada com até cinco casas decimais.

#_____________________________________________________________________________________________________________________________

# entrada: 

a = float(input(' valor de "A" : '))
b = float(input(' valor de "B" : '))
c = float(input(' valor de "C" : '))

# semiperimetro: 

s = (a+b+c)/2

#Área do perimetro: 

Area = (s*(s-a)*(s-b)*(s-c))**0.5

# Saída: 

print(Area)