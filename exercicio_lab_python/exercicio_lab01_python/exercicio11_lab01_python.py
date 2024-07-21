# EXERCICIO 11:

#@Bilichilde é consultora de uma linha de cosméticos. 
#Seu lucro sobre o valor total de vendas é de 30%.
#Escreva um programa que leia o total de vendas de Bilichilde. 
#Como saída, determine o valor do lucro obtido (em reais) arredondado em duas casas decimais de precisão.

# DICAS: 

# Valores percentuais devem ser divididos por 100 antes de serem multiplicados por uma expressão.
#Os valores em reais devem ser arredondados em duas casas decimais de precisão.
#Dentro do comando print, use o comando round(x, 2) para arredondar a resposta x com até duas casas decimais.

# PARTE LÓGICA: 

total_de_vendas = float(input("Vendas? "))

lucro = total_de_vendas * 0.3

print(round(lucro, 2))