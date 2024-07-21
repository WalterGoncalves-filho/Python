"""
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

1. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
2. A mensagem "Reprovado", se a média for menor do que sete;
3. A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""

nota0 = float(input("digite a sua nota parcial: "))
nota1 = float(input("Digite a sua segunda nota parcial: "))

media = (nota0 + nota1)//2

resultado = round(media, 1)

if resultado == 10.0:
    print("Aprovado com Distinção!");
elif resultado >= 7 < 10:
    print("Aprovado!");
elif resultado < 7.0:
    print("Reprovado!");
else:
    print("Erro! Digite Novamente!");