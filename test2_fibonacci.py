# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence 
# ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

print("Este programa identifica se o numero faz parte da sequencia de Fibonacci.\n\n")
n = int(input(f"Insira um número: "))
print("-"*50)

f1 = 0
f2 = 1
f3 = 0

while f3 < n:
    f3 = f1 + f2
    f1 = f2
    f2 = f3

if f3 == n:
    print(f"O Numero {n} FAZ parte da sequencia Fibonacci.")
else:
    print(f"O Numero {n} NAO FAZ parte da sequencia Fibonacci.")