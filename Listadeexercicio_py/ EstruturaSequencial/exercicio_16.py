# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

A_p = float(input("Qual o tamanho em metros quadrados da área a ser pintada?"))
l=A_p//3
latas = l//18.0
pr = latas*80.0
if l <= 18:
    print("Você precisará comprar uma lata de tinta.")
    print("Você pagaraá somente R$80.00.")
else:
    print("Você precisará comprar {} latas de tinta.".format(int(latas)))
    print("Você pagará somente R${}".format(pr))