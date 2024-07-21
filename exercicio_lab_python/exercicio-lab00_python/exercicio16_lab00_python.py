# EXERCICIO16:

#                   Enunciado

# IMPRESSÃO DE VÁRIAS EXPRESSÕES EM UMA SÓ CHAMADA:


'''

Elabore um programa que leia o ano corrente. Consulte o ano de fundação do IFAM (consulte o Google, se você não souber).
Qual o resultado do comando abaixo? Troque o YYYY pela variável que você leu na entrada e XXXX pelo ano de fundação do IFAM.
print("Em ",YYYY,"o IFAM completou", YYYY - XXXX, "anos de fundacao.")

'''
# DICAS:

'''
Nem todo traço é um sinal de subtração!
Alguns programas trocam o sinal de subtração por um travessão, e essa diferença é bem sutil. 
Por isso, digite você mesmo o sinal de subtração, para evitar erros.
Não use acentos.
Digite a mensagem exatamente como especificado, incluindo todos os caracteres de pontuação e respeitando o uso de maiúsculas e minúsculas.
'''
# ENTRDA:

an= int(input("digite o ano de fundacao do IFAM: "))
fun = 2008

# SAÍDA:

print ("Em ",an,"o IFAM completou", (an-fun), "anos de fundacao.")
