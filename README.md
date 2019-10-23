# Workshop Python Iniciante

Repositório destinado ao Workshop de Python para Iniciantes (utilizando Python 3). Aqui estarão as respostas para os exercícios (quando forem liberadas), e um guia (README.md) para a instalação, sintaxe, etc.

## Instalando o Python

Existem várias maneiras de programar em Python. Aqui citaremos 3 delas, assim como suas vantagens e desvantagens.

### IDE Online (recomendado para iniciantes)

Uma IDE Online é um ambiente de programação direto do seu navegador. Nela podemos escrever nossas linhas de código e rodá-lo, gerando a saída como qualquer outro método. Além disso, muitas IDEs auxiliam o programador, sugerindo o que possivelmente está sendo escrito, tornando a programação mais simples e rápida.

* Vantagens: fácil de acessar, auxílio na programação e execução do código, não depende de instalação
* Desvantagens: dependente de internet
* Como acessar: https://repl.it/languages/python3

### IDE (recomendado para iniciantes)

Uma IDE é um ambiente de programação instalado em seu computador. Possui todas as funcionalidades de uma IDE online (na maioria das vezes, possui mais funcionalidades ainda) e não depende da internet.

* Vantagens: auxílio na programação e execução do código, não depende de internet
* Desvantagens: pode ser um pouco pesada, necessita de instalação
* IDEs recomendadas:
    1. PyCharm: https://www.jetbrains.com/pycharm/
    2. Spyder: https://www.spyder-ide.org/

### Editor de Texto + Terminal (não recomendado para iniciantes)

Favorita de muitos computeiros, essa é a maneira raiz de programar! Nela, utilizamos um editor de texto para escrever o código e o terminal para executá-lo.

* Vantagens: geralmente bastante leve, não depende de internet
* Desvantagens: funcionalidades dependem do editor de texto, necessita conhecimentos de comandos do terminal, mais difícil de instalar
* Como instalar o Python (para utilizar no terminal): 
    1. Windows: https://python.org.br/instalacao-windows/
    2. Linux: https://python.org.br/instalacao-linux/
    3. Mac OS X: https://python.org.br/instalacao-mac/
* Editores de texto recomendados:
    1. Visual Studio Code: https://code.visualstudio.com/
    2. Sublime Text: https://www.sublimetext.com/

## Sintaxe

Aqui estão as características e regras de boa parte da sintaxe da linguagem Python.

### Variáveis

Variáveis são os valores que são manipulados em um programa. Nelas, armazenamos os dados.
Em Python, utilizamos o ```=``` para fazer uma atribuição.

Porém, nem tudo pode ser uma variável. Devemos seguir as seguintes regras de nomeação:
* O nome não deve começar com números
* Acentos não devem ser utilizados
* Há diferença entre letras maiúsculas e minúsculas
* Não pode usar nomes reservados da linguagem (como ```for``` e ```while```, por exemplo)
* Não pode ter espaço em branco

Exemplo:
```python
numero = 42
nome = "Jorge"
```

### Tipos de Dado

A linguagem Python possui tipagem dinâmica, isso significa que o interpretador infere o tipo de dado que uma variável recebe. Assim, não precisamos declarar se a variável é um número inteiro, número real, string, etc.
Exemplo:
```python
# Int (numero inteiro)
valorInteiro = 777

# Float (numero real)
valorReal = 10.25

# String (texto)
exString = "Arrasou"

# Boolean (verdadeiro ou falso)
valorVerdadeiro = True
valorFalso = False
```

### Entrada de Dados

* Utilizamos a função ```input()```.
* O valor retornado por essa função é sempre uma string.
* Para outros tipos de dados é preciso fazer uma conversão:
    1. Int: ```int(input())```
    2. Float: ```float(input())```

Exemplo:
```python
texto = input("Digite um texto: ")
numero = int(input("Digite um numero: "))
```

### Saída de Dados

Utilizamos a função ```print()```.
Exemplos:
```python
print(var)
print("A soma de", a, "+", b, "eh igual a", soma)
print("Geeks : % 2d, Portal : % 2f" %(1, 5.333))
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print(f"aaa {soma}")
```

### Operadores Aritméticos

