# EXERCICIO 10: 

#Porcentagem é a razão entre um número e 100, e representamos essa razão pelo símbolo %. 
#Utilizamos essa razão para representar partes de algo inteiro. 
#Porcentagem envolve diversas situações com que nos deparamos frequentemente em nosso cotidiano, por exemplo em indicadores econômicos, resultados de pesquisas ou promoções".  
#Fonte: https://brasilescola.uol.com.br/matematica/porcentagem.htm

#______________________________________________________________________________________________________________

#Temos então que x% é uma razão que corresponde a x/100, ou seja, 18% é igual a 18/100.
#Dado um valor y, se quisermos calcular  x% de y basta realizar a operação y * (x/100).
#Por exemplo, para calcular 25% do valor 240, fazemos 240 * (25/100) = 240 * 0,25 = 60.
#Uma aplicação comum de porcentagem é na concessão de descontos ou no cálculo de multas.
#Se em dia de Black Friday uma loja concede um desconto de 85% em um produto com valor de R$ 200,00, o valor final do produto é seu valor original menos o desconto, que corresponde a 85% do valor original.
#valorFinal = 200,00 - 200,00*(85/100) = 30
#Se um cliente paga uma conta no valor R$ 130,00 com atraso e a multa é de 12%, o valor final a pagar será o valor da conta acrescido da multa, que corresponde a 12% do valor original.
#valorFinal = 130,00 + 130,00*(12/100) = 145,60
#Dadas as definições acima, faça um programa que tem como entrada:
#Um número real n.
#Seu programa deve:
#Calcular e imprimir  o valor de 27% do valor de entrada n arrendondado para 2 casas decimais. 
#Calcular e imprimir o valor de entrada n acrescido de 42% arrendondado para 2 casas decimais.
#Calcular e imprimir o valor de entrada n com um desconto de 63% arrendondado para 2 casas decimais.

#_________________________________________________________________________________________________________

# DICAS: 

#Verifique se as variáveis associadas ao problema são reais ou inteiras.

#Utilize o comando input() para realizar a leitura das entradas.
#Use o comando int() para converter a entrada de texto para um número inteiro e float() para converter uma entrada de texto para número real.
#A ordem de leitura das variáveis de entrada deve obedecer àquela explicitada no enunciado.
#A quantidade de entradas solicitadas em um programa determina a quantidade de comandos input(); e a quantidade de saídas determina a quantidade de comandos print().
#Use a função round(x,n) para arrendondar o número x para n casas decimais.

#___________________________________________________________________________________________________________


# PARTE LOGICA:

n = float(input("o valor n; "))

#__________________________________________________________________________________________________________

calculo1 = n*(27/100)
calculo2 = n+n*(42/100)
calculo3 = n-n*(63/100)

#SAÍDA: 

print(round(calculo1, 2))
print(round(calculo2, 2))
print(round(calculo3, 2))