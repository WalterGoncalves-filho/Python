'''
* Enunciado
Festa das Corujas
Corujas de uma floresta decidiram se reunir para uma festa. Cada uma delas possui o seu número de identificação, para ter o acesso liberado na entrada. Se o número for divisível por 2 e por 3 ao mesmo tempo, a coruja tem entrada normal. Se for divisível apenas por 2, a entrada é VIP. Números que não atendem a nenhum desses requisitos indicam intrusos que estão tentando entrar na festa.

Faça um programa que leia um número inteiro, referente à identificação de uma coruja. Deve aparecer na tela "normal" se ela tem entrada normal, "vip" se tem entrada vip e "intruso" para aqueles que não se encaixam em nenhum dos requisitos.

 * Dicas
Um número qualquer x será divisível por outro número y se x % y for igual a 0;
Utilize a estrutura condicional (if-elif-else);
Lembre-se de que o condicional elif deve ser utilizado quando o if for falso e tivermos outra condição a ser estabelecida;
Quando necessário, utilize operadores lógicos como and, or e not.
'''


n = int(input())

a = n%2
b = n%3

if a == 0 and b==0:
    print("normal")
elif a == 0 and b !=0:
    print("vip")
else:
    print("intruso")
