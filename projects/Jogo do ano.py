#pergunta = "Em que ano o Brasil conquistou o pentacampionato no futebol?"

palpites1 = []
# jogador_1 = str(input("Informe o nome do jogador 1: "))
# pt1 = str(input("Informe a pergunta a ser feita: "))
# gabarito1 =  str(input("Informe seu gabarito: "))
# dica = str(input("Informe sua dica: "))

jogador_1 = 'joe'
pt1 = 'trans'
gabarito1 =  'filme'
dica =  'coisa de ver'

pular = "\n"
print(100*pular)

palpite1 = ""


print(pt1)
print(dica)


while palpite1 != gabarito1:
    palpite1 = str(input("Informe seu palpite: "))
    palpites1.append(palpite1)
    print("resposta invalida.tente novamente!")


if gabarito1 == palpite1:
    print(f"Parabéns {jogador_1} voçê acertou!")


#==================================================================

palpites2 = []
print(2*"\n")
# jogador_2 = str(input("Informe o nome do jogador 2: "))
# pt2 = str(input("Informe a pergunta a ser feita: "))
# gabarito2 =  str(input("Informe seu gabarito: "))
# dica = str(input("Informe sua dica: "))
jogador_2 = 'WALTER'
pt2 = 'v e f '
gabarito2 =  '10'
dica = 'carecas'

pular = "\n"
print(100*pular)

print(pt2)
print(dica)

palpite2 = ""

while palpite2 != gabarito2:
    palpite2 = str(input("Informe seu palpite: "))
    palpites2.append(palpite2)
    print("resposta invalida.tente novamente!")

if gabarito2 == palpite2:
    print(f"Parabéns {jogador_2} voçê acertou!")


print("\n")

print(f"A quantidade de palpites do {jogador_1} é de {len(palpites1)}")
print(f"Palpites do {jogador_1}:\n{palpites1}")
print("\n")

print(f"A quantidade de palpites do {jogador_2} é de {len(palpites2)}")
print(f"Palpites do {jogador_2}\n{palpites2}")
print("\n")

if len(palpites1) > len(palpites2):
    print(f"O jogador {jogador_1} Venceu!")
elif len(palpites1) < len(palpites2):
    print(f"O jogador {jogador_2} venceu!")
else:
    print("EMPATE!!\n")


