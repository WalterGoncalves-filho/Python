# EXERCICIO 1:

#Escreva um programa que leia dois números inteiros, nesta ordem:
#X (dividendo)
#Y (divisor)
#Como saída, imprima os quatro elementos da divisão inteira, nesta ordem:
#dividendo
#divisor
#quociente
#resto

#_________________________________________________________________________________________________

x = int(input('escreva dividendo: ')) 
y = int(input('escreva divisor: '))


quo =  x//y 
rest = x%y

print(x)
print(y)
print(quo)
print(rest)