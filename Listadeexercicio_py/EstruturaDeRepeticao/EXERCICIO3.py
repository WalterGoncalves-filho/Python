#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
nome = input("DIGITE SEU NOME: ")
c=len(nome)
while c <= 3: 
    print("invalido")
    nome = input("DIGITE SEU NOME: ")
    c=len(nome)
else:   
    idade = int(input("DIGITE SUA IDADE: ")) 
    while 0 == idade or idade > 150:
        print("IDADE inválido!")
        idade = int(input("DIGITE SUA IDADE: "))
    else:
        salario = float(input('DIGITE SEU SALARIO: '))
        while salario<=0:
            print("SALARIO Inválido!")
            salario = float(input('DIGITE SEU SALARIO:'))
        else:
            sexo = str(input("DIGITE M, MASCULINO OU F, FEMININO: "))
            ALFA = "qwertyuiopasdghjklçzxcvbnQWERTYUIOPASDGHJKLÇZXCVBN"
            while sexo in  ALFA :
                print("SEXO Inválido!")
                sexo = str(input("DIGITE M, MASCULINO OU F, FEMININO: "))
            else:
                estadoc = str(input("DIGITE s',SOLTEIRO, 'c',CASADO, 'v', VIÚVO(a) e 'd', DIVORCIADO: "))
                ALFA = "qwertyuiopaghjklçzxbnQWERTYUIOPAGHJKLÇZXVBFMNmf"
                while estadoc in ALFA:
                    print("ESTADO CIVIL Inválido!")
                    estadoc = str(input("DIGITE s',SOLTEIRO, 'c',CASADO, 'v', VIÚVO(a) e 'd', DIVORCIADO: "))
                else:
                    print("DADOS VALIDADOS!")                      