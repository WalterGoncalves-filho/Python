# Faça um programa que leia 5 números e informe a soma e a média dos números.
a, b, c, d, e = map(int, input('Digite 5 números separados por espaços: ').split())
soma = a+b+c+d+e
media= int(soma/5)
print("A soma desses números é: {} e média desses números é: {}".format(soma, media))
