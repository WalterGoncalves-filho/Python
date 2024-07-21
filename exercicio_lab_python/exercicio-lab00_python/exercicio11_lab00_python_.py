# EXERCICIO 11: 

# POTENCIAÇÃO
# área A de um hexágono regular, de aresta a, é dada por:
# A=3/2√3a**2
# Escreva um programa que calcule e imprima o valor da área de um hexágono de 5 cm de aresta, aplicando a fórmula acima.
# Exiba o resultado com até quatro casas decimais de precisão.

# DICAS: 

# Em Python, a potenciação é indicada por dois asteriscos (**). Por exemplo, 4 ** 3 equivale a 4³.
# Para extrair a raiz n de um número x, eleve o número x ao expoente 1/n. Por exemplo, a raiz quadrada de x é indicada por (x)**0.5.
# Use a função round(x, n) para arredondar um número x com até n casas decimais de precisão.
# A função round() apenas arredonda. 
# Se você deseja imprimir um resultado com arredondamento, então use a função round()dentro da função print().
# O exemplo de saída abaixo fornece um modelo de formatação da saída, e não o valor da resposta esperada.
  
# PARTE LÓGICA: 

a = int(5.0)
raiz = (3)**0.5
A = 3/2* raiz *a**2
 
# SAÍDA: 

print(round(A, 4))
