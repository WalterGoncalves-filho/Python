# enunciado:
'''
Paga ou não paga passagem?
Elabore um programa que leia a idade de uma pessoa (número inteiro). O programa deve verificar se a pessoa vai pagar ou não a passagem com base nas seguintes regras:

Se ela tiver 2 anos ou mais, então imprima a mensagem paga.
Caso contrário, imprima nao_paga.
'''

idade = int(input())
if idade >= 2:
	print("paga")
else:
	print("nao_paga")