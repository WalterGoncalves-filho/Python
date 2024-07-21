# Faça um Programa que leia três números e mostre-os em ordem decrescente. 
# vareável do 1° número!
nun0 = int(input("digite um numero: "));
# vareável do 2° número!
nun1 = int(input("digite um outro número: "));
# vareável do 3° número!
nun2 = int(input("digite mais um número: "));

# Estrutura conticional:

# condição em que a 3° variável é a MAIOR e que a 1° variável é a MENOR!
if nun2 > nun1 > nun0:
    print("1°", nun2)
    print("2°", nun1)
    print("3°", nun0);
# condição em que a 3° variável é a MAIOR e que a 2° variável é a MENOR!
elif nun2> nun0 > nun1:
    print("1°", nun2)
    print("2°", nun0)
    print("3°", nun1);
# condição em que a 1° variável é a MAIOR e que a 3° variável é a MENOR!
elif nun0 > nun1 > nun2:
    print("1°", nun0)
    print("2°", nun1)
    print("3°", nun2);
# condição em que a 1° variável é a MAIOR e que a 2° variável é a MENOR!
elif nun0 > nun2 > nun1:
    print("1°", nun0)
    print("2°", nun2)
    print("3°", nun1);
# condição em que a 2° variável é a MAIOR e que a 1° variável é a MENOR!
elif nun1 >nun2> nun0:
    print("1°", nun1)
    print("2°", nun2)
    print("3°", nun0);
# condição em que a 2° variável é a MAIOR e que a 3° variável é a MENOR!
else:
    print("1°", nun1)
    print("2°", nun0)
    print("3°", nun2);
