# exercicio 15:

                                                  # Enunciado:


            # Distância entre objetos


# A distância entre as duas árvores pode ser calculada pelo observador usando a lei dos cossenos:



# c = ((a**2)+(b**2)-(2*a*b)*(cosy))**0.5
# Faça um programa que tenha como entrada, nessa ordem:
# 1. a distância "a" entre o observador e a primeira árvore.
# 2. a distância "b" entre o observador e a segunda árvore.
# 3. o angulo γ" entre "a" e "b" (em graus).
# Como saída, seu programa deverá imprimir, com duas casas decimais, o valor de c, correspondente à distância entre as duas árvores.


# ENTRADA E LOGICA: 


from math import radians, cos

print('digitre os respectivos valores de "a, b e â":')
a = float(input('valor de a:'))
b = float(input('valor de b:'))
â = float(input('valor do â:'))

x = radians(â)
c = (  (a**2) +( b**2)-(2*a*b) * (cos(x)))**0.5

resultado = round(c, 2)

# SAÍDA:

print("A distância entre as duas árvores é de",resultado,'metros.')