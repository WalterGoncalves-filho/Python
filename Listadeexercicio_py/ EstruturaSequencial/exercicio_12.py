# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
# (72.7*altura) - 58
# LOGICA:

altura =  float(input("digite sua altura:"))
peso = (72.7 * altura)-58

# SAIDA: 

print(("seu peso e:"), (round(peso, 2)))