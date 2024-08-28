


'''
* Enunciado
Intervalo de valores
Considere dois números reais 
a e b, sendo b > a. Um número real x pertence ao intervalo [a,b] se a ≤ x ≤b.
Escreva um programa que leia os números reais 
x, a, b  nesta ordem.

Se  x pertencer ao intervalo, imprima a seguinte mensagem:
pertence
Caso contrário, imprima a seguinte mensagem:
nao pertence 
Se as entradas forem inválidas, ou seja, se 
b ≤ a, imprima a seguinte mensagem:
entradas invalidas

A validade das entradas segue a seguinte condição: b > a.
* Dicas
Note que as três entradas são números reais (float).
Utilize condições encadeadas (if/elif).
Alguns dos operadores booleanos (and, or, not) serão úteis.
Não confunda a vírgula que deve ser impressa (string) com a vírgula que separa um argumento de outro dentro da função print().'''


# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input())
a = float(input())
b = float(input())
if b > a:
	if a<= x <= b:
		print("pertence")
	else:
		print("nao pertence")
else:
	print("entradas invalidas")
