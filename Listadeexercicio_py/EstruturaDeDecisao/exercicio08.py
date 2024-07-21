#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar.
#sabendo que a decisão é sempre pelo mais barato.


preco0 = float(input("Digite o preço do primeiro produto: "));
preco1 = float(input("Digite o preço do segundo produto: "));
preco2 = float(input("Digite o preço do terceiro produto: "));

barato = min(preco0, preco1, preco2);

if barato == preco0:
    print("Escolha o 1° produto!");
elif barato == preco1:
    print("Escolha o 2° produto!");
else:
    print("Escolha o 3° produto!");