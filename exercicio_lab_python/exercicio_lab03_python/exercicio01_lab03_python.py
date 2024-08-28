'''
* Enunciado
Pedra, Papel e Tesoura
Codifique um programa que leia um número inteiro N como entrada, e imprima a seguinte saída:

“Pedra”, se N for positivo;
“Papel”, se N for negativo;
“Tesoura”, em caso contrário.

Note que a saída deve imprimir uma única mensage

* Dicas
Note que a ordem dos “ifs/elifs” do seu código não necessariamente será a mesma ordem da sequência de testes mostrada no enunciado.

* CASO DE TESTES: 

Entrada	:
--> 333
Saída	:
--> Pedra
Entrada	:
--> 0
Saída	:
--> Tesoura
Entrada	:
--> -1245
Saída	:
--> Papel
'''

n=int(input())

if n > 0:
	print("Pedra")
elif n<0:
	print("Papel")
else:
	print("Tesoura")




