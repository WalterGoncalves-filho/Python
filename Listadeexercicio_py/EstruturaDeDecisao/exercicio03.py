# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("digite F para Feminino ou M para Masculino: ").upper()

if sexo == "F":
    print("sexo Feminino")
elif sexo == "M":
    print('sexo Masculino.');
else:
    print("sexo invalido!")
