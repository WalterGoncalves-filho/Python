# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# o codigo pode ser feita de 2 maneiras!

vocabulario = input("digite uma letra do alfabeto: ")

# Alfabeto o na string única:


vogal  = "aeiou"
consoante = "qwrtypsdfghjklzxcvbnmç"

if vocabulario in vogal or vocabulario in vogal.upper():
    print("a letra", [vocabulario], "é uma vogal!");
elif vocabulario  in consoante or vocabulario in consoante.upper():
    print("a letra", [vocabulario], "é uma consoante!"); 
else:
    print("invalido! Digite novamente!");



#   Alfabetos separados, um em  cada string: 

"""

if vocabulario == "a":
    print("a letra digitada é uma vogal!"); 
elif vocabulario == "e":
   print("a letra digitada é uma vogal!");
elif vocabulario == "i":
    print("a letra digitada é uma vogal!");
elif vocabulario == "o":
    print("a letra digitada é uma vogal!");
elif vocabulario == "u":
    print("a letra digitada é uma vogal!");
elif vocabulario == "A":
    print("a letra digitada é uma vogal!");
elif vocabulario == "E":
    print("a letra digitada é uma vogal!");
elif vocabulario == "I":
    print("a letra digitada é uma vogal!");
elif vocabulario == "U":
    print("a letra digitada é uma vogal!");
elif vocabulario == "O":
    print("a letra digitada é uma vogal!");
elif vocabulario == ("b"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("B"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("c"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("C"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("d"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("D"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("f"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("F"):
   print("a letra digitada é uma consoante!");
elif vocabulario == ("g"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("G"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("h"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("H"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("j"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("J"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("k"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("K"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("l"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("L"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("m"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("M"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("N"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("N"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("p"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("P"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("q"):
   print("a letra digitada é uma consoante!");
elif vocabulario == ("Q"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("r"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("R"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("s"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("S"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("t"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("T"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("v"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("V"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("w"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("W"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("x"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("X"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("y"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("y"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("z"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("Z"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("ç"):
    print("a letra digitada é uma consoante!");
elif vocabulario == ("Ç"):
    print("a letra digitada é uma consoante!");
else:
    print("Inválido! Digite novamente!");

"""