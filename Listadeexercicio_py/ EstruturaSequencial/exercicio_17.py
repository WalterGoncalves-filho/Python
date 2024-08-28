# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


a = float(input("Qual o tamanho em metros quadrados da área a ser pintada?"))
pl = 80
pg= 25
cl = 18
cg = 3.6
col = 6
f = 0.1
area_com_folga = a * f
litros_necessarios = area_com_folga / cl

#situação1
preco_latas = round(litros_necessarios / cl) * pl
print(f"Situação 1: Comprar apenas latas de 18 litros: Preço total: R$ {preco_latas:.2f}")

#situação2
preco_galoes = round(litros_necessarios / cg) * pg
print(f"Situação 2: Comprar apenas galões de 3.6 litros: Preço total: R$ {preco_galoes:.2f}")

#situação 3
latas_inteiras = litros_necessarios // cl
litros_restantes = litros_necessarios % cl
galoes_necessarios =round(litros_restantes / cg)
preco_latas_galoes = (latas_inteiras * pl) + (galoes_necessarios * pg)
print(f"Situação 3: Misturar latas e galões: Preço total: R$ {preco_latas_galoes:.2f}")

