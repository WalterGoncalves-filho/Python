#Enunciado:

'''
É múltiplo de 2?
Elabore um programa que leia um número inteiro. Se ele for múltiplo de 2, então imprima a mensagem "sim". Caso contrário, imprima "nao".

Observe que as linhas 5, 7, 9 e 12 contêm erros. Corrija-os e submeta o programa ao CodeBench.

Atenção para a grafia das palavras: todas as letras do resultado devem ser minúsculas. Não use acentos.

'''
num = int(input("Digite um numero: "))
if num % 2 == 0:
	mensagem = "sim"
else:
	mensagem = "nao"
print(mensagem)
