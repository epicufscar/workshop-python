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
nome = "Joanelson"
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
Exemplo:
```python

```