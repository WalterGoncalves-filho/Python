# Faça um programa que leia 5 números e informe o maior número.
a, b, c, d, e = map(int, input().split())
maior = [a, b, c, d, e]
maior = max(maior)
print(maior)
