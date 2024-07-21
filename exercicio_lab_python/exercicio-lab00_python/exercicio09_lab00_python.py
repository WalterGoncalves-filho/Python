# EXERCICIO 9: 

# EXPRESSÕES ARITMÉTICAS
# Qual o valor da expressão abaixo? Escreva um programa que imprima o valor dessa expressão no console.
# 30 - 3 ** 2 + 8 // 3 ** 2 * 10

# DICAS: 

# No teclado, o sinal de subtração é o mesmo sinal do hífen, localizado ao lado da tecla do zero. Porém, vários outros sinais se parecem com o traço da subtração. 
# Para evitar um erro devido à semelhança de sinais, digite você mesmo o sinal de subtração em vez de copiar e colar.
# A ordem de precedência das operações é a mesma que aprendemos na Matemática. Da esquerda para a direita, vale a seguinte prioridade, na ordem em que aparecem:
# Operações contidas entre parênteses.
# Potenciações.
# Multiplicações, divisões e restos de divisão.
# Adições e subtrações.

# PARTE LÓGICA: 

potencia  = (3**2)
expressao = 30 - (potencia) + (8 // (potencia)*(10))


print( expressao)

