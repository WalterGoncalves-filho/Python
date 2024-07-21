#Enunciado: 
'''
CALCULADORA DE EMPRÉSTIMO VIP/COMUM
Desenvolva um programa para calcular o valor dos pagamentos mensais de um empréstimo, levando em consideração a condição VIP ou Comum do cliente. 
O programa deve receber como entrada uma string indicando o status do cliente ("V" para VIP e "C" para Comum) e o valor do empréstimo, e a saída deve ser o valor que o cliente pagará mensalmente por 2 anos (24 meses).
Se o status do cliente for "V" (VIP), aplique uma taxa de juros de 8% ao ano.
Se o status do cliente for "C" (Comum), aplique uma taxa de juros de 12% ao ano.

Entradas:

String informando qual o status do cliente ("V" para VIP ou "C" para Comum).
A string deve estar sempre em maiúscula; caso seja inserida em minúscula, converta-a para maiúscula.
O valor inteiro do empréstimo.

Saída:

Exiba o valor dos pagamentos mensais arredondada em duas casas decimais.

Formula:

P=r⋅PV1/(1+r)**-nt

Onde:

P é o pagamento mensal;
r é a taxa de juros mensal (taxa de juros anual dividida por 12);
PV é o valor do empréstimo;
nt é o numero total de meses
'''


def taxa(a, b):
	valor =( b * (a/12)) / (1 - (1 + a / 12)**-24)
	return valor
# a = taxa de juros
# b = valor do emprestimo
c_or_v = str(input()).upper()
emprestimo = int(input())

if c_or_v == "C":
	a = 0.12
else:
	a = 0.08
valor_emprestimo = taxa(a, emprestimo)
print("{:.2f}".format(valor_emprestimo))