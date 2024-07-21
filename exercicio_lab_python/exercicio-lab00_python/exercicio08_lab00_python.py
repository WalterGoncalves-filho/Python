# EXERCICIO 8: 

# DIVISÃO INTEIRA E RESTO DA DIVISÃO
# Um grupo de três guerreiros derrotou um monstro que escondia 50 moedas de ouro. 
# Cada um vai receber a mesma quantia de moedas e o restante será pago a um informante que indicou o caminho até o covil do monstro.
# Escreva um programa que determine:
# Quantas moedas de ouro cada guerreiro receberá?
# Quantas moedas de ouro serão pagas ao informante?

# DICAS: 

# A divisão inteira – aquela cujo quociente não tem parte fracionária – é indicada por duas barras (//).
# O resto da divisão é indicado pelo sinal %. 
# Por exemplo, o resto da divisão de 9 por 4 é indicado por  9 % 4, cujo resultado é 1.
# O exemplo de saída abaixo fornece um modelo de formatação da saída, e não o valor da resposta esperada.

# DICAS: 
# A divisão inteira – aquela cujo quociente não tem parte fracionária – é indicada por duas barras (//).
# O resto da divisão é indicado pelo sinal %. 
# Por exemplo, o resto da divisão de 9 por 4 é indicado por  9 % 4, cujo resultado é 1.
# O exemplo de saída abaixo fornece um modelo de formatação da saída, e não o valor da resposta esperada.

# PARTE LÓGICA: 

tota_lde_moedas = int(50.0)
quantidade_de_guerreiros = 3
valo_a_ser_pago_para_o_informante = ( 50 % 3 )
valo_a_ser_pago_para_os_guerreiros = ( 50 // 3 )

# SAÍDA: 

print ( " O valor a ser distribuido aos 3 guerreiros é: " , valo_a_ser_pago_para_os_guerreiros, " moedas. " )
print (" O valor a ser pago ao informante é: " , valo_a_ser_pago_para_o_informante, " moedas. " )