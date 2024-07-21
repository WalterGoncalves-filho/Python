#Enunciado;

'''
Fertilização aérea
A empresa de aviação agrícola Agro Fértil oferece um serviço de aplicação de fertilizantes. O custo do serviço depende da área da plantação a ser fertilizada e obedece a seguinte regra:

Se a área a ser fertilizada for de 10 mil hectares ou menos, o custo é de R$ 5,00 por hectare.
Se a área a ser fertilizada tiver mais do que 10 mil hectares, o custo total é de R$ 5,00 por cada um do 10 mil hectares iniciais, mais R$ 4,00 por hectare excedente.
Escreva um programa que leia:

a área a ser fertilizada (em hectares).
Como saída, determine:

o valor total a ser cobrado pela empresa Agro Fértil. 
O valor de saída deve ser arredondado com até duas casas decimais.
'''



area = float(input())
if area <= 10000:
	custo = 5.0*area
else:
	execedente = area-10000
	custo= 5.0*10**4 + execedente * 4 
print("{:.2f}".format(custo))