
# Faça um Programa que leia três números e mostre o maior e o menor deles.

nun0 = float(input("digite um numero: "));
nun1 = float(input("digite um outro número: "));
nun2 = float(input("digite mais um número: "));

maior = max(nun0, nun1, nun2);
menor = min(nun0, nun1, nun2);

print("o maior número é:", maior);
print("O menor número é:", menor);