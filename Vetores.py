#Exemplo 01: Programa que lê cinco números inteiros, armazena-os em um vetor e depois solicita ao usuário que escolha um número a mostrar.
"""
livro = [0,0,0]
cont = 0 

while cont < len(livro):
    escrita = input(f"Digite sua historia {cont + 1}:")
    livro[cont] = escrita 
    cont += 1

folha = int(input(f"Qual a folha será acessada? de 0 a {len(livro)-1 }"))
print(f"Folha Acessada:{folha} historia:{livro[folha]}")
"""
"""
a = []

for i in range(3):
    x = int(input("Digite elemento:"))
    a.append(x)

escolha = int(input(f"Digite um numero para selecionar o elemento atraves de seu indice de 0  a {len(a)-1}"))
print(f"O indice escolhido foi:{escolha} e o Elemento:{a[escolha]}")
"""
#Exemplo 02: Faça um programa que calcule a média aritmética dos valores armazenados no vetor L do exemplo anterior.
"""
vetor = [1,2,3,4,5]
soma = 0

for i in vetor:
    soma += i
    ma = soma/ len(vetor)

print(soma)
"""

#Exercício 03: Construa um programa que solicite e armazene em um vetor a nota de 10 estudantes. Em seguida, a partir do vetor em que os dados foram armazenados, 
#calcule a média aritmética da classe. Em seguida, imprima a quantidade de notas que estão acima da média calculada.
"""
estudantes = []
soma = 0

for i in range(5):
    x = int(input("Digite as notas dos estudantes:"))
    estudantes.append(x)

acima = 0 
abaixo = 0

for i in estudantes:
 
    soma += i
    ma = soma/len(estudantes) 

    if i > 7:
        acima += 1
    else:
        abaixo += 1

print(f"Media da classe{ma}")
print(f"Acima da média:{acima}")
print(f"Abaixo da média:{abaixo}")
"""
#Exercício 04: Desenvolva um algoritmo que leia 10 números inteiros armazenando-os em
#um vetor. Depois, crie outros dois vetores, um contendo apenas os números pares e o
#outro contendo apenas os números ímpares do vetor lido. Mostre então os três vetores: o
#original, o de pares e o de ímpares .
"""
num = []
par = []
impar = []

for i in range(6):
    x = int(input("Digite o valor desejado:"))
    num.append(x)


for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(num)

print(par)
print(impar)

"""


#Exercício 05: A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -
#8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim
#como a temperatura média.

"""
t = [-10, 8, 0, 1, 2, 5, -2, -4]
maior = t[0]  
menor = t[0] 


for valor in t:
    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print("Maior valor:", maior)
print("Menor valor:", menor)
"""