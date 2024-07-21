# EXERCICIO 16: 
                                                # ENUNCIADO: 

# Como o Google Maps calcula a distância entre dois pontos na superfície da Terra?
# A superfície da Terra é curva. Por isso, o teorema de Pitágoras não pode ser utilizado para calcular a distância entre dois pontos sobre a superfície da Terra.
# Seja (ti, gi) a latitude e longitude de um ponto Pi na superfície da Terra. A distância d entre dois pontos P1 e P2, em km, é dada por
# d = R.arccos(sen(t1).sen(t2)+cos(t1).cos(t2).cos(g1−g2))
# onde R = 6371,01 km é o raio médio da Terra.
# Escreva um programa que leia as seguintes informações, medidas em graus:
# 1. A latitude t1 de um ponto P1.
# 2. A longitude g1 de um ponto P1.
# 3. A longitude g2 de um ponto P2.
# Como saída, determine a distância d, em quilômetros, com duas casas decimais de precisão.

# dicas: 

# 1. Use as seguintes funções do módulo math:
 # °seno: sin()
 # °cosseno: cos()
 # °arco-cosseno: acos()
# 2. Use a função round(x, n) para arredondar um número x com até n casas decimais de precisão.
# 3. No exemplo abaixo, as entradas estão em graus.
# 4. Funções trigonométricas em Python trabalham em radianos. Por isso, use a função radians() para transformar as latitudes e longitudes de graus para radianos. Exemplo:
# ang = radians(float(input("Angulo: ")))

from math import radians, sin, acos, cos

# ENTRADA E LOGICA: 

t1 = radians(float(input('Latitude do p1:')))
g1 = radians(float(input('Longitude do p1:')))
t2 = radians(float(input('Latitude do p2:')))
g2 = radians(float(input('longitude do p2:')))

R = 6371.01

d = R*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
resultado = round(d, 2)

# SAÍDA:

print("A distância em quilômetros é de", resultado, '.')