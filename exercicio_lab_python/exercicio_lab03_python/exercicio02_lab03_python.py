"""
* Enunciado
Acesso VIP
Desenvolva um programa para auxiliar os participantes de um evento a descobrirem se o código que escolheram é o código para acesso VIP, o enigmático código 190. O funcionamento do programa deve ser o seguinte:

Receba como entrada um código numérico digitado pelo usuário.
Compare o código digitado com o código para acesso VIP.
Se o código digitado for igual a 190, mostre na tela a mensagem: “vip”.
Se o código digitado for menor que 190, mostre na tela a mensagem: “menor”.
Por fim, se o código digitado for maior que 190, apresente na tela: “maior”.
 * Dicas
Implemente a estrutura condicional (if-elif-else) para avaliar as diferentes situações;
Utilize os operadores de comparação (==, <, >) para verificar as relações entre os números.

"""


vip = 190
n= int(input())
if n > vip:
	print("maior")
elif n<vip:
	print('menor')
elif n==vip:
	print('vip')
