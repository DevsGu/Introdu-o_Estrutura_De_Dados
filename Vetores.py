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
#Exercício 06: Desenvolver um programa que leia dez elementos numéricos de um vetor A.
#Construir um vetor B do mesmo tipo, observando a seguinte lei de formação: se o valor do
#índice do vetor A for par, o valor deve ser multiplicado por 5; sendo ímpar, deve ser
#somado com 5. Ao final, mostrar o conteúdo dos vetores A e B.

"""
a = []
b = []
for i in range(6):
    x = int(input("Digite elemento:"))
    a.append(x)

for i , e in enumerate(a):
    if i % 2 == 0:
        b.append(e*5)
    
    else:
        b.append(e+5)

print(a)
print(b)
"""

#❑Exercício 07: Desenvolver um programa que leia cinco elementos numéricos inteiros de um
#vetor A. No final, apresentar o total da soma de todos os elementos do vetor A que sejam
#ímpares..
"""
a = [1,2,3,4,5]
soma = 0

for i in a:
    if i % 2 != 0:
        soma += i
    
print(a)
print(f"Soma dos imapares:{soma}")

"""
#❑Exercício 08: Elaborar um programa que efetue a leitura de dez nomes de pessoas e
#armazene em um vetor, apresente-os sem seguida.
"""
pessoas = []

for i in range(5):
    x = str(input("Digite o nome das pessoas:"))
    pessoas.append(x)

print(pessoas)
"""

#❑Exercício 9: Elaborar um programa que leia oito elementos inteiros em um vetor A.
#Construir um vetor B de mesma dimensão com os elementos do vetor A multiplicados por 3.
# O elemento B[1] deve ser implicado pelo elemento A[1]*3, o elemento B[2] implicado
#pelo elemento A[2]*3 e assim por diante, até 8. Apresentar o vetor B.
"""
a = [1,2,3,4,5,6,7,8]
b = []

for i in a:
    b.append(i * 3)

print(a)
print(b)
"""
#Exercício 10: Escrever um programa que leia dois vetores (denominados A e B) com 20
#elementos reais. Construir um vetor C, sendo cada elemento do vetor C a subtração de um
#elemento correspondente do vetor A com um elemento correspondente do vetor B, ou
#seja, a operação de processamento deve estar baseada na operação C[i] = A[i] - B[i]. Ao
#final, apresentar os elementos do vetor C.

"""
a = [10,9,8,7,6]
b = [1,2,3,4,5]
c = []

for i in range(5):
    c.append(a[i]-b[i])

print(c)
"""

#Exercício 11: Elaborar um programa que leia 15 elementos inteiros de um vetor A.
#Construir um vetor B de mesmo tipo, observando a seguinte lei de formação: "todo
#elemento do vetor B deve ser o quadrado do elemento do vetor A correspondente".
#Apresentar os elementos dos vetores A e B.

#Feito Com For
"""
a = [1,2,3,4,5]
b = []

for i in a:
    b.append(i * i)

print(a)
print(b)
"""
#Feito com Lista Comprehesion
"""
a = [1,2,3,4,5]
b = [i ** 2 for i in a]

print(a)
print(b)
"""

#Exercício 12: Elaborar um programa que leia um vetor A com 3 elementos inteiros.
#Construir um vetor B de mesmo tipo, e cada elemento do vetor B deve ser o resultado do
#fatorial correspondente de cada elemento do vetor A. Apresentar os vetores A e B.
"""
a = [1,2,3,4,5]
b = []

for i in a:
    fat = 1
    for j in range(i):
        fat *= j + 1
    b.append(fat)

print(a)
print(b)
"""

#❑Exercício 13: Construir um programa que leia dois vetores A e B com 15 elementos inteiros
# cada. Construir um vetor C, sendo este o resultado da junção dos vetores A e B. Desta
#forma, o vetor C deve ter o dobro de elementos em relação aos vetores A e B, ou seja, o
#vetor C deve possuir 30 elementos. Apresentar o vetor C.
"""
a = [1,2,3]
b = [4,5,6]
c = []

c = a + b

print(c)
"""
#Exercício 14: Elaborar um programa que leia 10 elementos do tipo real em um vetor A e
#construir um vetor B de mesma dimensão com os mesmos elementos armazenados no
#vetor A, porém de forma invertida. Ou seja, o primeiro elemento do vetor A passa a ser o
#último do vetor B, o segundo elemento de A passa a ser o penúltimo de B, e assim por
#diante. Apresentar os elementos dos vetores A e B.
"""
a = list(range(1 , 10 + 1  , 1))
b = []

b.append(a[::-1])
print(a)
print(b)
"""
#❑Exercício 15: Escrever um programa que leia três vetores (A, B e C) com cinco elementos
#cada que sejam do tipo real. Construir um vetor D, sendo este o resultado da junção dos
#três vetores (A, B e C). Desta forma, o vetor D deve ter o triplo de elementos dos vetores A,
#B e C, ou seja, 15 elementos. Apresentar os elementos do vetor D.
"""
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = []

d = a + b + c + d

print(d)
"""

#Exercício 16: Elaborar um programa que leia um vetor A com 10 elementos inteiros.
#Construir um vetor B do mesmo tipo e dimensão do vetor A, sendo cada elemento do vetor
#B o somatório de 1 até o valor do elemento correspondente armazenado no vetor A. Se o
#valor do elemento do vetor A[1] for 5, o elemento correspondente do vetor B[1] deve ser
#15, pois o somatório do elemento do vetor A é 1+2+3+4+5. Apresentar os elementos do
#vetor B.
"""
a = [1,2,3,4,5]
b = []

for i in a:
    soma = 0
    for j in range(i):
        soma += j + 1
    b.append(soma)

print(a)
print(b)
"""
#Exercício 17: Elaborar um programa que leia um vetor A com dez elementos inteiros
#positivos. Construir um vetor B do mesmo tipo e dimensão, em que cada elemento do
#vetor B deve ser o valor negativo do elemento correspondente do vetor A. Desta forma, se
#em A[1] estiver armazenado o elemento 8, deve estar em B[1] o valor –8 e assim por
#diante. Apresentar os valores dos vetores A e B.
"""
a = [1,2,3,4,5]
b = []

for i in a:
    b.append(i * -1)

print(a)
print(b)
"""
#❑Exercício 18 Elaborar um programa que leia um vetor A com dez elementos inteiros.
#Construir um vetor B de mesmo tipo, em que cada elemento deve ser a metade de cada
#um dos elementos existentes no vetor B. Apresentar os elementos dos vetores A e B.
"""
a = [1,2,3,4,5]
b = []

for i in a:
    b.append(i / 2)

print(a)
print(b)
"""
#Exercício 19: Construir um programa que calcule a tabuada de um valor qualquer de 1 até
#10 e armazene os resultados em um vetor A. Apresentar os elementos do vetor A.
"""
a = []
n = int(input("Digite a tabuada desejada:"))

for i in range(11):
    a.append(n * i)

print(a)
"""

#Exercício 20: Elaborar um programa que leia 10 elementos (valores reais) para
#temperaturas e graus Celsius e armazene esses valores em um vetor A. O programa ao final
#deve apresentar a menor, a maior e a média das temperaturas lidas.
"""
temp = [18,30,45,12,20]
maior = 0 
menor = 1000
soma = 0 


for i in temp:
    soma += i
    if maior < i:
        maior = i
    if i < menor:
        menor = i

ma = soma / len(temp)


print(maior)
print(menor)
print(f"Média:{ma}")
"""
