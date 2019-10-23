# Exemplo 2:
# Faca um Programa que leia tres numeros e mostre o maior deles.
a = int(input())
b = int(input())
c = int(input())

if (a >= b and a >= c):
	maior = a
else:
	if(b >= c):
		maior = b
	else:
		maior = c
		
print(maior)

# Exercicio 4:
# Faca um Programa que verifica se o numero eh par.
n = int(input())

if(n % 2 == 0):
	print('par')
else:
	print('impar')

# Exercicio 5:
# Faça um Programa que leia tres numeros e mostre-os em ordem decrescente
a = int(input())
b = int(input())
c = int(input())

if (a >= b and a >= c):
	maior = a
	if(b >= c):
		medio = b
		menor = c
	else:
		medio = c
		menor = b
elif(b >= a and b>=c):
	maior = b
	if(a >= c):
		medio = a
		menor = c
	else:
		medio = c
		menor = a
elif(c >= a and c>=b):
	maior = c
	if(a >= b):
		medio = a
		menor = b
	else:
		medio = b
		menor = a

print(menor,medio,maior)

# Exercicio 6:
# Faca um programa que calcule as raizes de uma equaçao do segundo grau, na forma ax2 + bx + c.
# O programa devera pedir os valores de a, b e c e fazer as consistencias, informando ao usuario nas seguintes situacoes:
# 1. Se o usuario informar o valor de A igual a zero, a equacao nao eh do segundo grau e o programa nao deve fazer pedir os demais valores, sendo encerrado;
# 2. Se o delta calculado for negativo, a equacao nao possui raizes reais. Informe ao usuario e encerre o programa;
# 3. Se o delta calculado for igual a zero a equacao possui apenas uma raiz real; informe-a ao usuario;
# 4. Se o delta for positivo, a equacao possui duas raiz reais; informe-as ao usuario;


a = int(input())
b = int(input())
c = int(input())

delta = b**2 - (4*a*c) 

if(a == 0):
	print('nao da')
elif(delta < 0):
	print('<0')
elif(delta == 0):
	x1 = (-b + delta**2)/(2*a)
	print(x1)
else:
	x1 = (-b + delta**2)/(2*a)
	x2 = (-b - delta**2)/(2*a)
	print(x1)
	print(x2)







