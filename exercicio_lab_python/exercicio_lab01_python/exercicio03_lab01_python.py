#Exercicio3: 
# Agora, Estanislau deseja comprar vários jogos para seu console favorito. 
# Em um mesmo site, o preço do jogo é sempre o mesmo para todos os títulos. O valor do frete é diferente para cada site.
# Escreva um programa que leia as seguintes entradas, nesta ordem:
# 1: A quantidade de jogos a serem encomendados;
# 2: O valor unitário de cada jogo;
# 3: O valor do frete
# Como saída, determine o preço total a ser pago por Estanislau pelos jogos que for encomendar do site, incluindo o valor do frete.

# Quanditade jogos encomendados:

quant = int(input('Quantidade de jogos a serem encomendados: '))

# Valor unitário de cada jogo: 

var = float(input("Valor Unit. de cada jogo: "))

# Valor do frete: 

frete = float(input('Valor do Frte: '))

# Total:

total =  (quant*var)+frete

#saída: 
print (total)