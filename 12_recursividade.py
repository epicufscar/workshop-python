# Exemplo 9:
# Fatorial iterativo
def fatorial_ite(num):
    if(num == 0):
        return 1
    else:
        resultado = 1
        for i in range(1, num+1):
            resultado *= i
        return resultado

# Exemplo 10:
# Fatorial recursivo
def fatorial_rec(num):
    if(num == 0):
        return 1
    else:
        return num * fatorial_rec(num-1)

# Exercicio 20:
# Faca uma funcao recursiva que recebe como entrada um inteiro n e retorna o enesimo numero da sequencia de Fibonacci.
def fibo(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)