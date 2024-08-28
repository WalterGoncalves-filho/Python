# exercicio14: 
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

# LOGICA: 

peso = float(input("Digite o peso de peixes em quilos: "))
limite = 50 
if peso > limite:
    excesso = peso - limite
    valor_multa = excesso * 4

    print("O peso excedeu o limite estabelecido pelo regulamento de pesca do estado de Sao Paulo.")
    print(("O excesso de peso e:"), (round(excesso, 2)), ("quilos"))
    print(("Valor da multa a ser pago por Joao sera de: R$"), (round(valor_multa, 2)))
    
else:
    print("O peso de peixes esta dentro do limite estabelecido pelo regulamento de pesca.")
