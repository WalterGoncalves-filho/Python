# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = input("Em que turno você estuda?Digite \"M\" para MATUTINO,\"V\", para VESPERTINO e \"N\", para NOTURNO: ")

vespertino = "v"
matutino = "m"
noturno = "n"

if turno in matutino or turno in matutino.upper():
    print("Bom Dia!");
elif turno in vespertino or turno in vespertino.upper():
    print("Boa Tarde!");
elif  turno in noturno or turno in noturno.upper():
    print("Boa Noite!");
else: 
    print("Valor Inválido!")   