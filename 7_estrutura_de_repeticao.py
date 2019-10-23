# Exemplo 3:
# Faca um programa que peca uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja invalido e continue pedindo
# ate que o usuario informe um valor valido. 
n = int(input())
while(n < 0 or n >10):
    print("Outra vez")
    n = int(input())

# Exemplo 4:
# Faca um programa que imprima os números pares no intervalo de 0 a 50, e mostre a soma dos numeros pares.
soma = 0
for i in range(0,50,2):
	print(i)
	soma+=i
print(soma)

# Exercicio 7: 
# Faca um programa que leia n numeros, dado pelo usuario e informe o maior numero e a quantidade de numeros digitados. O programa deve ler ate que o usuario digite 0

n = int(input())
maior = 1
i = 0
while(n != 0):
	i += 1
	if (n > maior):
		maior = n
	
	n = int(input())

print(i)
print(maior)

# Exercicio 8:
# Altere o programa anterior para mostrar no final a soma dos numeros.

n = int(input())
maior = 1
i = 0
soma = 0
while(n != 0):
	i += 1
	soma += n
	if (n > maior):
		maior = n
	
	n = int(input())

print(i)
print(maior)
print(soma)

# Exemplo 9:
# Faca um programa que dado um numero inteiro, mostre todos os seus divisores.
n = int(input())
i = 1
while(i<=n):
	if (n % i == 0):
		print(i)
	i = i + 1





	
