# Workshop Python Iniciante

Repositório destinado ao Workshop de Python para Iniciantes. Aqui estarão as respostas para os exercícios (quando forem liberadas), e um guia (README.md) para a instalação, sintaxe, etc.

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

> [!IMPORTANT]
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

> [!IMPORTANT]
> Sempre se atente à indentação (espaços ou tabs antes dos comandos) para que o interpretador saiba a execução correta!

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
