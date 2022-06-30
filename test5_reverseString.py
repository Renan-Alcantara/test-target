#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

#----------------------------------------------------------------------------------------------------------------------------

string = input("Insira uma linha de texto para reverte-la: ")
str = string
str_reverse = []
loc = len(str)

while loc > 0:
    str_reverse += str[loc-1]
    loc = loc - 1
print(''.join(str_reverse))