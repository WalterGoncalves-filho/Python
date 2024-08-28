# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a)o produto do dobro do primeiro com metade do segundo .
# b)a soma do triplo do primeiro com o terceiro.
# c)o terceiro elevado ao cubo.

# LOGICA 

inteiro1 = int(input('n inteiro:'))
inteiro2 = int(input("n inteiro2:"))
real = float(input('n real:'))

a = (2*inteiro1) * (inteiro2//2)
b = (3*inteiro1) + real 
c = (real)**3

# SAIDA: 

print("o produto do dobro do primeiro com metade do segundo e:", a)
print("a soma do triplo do primeiro com o terceiro e:", b)
print(("o terceiro elevado ao cubo e:"), (round(c)))