| Operador | Descrição       |
| :------: | :-------------: |
| +        | Adição          |
| -        | Subtaração      |
| *        | Multiplicação   |
| /        | Divisão         |
| //       | Divisão Inteira |
| **       | Exponenciação   |
| %        | Módulo          |

### Operadores Relacionais

| Operador | Descrição      |
| :------: | :------------: |
| ==       | Igual          |
| !=       | Diferente      |
| >        | Maior          |
| >=       | Maior ou Igual |
| <        | Menor          |
| <=       | Menor ou Igual |

### Operadores Lógicos

| Operador | Descrição |
| :------: | :-------: |
| or       | Ou        |
| and      | E         |
| not      | Não       |

### Estrutura Condicional (if)

É uma estrutura que possibilita a escolha de um grupo de ações a serem executadas quando determinadas condições são ou não satisfeitas (controla o fluxo do programa).

> **Importante**
> Sempre se atente à indentação (espaços ou tabs antes dos comandos) para que o interpretador saiba a execução correta!

```python
if(condicao1): 
    # Satisfaz condicao1
    x = 1
elif(condicao2):
    # Nao satisfaz condicao1 mas satisfaz condicao2
    x = 2
else:
    # Nao satisfaz condicao1 nem condicao2
    x = 777
```

### Estruturas de Repetição

São estrutura que permitem executar mais de uma vez o mesmo comando ou conjunto de comandos, de acordo com uma condição ou com um contador.

>  **Importante**
>   Sempre se atente à indentação (espaços ou tabs antes dos comandos) para que o interpretador saiba a execução correta!

#### While (enquanto)

* Executa o bloco **enquanto** a condição for verdadeira
* É preciso de uma variável para poder auxiliar nas iterações, o **incrementador**
* Geralmente, o número de iterações é desconhecido

```python
while(condicao):
    # Acoes a serem executadas enquanto condicao for True
```

#### For (para)

* Faz interações sob uma sequência
* Range(x,y) gera uma sequência crescente de valores entre x e y-1
* É utilizado quando sabemos o número de vezes que o código será repetido

```python
for valor in sequencia:
    # Acoes a serem executadas dentro dessa sequencia

for i in range(0, 3):
    print(i)
# Imprimira 0 1 2
```

### Listas

São sequências ou coleções ordenadas de valores. Cada valor na lista é identificado por um índice, começando por 0.

```python
# Declarando uma lista
Lista = [1, 2, 3, 4, 5]
#        0  1  2  3  4  (indices)

# Criando uma lista vazia
L = []

# Acessando uma posicao da lista (indice 2)
Lista[2] 

# Modificando um elemento da lista
Lista[2] = 8

# Copiando listas
L = Lista[:]
L = Lista.copy()
```

#### Funções para Listas

```python
# Retorna o tamanho de uma lista
len(Lista)

# Adiciona um elemento a lista
Lista.append(valor)

# Remove um elemento da lista
Lista.remove(valor)

# Fatiamento de lista (da posicao x a y-1)
Lista[x:y]

# Pertencimento
valor in Lista

# Inserir um elemento em uma determinada posicao
Insert(pos, valor)
```

#### Listas de Listas

* Para percorrer os elementos utiizamos dois laços de repetição: um fica fixado na linha e o outro percorre as colunas

```python
# Declarando a matriz
# 1 2 3
# 4 5 6
# 7 8 9
matriz = [[1,2,3],[4,5,6],[7,8,9]]

Linha_i_coluna_j = matriz[i][j]

matriz[1][2] = 3 # Atribuicao de valor a um elemento

# Impressao dos elementos de uma matriz
for linha in matriz:
    for coluna in linha:
        print(coluna)
```

### Strings

São sequências de caracteres, geralmente utilizadas para representar palavras, frases ou textos de um programa.
Em Python, possuem as seguintes características:
* São imutáveis, a não ser que as transformemos em uma lista
* São delimitadas por aspas, duplas ```""``` ou simples ```''```
* Podemos acessar elemento como nas listas
* Alguns métodos de listas também são válidos para strings

#### Métodos Úteis para Strings

```python
# Separacao de strings de acordo com um caractere ded referencia
mensagem = 'Popcorntime, Netflix, Telecine'
mensagem.split(',') # Imprimira ['Popcorntime', ' Netflix', ' Telecine']

# Conversao de string em lista
mensagem.list()
```

### Dicionários

