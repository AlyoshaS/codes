Expressão Condicional.

Uma expressão condicional em python é o que em muitas linguagens, como por exemplo: C, javascript, php, java e etc, é chamado de operador ternário. É comum vermos expressões condicionais em trechos de código que possuem um desvio de fluxo simples(estrutura de controle condicional), em tecnês seria um if/else.
Você só poderá utilizá-lo em  estruturas condicionais compostas, ou seja, executar um comando quando uma condição for verdadeira ou outro quando a condição for falsa.  Não utilize esse exemplo em Estruturas Condicionais Aninhadas.

A forma geral de uma expressão condicional é:

<expressao1> if <condicao> else <expressao2>

Primeiro, a condição é avaliada (ao invés de expressao1), se a condição for verdadeira, expressao1 é avaliada e seu valor é retornado; caso contrário, expressao2 é avaliada e seu valor retornado.

exemplo:

x = 10
print ("par" if x % 2 == 0 else "impar")

Vejamos abaixo um bom exemplo de como podemos substituir uma estrutura condicional utilizando if/else, por uma expressão condicional:

if/else:

if media >= 7:
        print("Aprovado!")
else:
        print("Reprovado.")

expressão condicional:

print("aprovado" if media >= 7 else "Reprovado")

OBS: as duas formas estão corretas, mas a segunda é mais elegante!
