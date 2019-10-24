# Exemplo 8:
# Faca uma funcao que verifica se um numero eh par e retorna True, caso positivo, e False caso contrario

def par(x):
	if(x%2==0):
		return True
	else:
		return False


# Exercicio 17: 
# Construa uma funcao que desenhe um retangulo usando '*'. 
# Esta funcao deve receber dois parametros, linhas e colunas.
def ret(linha,col):
	for i in range(linha):
	  for j in range(col):
	    print('*',end='')
	  print()

# Exercicio 18: 
# Faca uma funcao que retorne o reverso de um numero inteiro informado. Por exemplo: 127 -> 721.
def reverso(n):
	i = 0
	while(n != 0):
		resto = n % 10
		n = n // 10
		print(resto,end='')

n = 8765
reverso(n)

# Exercicio 19: 
# Faça uma funcao, que verifica se um caractere eh vogal.
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
