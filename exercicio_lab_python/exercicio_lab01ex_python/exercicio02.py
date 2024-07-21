# Exercicio 02:


#                                           Enunciado

# Polpa de frutas:

# Michael comprou alguns litros de polpa de frutas, com o objetivo de doar dois terços a uma instituição de caridade e ficar com um terço.
# Escreva um programa que leia quantos litros foram comprados.
# Como saída, apresente a quantidade que ficará com Michael.
# Arredonde os valores com até 03 casas decimais de precisão.


# DICAS :

"""
1. Dentro do comando print, use o comando round(x, 3) para arredondar a resposta x com até três casas decimais.
2. Observe qual o tipo de entradas e saídas esperadas: real ou inteiro? Por exemplo, é possível comprar 2,5 litros ou apenas quantidades inteiras?
3. Use a função round(x, n) para arredondar um número x com até n casas decimais de precisão.

"""

# ENTRADA:
litrs = float(input())

# PARTE LOGICA:
result = litrs * (1/3)

# SAIDA:
resultado = round(result, 3)
print(resultado)