
# EXERCICIO 11:

"""
  As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
  Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  a. salários até R$ 280,00 (incluindo) : aumento de 20%
  b. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  c. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  d. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    1. o salário antes do reajuste;
    2. o percentual de aumento aplicado;
    3. o valor do aumento;
    4. o novo salário, após o aumento.
"""
s = float(input('Digite seu salário: '))
if s <=280.00:
  r0=s/0.2
  v0=r0-s
  print("salário antes do reajuste é de R${}".format(s))
  print("percentual de aumento aplicado foi de 20%.")
  print("o valor de aumento foi de R${}".format(round(v0, 2)))
  print("o novo salario apos o aumento é de R${}".format(round(r0, 2)))
elif 280.00<=s<=700.00:
  r1=s/0.15
  v1=r1-s
  print("salário antes do reajuste é de R${}".format(s))
  print("percentual de aumento aplicado foi de: 15%.")
  print("o valor de aumento foi de R${}".format(round(v1, 2)))
  print("o novo salario apos o aumento é de R$ {}".format(round(r1, 2)))
elif 700.00<=s<=1500.00:
  r2=s/0.10
  v2=r2-s
  print("salário antes do reajuste é de R${}".format(s))
  print("percentual de aumento aplicado foi de: 10%.")
  print("o valor de aumento foi de R${}".format(round(v2, 2)))
  print("o novo salario apos o aumento é de R${}".format(round(r2, 2)))
elif s>=1500.00:
  r3=s/0.05
  v3=r3-s
  print("salário antes do reajuste é de R${}".format(s))
  print("percentual de aumento aplicado foi de: 5%.")
  print("o valor de aumento foi de R${}".format(round(v3, 2)))
  print("o novo salario apos o aumento foi de R${}".format(round(r3, 2)))