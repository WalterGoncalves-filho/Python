# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

#TAXA DE "A" 3%
#TAXA DE "B"1.5%

A = 80000
B = 200000
an = 0
while A < B:
    a = A*(3/100) + A
    b = B*(1.5/100) + B 
    A = a
    B = b
    an += 1   
print("Serão necessários {} anos aproximadamente para que a população do país A ultrapasse ou iguale a população do país B.".format(an))

