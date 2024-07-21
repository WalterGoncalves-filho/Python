# EXERCICIO14: 

#                                                      Enunciado:
# Média ponderada
# Escreva um programa que leia quatro notas de um aluno. 
# Como saída, imprima a média ponderada, sabendo que os pesos das avaliações são respectivamente: 1, 2, 3 e 4.
# Arredonde os resultados com até 02 casas decimais de precisão.

# dicas: 

# 1. Dentro do comando print, use o comando round(x, 2) para arredondar a resposta x com até n casas decimais.
# 2. Verifique o tipo das entradas: as notas são valores inteiros ou reais?

# LOGICA E ENTRADA: 

print('digite as notas do aluno:')

n1 = float(input('-->'))
n2 = float(input('-->'))
n3 = float(input('-->'))
n4 = float(input('-->'))

media_ponderada = (   (n1*1) + (n2*2)+ (n3*3) + (n4*4) ) / ( 1 + 2 + 3 + 4 ) 

# SAIDA: 

print('A média de nota do aluno foi:',(round(media_ponderada, 2)),'!')