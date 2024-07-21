# EXERCICIO 1: 


# O trabalhador de um banco brasileiro recebeu um cliente da Austrália, que possui apenas dinheiro em dólares australianos. O cliente pediu ao atendente do banco que trocasse todas os seus dólares australianos por reais.  Assim, ajude o atendente e escreva um programa que converta dólares australianos em reais. 
#Considere que 1 dólar australiano equivale a 3,22 reais. Dessa forma:
#valor Em Reais= valor EmDolares Australianos*3,22
#O seu programa deve:
#Ler um valor em dólares australianos na entrada;
#Calcular o equivalente em reais;
#Mostrar na tela o valor convertido com duas casas decimais.

# PARTE LÓGICA: 

valor_em_dolar = float(input(" Valor em dolar: "))

valor_em_reais = valor_em_dolar*3.22

# Saída: 

print(round(valor_em_reais, 2))





