# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
# - Imposto de Renda (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

q_h= float(input("Quantos você ganha por hora?"))
h_m = int(input('Qual o numero de horas trabalhadas no mês? '))
SB = q_h*h_m
IR = SB*(11/100)
INSS = SB*(8/100)
S= SB*(5/100)
#D=IR+INSS+S
D = SB-(SB*(0.24))
SL= SB-D
print("Salário Bruto: R${}".format(round(SB, 2)))
print("Imposto de Renda: R${}".format(round(IR, 2)))
print("Sindicato: R${}".format(round(S, 2)))
print("Salário Liquido: R${}".format(round(SL, 2)))