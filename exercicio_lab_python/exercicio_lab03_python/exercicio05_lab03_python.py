'''
* Enunciado
Planos Saúde Mais
A empresa de planos de Saúde "Saúde Mais" está lançando uma campanha para incentivar famílias a aderirem aos seus serviços.
Para isso, estão oferecendo descontos progressivos para famílias com mais membros. 
Eles aplicam os seguintes descontos:

Número de membros da família	| Desconto
            1                   |  Nenhum
            2                   |   15%
            3                   |   25%
            4 ou mais           |   35%
Escreva um programa que leia:

O valor do plano de saúde mensal individual, em R$ (float).
O número de membros da família que vão aderir ao plano  (int).
Como saída, determine o valor do plano de saúde mensal total da família com o desconto aplicado.
'''



valor  = float(input())
n_m = int(input())

if n_m == 1:
	d = 0 * valor
elif n_m == 2:
	d = 0.15 * valor
elif n_m == 3:
	d = 0.25 * valor
elif n_m >= 4:
	d = 0.35 * valor
	
desconto = n_m *( valor - d)
print("R$ {}".format(desconto))
