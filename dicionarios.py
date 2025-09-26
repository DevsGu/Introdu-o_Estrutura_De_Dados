#📝 Exercício 1: Criação de Dicionário
#Crie um dicionário chamado pessoa com as seguintes informações:
#nome: "Ana"
#idade: 25
#cidade: "São Paulo"
#Depois, imprima:
#Todas as chaves,
#Todos os valores,
#Todos os itens (chave + valor).


"""
pessoa = {"nome":"ana" , "idade":25 , "cidade":"São Paulo"}
pessoa["Bairro"] = "Meireles"


for chave in pessoa.keys():
    print(chave)

for valores in pessoa.values():
    print(valores)

for valor in pessoa:
    print(pessoa[valor])

for chave in pessoa:
    print(chave)

for chave , valor in pessoa.items():
    print(chave , valor)
"""

#📝 Exercício 2: Acessando Valores
#Dado o dicionário produto:
#Acesse e imprima o valor da chave "preco".
#Atualize o valor da chave "estoque" para 100.


"""
produto = {'preco':100 , 'estoque':200}
print(produto['preco'])

produto['estoque']=100

print(produto)
"""

#📝 Exercício 3: Adicionando e Removendo
#Usando o dicionário produto:
#Adicione uma nova chave chamada "cor" com valor "azul".
#Remova a chave "estoque".


"""
produto = {'preco':100 , 'estoque':200}

#Adicionando Valor diretamente
produto['cor'] = 'azul'
print(produto)


#Deletando chave e valor diretamente
del produto['preco']
print(produto)

#Removendo a chave e capturando o valor
removendo_chave = produto.pop("estoque2" , "Valor não encontrado!")
print(removendo_chave)
"""

#📝 Exercício 4: Iterando sobre o Dicionário
#Crie um dicionário chamado aluno com informações de nome e uma lista de notas.
#Depois:
#Imprima todas as chaves e seus respectivos valores usando um loop for.


"""
aluno = {"nome":"Gilbert" , "notas":[8 , 9 , 10] }

for chave , valor in aluno.items():
    print(chave , valor)
"""

#📝 Exercício 5: Contando Palavras
#Dada uma lista de palavras:
#Crie um dicionário que conte quantas vezes cada palavra aparece na lista.



"""
palavras = ["mamao" , "abaixa" ,  "mamao" , "ameixa" , "mamao" , "jabuticaba"]

contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra]+= 1
    else:
        contador[palavra]=  1

print(contador)
"""

"""
palavras = ["joao" , "jose" , "joao" , "fabricio" , "verdum" , "clarisse" , "joao" , "jose", "jose"]
contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1
print(contador)
"""