# Exercicio 01:

#                                             Enunciado

# Qual o valor da fórmula?

# Escreva um programa que leia três variáveis reais a, b, c, nesta ordem.
# Como saída, o programa deve imprimir o resultado da seguinte fórmula matemática:


# (a²+b²+c²)
# __________
#  (a+b+c)


# Arredonde os resultados com 07 casas decimais.

# dicas:

'''
1. Primeiro leia as variáveis, depois aplique a fórmula e, por fim, imprima o resultado.
2. Considere que a soma a + b + c nunca será igual a zero, ou seja, não terá divisão por zero
3. Dentro do comando print, use o comando round(x, n) para arredondar a resposta x com até n casas decimais.

'''
from math import*

# entrada:

# VAREAVEL A, PARA ARMAZENAR O VALOR DE A;
a = float(input())
# VAREAVEL B, PARA ARMAZENAR O VALOR DE B;
b = float(input())
# VAREAVEL C, PARA ARMAZENAR O VALOR DE C;
c = float(input())


conta = ( ( (a**2) + (b**2) + (c**2) ) / (a + b + c) )
resultado = round(conta, 7)

# saida:
print(resultado)