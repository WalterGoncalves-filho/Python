# EXERCICIO 2: 

# Enunciado
#Ração para Porquinho-da-índia
#Cleosméria comprou um saco de ração para porquinho-da-índia. 
#Ela alimenta diariamente alguns porquinhos com ração. 
#A quantidade diária de ração fornecida aos porquinhos é sempre a mesma.
#Escreva um programa que leia:
#O peso do saco de ração em gramas.
#A quantidade diária de ração em gramas.
#Como saída determine:
#A quantidade de ração (em gramas) que RESTARÁ no saco após uma semana.
#O valor de saída deve ser arredondado para três casas decimais.

#  LÓGICA: 

peso_racao_em_gramas = float(input(" O peso do saco de ração em gramas: "))
quantidade_diaria_de_racao = float(input(" A quantidade diária de ração em gramas:  "))
gasto_semanal = quantidade_diaria_de_racao*7
rest = peso_racao_em_gramas - gasto_semanal



#Saída: 

print(round(rest, 3))