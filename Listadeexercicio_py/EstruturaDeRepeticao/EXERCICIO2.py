n = str(input("Digite seu nome de usuário: "))
s = str(input("Digite sua senha: "))
while s==n:
    print("Sua senha não pode ser a mesma que o nome de Usuário!")
    n = str(input("Digite seu nome de usuário: "))
    s = str(input("Digite sua senha: "))
else:
    print("Logado!")