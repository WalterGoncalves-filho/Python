#Enunciado:
'''
Empréstimo do seu Madruga
Seu Madruga estava sempre inadimplente com o seu Barriga. Para poder pagar o aluguel, ele precisa fazer um empréstimo para quitar suas dívidas e não ser despejado. 
Escreva um programa que avalie a capacidade do Seu Madruga de efetuar o pagamento da prestação do empréstimo.
Escreva um programa que leia:
O valor da renda do seu Madruga.
O valor da prestação que ele pode pagar por mês.
Se o valor da prestação for maior que 20% da renda, imprima a mensagem “Emprestimo nao aprovado”. Caso contrário, imprima a mensagem “Emprestimo aprovado”.
'''

valor_r = float(input("digite os respectivos valores:"))
valor_p = float(input("digite os respectivos valores:"))

if valor_p > (0.2*valor_r):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")