#Enuciado:


'''
Movimento uniforme - pessoa no caminho
O movimento uniforme é o deslocamento que ocorre em linha reta e com velocidade constante, assim, percorre distâncias iguais em intervalos de tempos iguais. 
Nesse movimento, a posição varia com o tempo de forma uniforme. 
Com isso, é possível calcular a posição em que um objeto estará após um intervalo de tempo (t). 
Para tanto, devemos saber a sua posição inicial (S0) e a velocidade (v) com que esse corpo se desloca. Após ter identificado essas informações, basta utilizá-las na seguinte fórmula:

S=S0+vt
S - Posição Final do objeto

S0- Posição Inicial do objeto

v- Velocidade do objeto

t- Tempo de deslocamento

Com base nessas informações, escreva um programa que leia:
A posição inicial do objeto (m).
A velocidade do objeto (m/s).
O tempo de deslocamento (s).
Imagine que uma pessoa está a 1000 metros de distância da posição inicial. Como saída, imprima:

A posição final (S) do objeto.
‘Sim’ se objeto conseguir passar pela pessoa até o tempo de deslocamento ou ‘Nao’, caso a posição final seja menor que os 1000 metros.
'''

s0 = float(input())
v  = float(input())
t  = float(input())

s  = s0 + (v*t)

print(int(s))

if s > 1000:
	print("Sim")
else:
	print("Nao")