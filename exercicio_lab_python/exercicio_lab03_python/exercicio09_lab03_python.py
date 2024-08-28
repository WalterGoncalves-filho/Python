'''
Função J
Considere a seguinte função f(x):


      ⎧    −1      
      ⎪  ________   , se −1000 ≤ x < −2
      ⎪  (x + 2)
      ⎪
f(x) =⎨
      ⎪    1
      ⎪ ________   , se 2 <x ≤ 1000
      ⎪  (X - 2) 
      ⎩

Faça um programa que leia o valor de x e retorne o valor de f(x) baseado na definição acima. 
Imprima saída com 4 casas decimais (use a função round()).
Observe que a função não está definida para todos os valores reais. 
Caso o usuário entre como um valor de x que não pertence ao domínio da Função, o programa deve gerar como saída a mensagem ‘entrada invalida’.

Dicas
Atenção para o uso de caracteres maiúsculos e minúsculos. Não use acentos, para evitar erros.
Alguns dos operadores booleanos (and, or, not) serão úteis.
Use a função round(x, n) para arredondar um número x com até n casas decimais de precisão.
'''

x = float(input())
if  -1000 <= x < -2:
	v  = -1 * (1/(x+2)) 
	print(round(v, 4))
elif 2 < x <= 1000:
	v  = (1/(x-2))
	print(round(v, 4))
else:
	print("entrada invalida")
