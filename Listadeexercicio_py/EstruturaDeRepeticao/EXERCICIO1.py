n = float(input("Digite uma nota, entre zero e dez: "))
while not 0<=n<=10: 
    print("INVÁLIDO!")
    n = int(input("Digite uma nota, entre zero e dez: "))
else:
    print("Obrigado!😁")