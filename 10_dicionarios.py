# Exercicio 13:
# Crie um dicionario que contenha seu nome como chave e sua idade como valor.
minha_idade = {}
minha_idade["Claucio"] = 21
print(minha_idade)

# Exercicio 14:
# Crie um dicionario que contenha seu nome e o nome dos seus pais como chave e a quantidade de letras de cada nome como valores
meus_pais = {}
meus_pais["Claucio"] = 7
meus_pais["Roselene"] = 8
meus_pais["Claucio Filho"] = len("Claucio Filho")
print(meus_pais)

# Exercicio 15:
# A partir dessa lista L = ["Caio", "Amanda", "Claucio",  "Epic"] crie um dicionario onde as chaves sao itens de L e os valores sao as o tamanho dos itens.
L = ["Caio", "Amanda", "Claucio",  "Epic"] 
tamanho = {}
for i in L:
    tamanho[str(i)] = len(i)
print(tamanho)


# Exercicio 16:
# A partir dessa lista  L = [1,2,3,1,3,2,2,2,4] crie um dicionario que conta quantas vezes cada item de L se repete.
L = [1,2,3,1,3,2,2,2,4]
conta = {}
for i in L:
    if i in conta:
        conta.update({i:conta[i]+1})
    else:
        conta.update({i:1})
print(conta)