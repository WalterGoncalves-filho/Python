# EXERCICIO 12: 


# Soraiadite foi a um posto de gasolina abastecer seu carro e trocar o óleo do motor. 
#O preço do litro da gasolina é R$2,86 e o serviço de troca de óleo foi R$50,00. Sobre o total de serviços realizados (abastecimento e troca de óleo), é aplicado um aumento de 34% referente ao ICMS (imposto sobre circulação de mercadorias e serviços).
#Escreva um programa que leia:
#a quantidade de litros abastecidos.
#Como saída, determine:
#o valor total a ser pago.
#O valor de saída deve ser arredondado para duas casas decimais.

# DICAS: 

#Verifique se as variáveis associadas ao problema são reais ou inteiras.
#Utilize o comando input() para realizar a leitura das entradas.
#Use o comando int() para converter a entrada de texto para um número inteiro e float() para converter uma entrada de texto para número real.
#A ordem de leitura das variáveis de entrada deve obedecer àquela explicitada no enunciado.
#A quantidade de entradas solicitadas em um programa determina a quantidade de comandos input(); e a quantidade de saídas determina a quantidade de comandos print().
#Use a função round(x,n) para arrendondar o número x para n casas decimais.
#Lembre-se que x% é igual x/100. Dado um valor total y, se quisermos calcular o valor de x% de y basta realizar a operação y * (x/100). Por exemplo, para calcular 25% do valor 240, fazemos 240 * (25/100) = 240 * 0,25 = 60.


# PARTE LÓGICA: 

quantidade_de_litros_abastecidos = float(input(" litros abastecidos? "))

preco_gasolina = 2.86

troca_de_oleo = 50.00

preco_total = (quantidade_de_litros_abastecidos*preco_gasolina)+(troca_de_oleo) 

total = preco_total + (preco_total*(34/100))




# SAÍDA: 


print(round(total, 2))