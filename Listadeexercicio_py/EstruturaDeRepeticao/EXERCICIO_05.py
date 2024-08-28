#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.

A = int(input())
B = int(input())
an = 0
while A < B:
    a = A*(3/100) + A
    b = B*(1.5/100) + B 
    A = a
    B = b
    an += 1   
print("Serão necessários {} anos aproximadamente para que a população do país A ultrapasse ou iguale a população do país B.".format(an))

