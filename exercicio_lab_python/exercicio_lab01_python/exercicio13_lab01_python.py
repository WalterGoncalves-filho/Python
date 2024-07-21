#   ENUNCIADO:

#                               Temperatura na cidade de Manaus.

# Na cidade de Manaus, setembro de 2023 foi o mês mais quente do ano. 
# Uma medição durante 6 dias aferiu os seguintes valores: 28,3; 27,5; 29,8; 38,3; 39,3; 32,2 graus celsius. 
# A menor temperatura do período foi 27,5 graus celsius e a maior temperatura foi 39,2 graus  celsius.
# Curiosidade: O maior valor de temperatura é o maior já registrado no mês, nos últimos 33 anos, ele supera os 39,0 °C registrado em 21/09/2015.
# Agora, escreva um programa que leia 6 (seis) valores de temperatura e como saída imprima a menor temperatura e a maior temperatura registradas no período.

# dicas: 

# 1. Leia os seis valores um de cada vez usando as funções  float() e input() para ler um valor digitado via teclado e atribua cada um à uma variável.
# 2. Use as funções min() e max() para encontrar a menor e a maior temperatura
# 3. As quantidades de entradas solicitadas em um programa determina a quantidade de comandos input(); e a quantidade de saídas determina a quantidade de comandos print().
# 4. Verifica a formatação da saída antes de submeter.


#  LÓGICA:


print("Digite as 6 temperaturas:")

temperatura1 = float(input('-->'))
temperatura2 = float(input('-->'))
temperatura3 = float(input('-->'))
temperatura4 = float(input('-->'))
temperatura5 = float(input('-->'))
temperatura6 = float(input('-->'))

temperatura_minima = min(temperatura1,temperatura2,temperatura3,temperatura4,temperatura5,temperatura6)
temperatura_maxima = max(temperatura1,temperatura2,temperatura3,temperatura4,temperatura5,temperatura6)

# SAIDA: 

print("Temperatura Minima:",(temperatura_minima),'graus celsius.')
print('Temperatura Maxima:',(temperatura_maxima),"graus celsius.")