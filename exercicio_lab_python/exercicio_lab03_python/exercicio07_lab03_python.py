
'''
Enunciado
Calculando a área do triângulo
Escreva um programa que leia as medidas dos três lados A, B e C de um triângulo qualquer.
Em seguida, ele deve verificar se as medidas são válidas (condição de existência de um triângulo).
Se as medidas forem válidas o programa deve calcular a área do triângulo.

Dados de entrada:

1. Lado A.

2. Lado B.

3. Lado C.

Como saída, se as entradas forem válidas, o programa deve imprimir o valor da área arrendodando com três casas decimais.
Caso contrário, o programa deve imprimir a mensagem "invalida".

Lembre-se de que as condições de existência de um triângulo são:

1. Todos os lados devem ser positivos.

2. A medida de qualquer um dos lados deve menor que a soma das medidas dos outros dois

Leia as dicas caso ainda tenha alguma dúvidas em como verificar as condições em que os três valores representam medidas válidas de um triângulo.

Dicas
O programa fornecido está incompleto. Substitua as expressões ___COMPLETE AQUI___ por comandos que façam o programa executar corretamente.
A solução proposta adota os seguintes passos:
Ler o valor de cada lado do triângulo: A, B, C.
Verificar se todos os valores fornecidos são positivos.
Se verdade, verificar se as medidas fornecidas correspondem às de um triângulo, ou seja, se a soma dos dois lados menores é maior que o lado maior.
O teste deve ser verdadeiro para todas as três combinações possíveis de lados.
Se todos os testes forem bem sucedidos, calcule a área e exiba a mensagem.
Se pelo menos um teste falhar, apresente a mensagem de erro.
Execute o programa para todos o casos de teste apresentados.
'''

from math import *
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
# if ___COMPLETE AQUI___ :
if a > 0 and b> 0 and c>0:
  #if___COMPLETE AQUI___  :
	if (a + b) > c and (a + c) > b and (b+c) > a :
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		print(round(area, 3))
	else:
		print("invalida")
else:
	print("invalida")
