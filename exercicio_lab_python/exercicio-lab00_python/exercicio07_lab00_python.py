# EXERCICIO 7:


#ARREDONDAMENTO
#Seis amigos foram a um restaurante. A conta deu R$ 250, a ser repartida igualmente para cada um.
#Escreva um programa que imprima o valor que cada um tem que desembolsar.
#O resultado deve ser apresentado com, no máximo, duas casas decimais, indicativas dos centavos.

# DICAS: 

# Use a função round(x, n) para arredondar um número x com até n casas decimais de precisão.
# A função round() apenas arredonda. 
# Se você deseja imprimir um resultado com arredondamento, então deve usá-la dentro da função print().
# O exemplo de saída abaixo fornece um modelo de formatação da saída, e não o valor da resposta esperada.


# PARTE LÓGICA: 

total_da_conta = 250.00
total_de_amigos = int(6)
valor_a_ser_pago_por_cada_um = ( total_da_conta / total_de_amigos )


# SAÍDA: 



print(round(valor_a_ser_pago_por_cada_um, 2))


