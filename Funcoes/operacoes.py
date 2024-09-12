'''
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    if b != 0:
        divisao = a / b
        result = [soma, subtracao, multiplicacao, divisao]
        return result
    else:
        return "Error!"
    return 0
num_1 = int(input("Digite um número inteiro: \n"))
num_2 = int(input("Digite outro número inteiro: \n"))
calculo = operacoes(num_1, num_2)
print('{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {:.2f}'.format(num_1, num_2, calculo[0], num_1, num_2, calculo[1], num_1, num_2, calculo[2], num_1, num_2, calculo[3]))
'''
def operacoes(a, b):
    if b != 0:
        divisao = a / b
        soma = a + b
        subtracao = a - b
        multiplicacao = a * b
        result = [soma, subtracao, multiplicacao, divisao]
        return result
    else:
        print("Error!")   

num_1 = int(input("Digite um número inteiro: \n"))
num_2 = int(input("Digite outro número inteiro: \n"))
calculo = operacoes(num_1, num_2)
print(f'{num_1} + {num_2} = {calculo[0]}\n{num_1} - {num_2} = {calculo[1]}\n{num_1} * {num_2} = {calculo[2]}\n{num_1} / {num_2} = {calculo[3]:.2f}')

'''
def soma(a, b):
    soma = a + b
    return soma
def subtracao(a, b):
    subtracao = a - b
    return subtracao
def multiplicacao(a, b):
    multiplicacao = a * b
    return multiplicacao
def divisao(a, b):
    if b != 0:
        divisao = a / b
        return divisao
    return"Error"

a = int(input("Digite um numero inteiro: "))
b = int(input("Digite um numero inteiro: "))
print(f'{a} + {b} = {soma(a, b)}\n{a} - {b} = {subtracao(a, b)}\n{a} * {b} = {multiplicacao(a, b)}\n{a} / {b} = {divisao(a, b):.2f}')
'''










