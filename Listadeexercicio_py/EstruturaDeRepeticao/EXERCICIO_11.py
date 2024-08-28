# Altere o programa anterior para mostrar no final a soma dos números.


a, b = map(int, input("Digite dois números interiros de 0 a 100 separados por espaços: ").split())
if 0<= a <= 100 and 0 <= b <= 100:
    if a > b:
        a, b = b, a
    soma = 0
    for a in range(a,b+1):
        soma += a
    print(soma)