Dicionário é uma estrutura de dado do tipo Chave:Valor, em que cada Valor pode ser acessado pela sua Chave.

```python
Dic  = {"Um": 1, "Dois":2, "Tres":3}
Idade = {"Maria": 21, "Joao": 30, "Ana":30}
```

#### Funções Úteis para Dicionários

```python
# Criar dicionario vazio
dic = {}

# Inserindo elementos no dic
dic["Carlos"] = 30

# Modificando um elemento do dicionario
dic.update({"Maria":10}

# Tamanho do dicionario
len(dic)

# Acessando itens (valores)
dic["nome_da_chave"]

# Remover do dic
del dic["chave"]

# Acessando os valores
dic.values()

# Acessando todas as tuplas
dic.items()

# Acessando todas as chaves
dic.keys()
```

#### Tipos de dados

Dicionários podem armazenar uma grande variedade de tipos de dados: Inteiros, Reais, Strings, etc.
Porém, além disso, podem armazenar, também, Listas como valores:

```python
L=[1,2,3]
Idades.[“Lista”] = L
print(Idades)
# Sera printado {'Maria': 21, 'Joao': 30, 'Ana': 30, 'lista': [1, 2, 3]}
```

Também é possível armazenar outros dicionários!

```python
Dic = {'dic1’: {'Maria': 21, 'Joao': 30, 'Ana': 30}, 'dic2': {'um': 1, 'dois': 2}}
```

### Funções

Uma função é uma sequência de instruções que computa um ou mais resultados que chamamos de parâmetros.
Em Python, as funções possuem as seguintes características:
* A ordem dos argumentos tem que ser a mesma
* Podem não receber nenhum parâmetro
* São definidas no início do código, como boas práticas
* A função só é executada quando é chamada
* Uma função pode chamar outra função

> **Importante**
> Sempre se atente à indentação (espaços ou tabs antes dos comandos) para que o interpretador saiba a execução correta!

```python
def funcao(parametro1, parametro2):
    
    # Corpo da funcao

    return valor # Valor que a funcao retorna (pode nao retornar nada)

# Chamando a funcao
valor = funcao(argumento1, argumento2)
```

### Recursividade

Quando uma função invoca a si mesma, acontece o que chamamos de **recursividade** (ou recursão).
A recursividade simplifica a programação, permitindo códigos mais limpos e enxutos, muitas vezes facilitando o entendimento e manutenção do programa.
Em contrapartida, loops recursivos, na maioria das vezes, consomem bastante memória e demoram mais para serem executados que soluções iterativas.

#### Exemplo: Fatorial

Primeiramente, vamos lembrar o que é o fatorial:

*Na matemática, o fatorial de um número natural n, representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n.*

Por exemplo, vamos calcular o fatorial de 4:
```4! = 4*3*2*1 = 24```

Além disso, é importante ressaltar que não existe fatorial de números negativos, e ```0! = 1```.
Agora, vamos criar duas funções, uma usando iteração e outra usando recursividade.

##### Fatorial Iterativo

```python
def fatorial_ite(num):
    if(num == 0):
        return 1
    else:
        resultado = 1
        for i in range(1, num+1):
            resultado *= i
        return resultado
```

Na solução iterativa, primeiro verificamos se *num = 0*, e, caso não seja, utilizamos um ```for``` para multiplicar os números de *1* até *num+1* (assim, a função ```range()``` incluirá *num*).

##### Fatorial Recursivo

```python
def fatorial_rec(num):
    if(num == 0):
        return 1 # Caso base
    else:
        return num * fatorial_rec(num-1) # Caso recursivo
```

Na solução recursiva, temos um ```if``` que verifica se estamos no caso base (num == 0) ou no caso recursivo.
O caso recursivo chama novamente a função ```fatorial_rec()``` passando *(num-1)* como parâmetro. Assim eventualmente a função chamará ```fatorial_rec(0)```, nosso caso base, e então retornará o resultado para a chamada ```fatorial_rec(1)```, que vai multiplicar o retorno por 1 e retornar o resultado para a chamada ```fatorial_rec(2)```, que multiplicará o retorno por 2 e retornaráa o resultado para a chamada ```fatorial_rec(3)```, e assim por diante.

![Fatorial Recursivo](https://github.com/epicufscar/workshop-python/blob/master/img/img_fatorial.png)