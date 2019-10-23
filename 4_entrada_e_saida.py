# Exemplo 1:
# Faca um algoritmo que receba dois valores inteiros e some-os.
a = int(input())
b = int(input())
soma = a + b
print(soma)
print("A soma eh %d" %soma)

# Exercicio 1:
# Faca um algoritmo que receba dois valores inteiros e troque-os.
a = int(input())
b = int(input())
aux = b
b = a
a = aux
print(a)
print(b)

# Exercicio 2:
# Faça um programa que peca as 4 notas bimestrais e mostre a media.
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
media = (n1+n2+n3+n4)/4
print(media)

# Exercicio 3:
# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule o numero da sorte, dada a fórmula (4.42*altura) - 37
h = float(input())
nro = (4.42*h)-37
print(nro)
