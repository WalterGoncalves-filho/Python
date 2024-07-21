#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
#Não utilize a função de potência da linguagem.

b  = int(input('Digite o valor da base: '))
ex = int(input('Digite o valor do expoente: '))
a = 1
for x in range(abs(ex)):
    a = a*b
if ex < 0:
    a = f'1/{a}' 
print('{} elevado a {} = {}'.format(b, ex, a))