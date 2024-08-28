# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps). 
#Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print('Qual o tamanho do seu arquivo? ')
T  = float(input('>>'))
print('E qual a velocidade da sua internet? ')
V = float(input('>>'))

# transforma a velocidade de bits para bytes 
v = V/8

# calculo do tempo em segundos
t = T / v
t = int(t)
# converter o tempo em segundos para minutos

print(f'o tempo PROXIMADO do download é de {t} minutos.')
