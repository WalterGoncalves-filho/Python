def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    if b != 0:
        divisao = a / b
        result = [soma, subtracao, multiplicacao, divisao]
        return result
    else:
        print("error!")
    return 0
num_1 = int(input("Digite um número inteiro: \n"))
num_2 = int(input("Digite outro número inteiro: \n"))
calculo = operacoes(num_1, num_2)
print('{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {:.2f}'.format(num_1, num_2, calculo[0], num_1, num_2, calculo[1], num_1, num_2, calculo[2], num_1, num_2, calculo[3]))
