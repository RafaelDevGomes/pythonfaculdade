# anotações de python(fundamentos da programação)

## tipos de dados em python
1. string
2. number int
3. number float
4. boolean 

## operadores matematicos - básicos

1. + soma
2. - subtração
3. * multiplicação
4. / divisão

## métodos em python

1. print() exibe informações no terminal

## format em python

# estrutura condicional

``if(se)`` -> verifica se uma condição é true(verdadeira) se for, ele executa o code.
``else(senão)`` -> executa o código se a condição do if for false(falsa).
``eliif(senão se)`` -> é apenas utilizado se todas as outras condições anteriores forem false, ele é utilizado para verificar uma nova condição.

# operadores logicos
and -> e >- se duas condições forem true, ent o resultado é true.
or -> ou -> se peomenos uma condição for true, ent o resultado é true.
not -> ele altera o valor booleano da condição.

## boas práticas:
1. qualquer variavel utilizar o padrão case/snake_case ou recentemente o cammelCase.
2. se vc observar uma estrutura tipo nome(), 90% de chance de ser uma função.
3. python n tem constante, porém utilizamos o padrão case UPPERCASE, para simular que aquela variável n pd ser alterada.

# laços de repetição

é um recurso de programação que permite executar um conjunto de comandos várias vezes, também são chamados de Loop, laços de repetição ou iteração.

`For` -> Utilizamos quando sabemos quantas vezes queremos repetir algo.
sintaxe:
for variavel in range(inicio, fim:)
      comandos 
range() -> metódo que aceita geração de números.
inicio -> é inclusivo. o primeiro número a ser usado.
fim -> é exclusivo. o número utilizado é o anterior a esse.

## escopo das variaveis
escopo local: a variavel só pode ser acessada dentro daquele contexto que foi criada.
escopo global: a variavel pode ser acessada por todo mundo.

## variações das variáveis
variável em memória -> é declarada quando vc não pretende utilizar essa variável em outros cenários
variável contadora -> é utilizadapara uma lógica onde a repetição irá ser alterada.

while -> é utilizado quando não sabeos quantas vezes o programa vai repetir. ele repete enquanto uma condição for verdadeira.
Sintaxe:
while condição:
      comandos