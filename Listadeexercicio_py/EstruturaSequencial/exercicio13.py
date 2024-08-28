# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# LOGICA:

h = float(input('altura:'))
para_homens = (72.7*h) - 58
para_mulheres = (62.1*h) - 44.7

# SAIDA: 

print("o respectivo peso para homens:", para_homens)
print("respectivo peso para mulheres", para_mulheres)

