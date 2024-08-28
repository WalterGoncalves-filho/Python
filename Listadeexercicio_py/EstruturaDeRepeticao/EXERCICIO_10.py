# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

a, b = map(int, input("Digite dois números interiros de 0 a 100 separados por espaços: ").split())
if 0<= a <= 100 and 0 <= b <= 100:
    if a > b:
        a, b = b, a
    '''while a < b:
        a+=1
        print(a, end=" ")
    '''
    for a in range(a+1, b):
        print(a, end=" ")











