'''
Enunciado
Boate
Em uma boate, o preço da entrada varia conforme o dia da semana. Nas segundas, terças e quintas, ela normalmente oferece um desconto de 25% sobre o preço normal de entrada. 
Porém, nos dias de músicas ao vivo, independentemente do dia da semana, é acrescida uma taxa fixa de R$20,00 ao preço da entrada.
Elabore um programa que calcule o preço final a ser pago para entrar na boate, a partir dos seguintes valores, nesta ordem:

O preço normal da entrada (em reais).
O dia da semana (1 para domingo, 2 para segunda, ..., 7 para sábado).
É dia de música ao vivo? (S ou N).
Validação dos dados de entrada
Note que:
O preço normal deve ser maior ou igual a zero.
Dias da semana só podem assumir valores inteiros de 1 a 7.
Música ao vivo só pode ser S ou N.
Se as entradas forem válidas, imprima o valor do ingresso arredondado para duas casas decimais.
Se o usuário inserir valores inválidos, imprima a mensagem "Dados invalidos":
'''


'''
domingo = 1
segunda = 2
terca = 3
quarta= 4
quinta = 5
sexta = 6
sabado = 7'''

'''domingo = 1
segunda = 2
terca = 3
quarta= 4
quinta = 5
sexta = 6
sabado = 7'''
dia_da_semana = [1, 2, 3 ,4 ,5 ,6, 7]

preco = float(input("Digite o preco da boate: "))
dia  = int(input("Digite o dia da semana com seu reespectivo numero da semana de 1 a 7: "))
m = str(input('É dia de musica ao vivo? ').upper())

musica = ["S", "N"]

if m in musica:
  	if m == "S":
	   if dia in dia_da_semana:
		   if dia == 2 or dia == 3 or dia == 5:
			   v =  (preco - (preco*0.25))+20
			   print("{:.2f}".format(v))
			else:
			   v = preco + 20
			   print("{:.2f}".format(v))
	   else:
		    print("Dados invalidos")
   elif m == "N":
	   if dia in dia_da_semana:
		    if dia == 2 or dia == 3 or dia == 5:
			   v = preco - preco*0.25
				print("{:.2f}".format(v))
		   else:
			   v = preco
				print("{:.2f}".format(v))
	   else:
		    print("Dados invalidos")
else:
	print("Dados invalidos")
