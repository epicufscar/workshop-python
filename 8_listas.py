# Exemplo Extra: 
# Imprimir os valores de uma lista

L = [1,2,3,4]

for i in L:
	print(i)

# Exemplo 5: 
# Faca um programa que, dada uma lista de valores, retorna o maior valor presente na lista.
lista = []
maior = -999
while True:
	n = input('digite um valor: ')
	if (n == 's'):
		break
	n = float(n)
	if (n > maior):
		maior = n
	lista.append(n)

print(maior)

# Exercicio 10: 
# Faca um programa que, dada uma lista de valores, calcula a soma dos valores da lista.
lista = []
soma = 0
while True:
	n = input('digite um valor: ')
	if (n == 's'):
		break
	n = float(n)
	soma = soma + n
	lista.append(n)

print(soma)

# Exercicio Extra 1:
# Faca um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def vogal(c):
	if(c == 'a'):
		return True
	elif(c == 'e'):
		return True
	elif(c == 'i'):
		return True
	elif(c == 'o'):
		return True
	elif(c == 'o'):
		return True
	else:
		return False
l = ['a','b','e','l','h','a']
v=0
c=0
for i in range(len(l)):
	if(vogal(l[i]) == True ):
		v+=1
	else:
		c+=1
print(v)
print(c)

# Exercicio Extra 2:
# Escreva um programa que, dada uma lista de valores listVal, gera duas novas listas,
# uma contendo todos os valores pares de listVal e outra contendo todos os valores impares.
lista = []
lista_impar = []
lista_par = []
while True:
	n = input('digite um valor: ')
	if (n == 's'):
		break
	n = float(n)
	lista.append(n)
	if(n % 2 == 0):
		lista_par.append(n)
	else:
		lista_impar.append(n)

# Exemplo 6:
# Leitura de uma matriz

mtz = [[1,2],[3,4],[5,6]]

l = int(input())
col = int(input())

matriz = []
for i in range(l):
	linhas = []
	for j in range(col):
		n = int(input())
		linhas.append(n)
	matriz.append(linhas)

print(matriz)
print(mtz)

# Exercicio 11:
# Soma de duas matrizes
mtz1 = [[1,2],[3,4]]
mtz2 = [[1,1],[1,1]]

linha = len(mtz1)
col = len(mtz1[0])
matrizR = []

for i in range(linha):
	somalinha = []
	for j in range(col):
		soma = mtz1[i][j]+mtz2[i][j]
		somalinha.append(soma)
	matrizR.append(somalinha)

print(matrizR)















