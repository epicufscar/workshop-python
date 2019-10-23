# Exemplo 7:
# Faca um programa que, dada uma string, imprima o inverso dela.

stre = 'pessoas'
stri = ''
tam = len(stre)-1
for i in range(len(stre)):
	stri = stri+stre[tam-i]
print(stri)

# Exercicio 12: 
# Faca um programa que retire os espacos em brancos de uma string
mensagem = 'hoje dia 9 de outubro de 2019'
newm = ''
for i in mensagem:
	if (i != ' '):
		newm = newm+i
print(newm)

# Exercicio Extra 1: 
# Faca uma funcao, chamada ehPalindromo, que recebe como entrada uma palavra (string) 
# e identifica se ela eh um palindromo

stre = 'arara'
stri = ''
tam = len(stre)-1
for i in range(len(stre)):
	stri = stri+stre[tam-i]
print(stri)

if(stre == stri):
	print('s')
else:
	print('n')