
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

print(f"Pergunta do jogador 1:\n{pt1}")
print(f'Dica da pergunta: {dica}')
print("\n\n")

palpite1 = str(input("Informe seu palpite: "))
print("")


while palpite1 != gabarito1:
    if palpite1 != gabarito1:
        print("resposta invalida.tente novamente!")
        palpites1.append(palpite1)
        palpite1 = str(input("Informe seu palpite: "))
        print("")
    else:
        break

if palpite1 == gabarito1:
    print(f"Parabéns {jogador_1} voçê acertou!")
    palpites1.append(palpite1)




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

print(f"Pergunta do jogador 2:\n{pt2}")
print(f'Dica da pergunta: {dica}')

palpite2 = str(input("Informe seu palpite: \n"))
print("")


while palpite2 != gabarito2:
    if palpite2 != gabarito2:
        print("resposta invalida.tente novamente!")
        palpites2.append(palpite2)
        palpite2 = str(input("Informe seu palpite: \n"))
        print("")
    else:
        break

if palpite2 == gabarito2:
    print(f"Parabéns {jogador_2} voçê acertou!")
    palpites2.append(palpite2)


print("")

print(f"A quantidade de palpites do {jogador_1} : {len(palpites1)}")
print(f"Palpites do {jogador_1}:\n{palpites1}")
print("\n")

print(f"A quantidade de palpites do {jogador_2}: {len(palpites2)}")
print(f"Palpites do {jogador_2}:\n{palpites2}")
print("\n")

if len(palpites1) > len(palpites2):
    print(f"{jogador_1} Venceu!")
elif len(palpites1) < len(palpites2):
    print(f"{jogador_2} venceu!")
else:
    print("EMPATE!!\n")


