# Estrutura de REPETIÇÃO

Repetições representam a base de vários programas. São utilizadas para executar a mesma parte de um programa várias vezes, normalmente dependendo de uma condição. Por exemplo, para imprimir três números na tela, poderíamos escrever um programa como o apresentado abaixo:

**Imprimindo de 1 a 3**

```python
print(1)
print(2)
print(3)
```

Podemos imaginar que para imprimir três números, começando de 1 até o 3, deveremos variar **print(x)**, onde `x` varia de 1 a 3. Vejamos outra solução para o problema abaixo:

**Imprimindo de 1 a 3 usando uma variável**
```python
x = 1
print(x)

x = 2
print(x)

x = 3
print(x)
```

Outra solução seria incrementar o valor de `x` após cada `print`. Vejamos essa solução abaixo:

**Imprimindo de 1 a 3 incrementando**
```python
x = 1
print(x)

x = x+1
print(x)

x = x+1
print(x)
```

Porém, se o objetivo fosse escrever 100 números, a solução não seria tão agradável, pois teríamos que escrever pelo menos 200 linhas! A estrutura de repetição aparece para nos auxiliar a resolver esse tipo de problema.

Uma das estruturas de repetição do Python é o **while**, que repete um bloco enquanto a condição for verdadeira. Seu formato é apresentado mais abaixo, onde `condição` é uma expressão lógica, e `bloco` representa as linhas de programa a repetir enquanto o resultado da condição for verdadeiro.

**Formato da estrutura de repetição com while**

```python
while <condição>:
    bloco
```

Para resolver o problema de escrever três números utilizado o **while**, escreveríamos um programa como o da listagem abaixo:

**Imprimindo de 1 a 3 com while**

```python
1 x = 1
2 while(x <= 3):
3    print(x)
4    x = x + 1
```

A execução desse programa seria um pouco diferente do que vimos até agora. Primeiramente, a linha 1 seria executada inicializando a variável `x` com o valor `1`. A linha 2 seria uma combinação de estrutura condicional com estrutura de repetição. Podemos entender a condição do **while** da mesma forma que a condição de **if**. A diferença é que, se a condição for verdadeira, repetiremos as linhas 3 e 4 (bloco) enquanto a avaliação da condição for verdadeira.

Na linha 4 teremos a impressão na tela propriamente dita, onde `x` é 1. Na linha 4 temos 1 acrescentado ao valor de x. Como `x` vale 1, `x + 1` valerá 2. Esse novo valor é então atribuído a `x`. A parte nova é que a execução não termina após a linha 4 que é o fim do bloco, mas retorna para a 2. É esse o retorno que faz a estrutura de repetição especial.

Agora `x` vale 2 e `x <= 3` continua verdadeiro(**True**), logo, o bloco será executado outra vez. A linha 3 realizará a impressão do valor 2, e a 4 atualizará o valor de `x` para `x + 1`; nesse caso, 2 + 1 = 3. A execução volta novamente para a linha 2.

A condição é avaliada novamente na linha 2, e como `x` vale 3, e `x <= 3` continua a ser verdadeira, fazendo com que as linhas 3 e 4 sejam executadas, exibindo 3 e atualizando o valor de `x` pra 4(3 + 1). 

Nesse ponto, em nossa avaliação(linha 2), temos que `x` vale 4 e que a condição `x <= 3` resulta em Falso (**False**), terminando, assim, a repetição do bloco.

**Exercício 1 -** Modifique o programa para exibir os números de 1 a 100.

**Exercício 2 -** Modifique o programa para exibir números de 50 a 100.

**Exercício 3 -** Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8...1, 0 e Fogo! na tela.

## Contadores

O poder das estruturas de repetições é muito interessante, principalmente quando utilizamos condições com mais de uma variável. Imagine um problema onde deveríamos imprimir os números inteiros entre 1 e um valor digitado pelo usuário. Vamos modificar o programa de exemplo que vimos anteriormente de forma que o último número a imprimir seja informado pelo usuário. O programa já modificado é apresentado abaixo:

**Impressão de 1 até um número digitado pelo usuário**

```python
fim = int(input("Digite o último número a ser impresso >> "))    1
x = 1;
while(x <= fim):                                                 2
    print(x)                                                     3
    x = x + 1                                                    4
```

Nesse caso, o programa imprimirá de 1 até o valor digitado em **1**. em **2** utilizamos a variável `fim` para representar o limite de nossa repetição.

Agora vamos analisar o que realizamos com a variável `x` dentro da repetição. Em **3** o valor de `x` é simplesmente impresso. Em **4** atualizamos o valor de `x` com `x + 1`, ou seja, com o próximo valor inteiro. Quando realizamos esse tipo de operação dentro de uma repetição estamos contando. Logo diremos que `x` é um contador. Um contador é uma variável utilizada pra contar o número de ocorrências de um determinado evento; nesse caso, o número de repetições do **while**, que satisfaz às necessidades do nosso problema.

Experimente esse programa com vários valores, primeiro digitando 5, depois 500 e, por fim, 0(zero). Provavelmente, 5 e 500 produzirão os resultados esperados, ou seja, a impressão de 1 até 5, ou de 1 até 500. Porém, quando digitamos zero, nada acontece, e o programa termina logo a seguir, sem impressão.

Analisando nosso programa quando a variável `fim` vale 0, ou seja, quando digitamos 0 em **1**, temos que a condição em **2** é `x <= fim`. Como `x` é 1 e `fim` é 0, temos que `1 <= 0` é falso desde a primeira execução, fazendo com que o bloco repetir não seja executado, uma vez que sua condição de entrada é falsa. O mesmo aconteceria na inserção de valores negativos.

Imagine que o problema agora seja um pouco diferente: imprimir apenas os números pares entre 0 e um número digitado pelo usuário, de forma bem similar ao problema anterior. Poderíamos resolver o problema com um `if` para testar se `x` é par ou ímpar antes de imprimir. Vale lembrar que um número é par quando é 0 ou múltiplo de 2. Quando é múltiplo de 2, temos que o resto da divisão desse número por 2 é 0, ou seja, o resultado é uma divisão exata, sem resto. Em Python, podemos escrever esse teste com `x % 2 == 0`(resto da divisão de `x` por `2` é igual a zero), alterando o programa anterior para o programa abaixo:

**Impressão de números pares de 0 até um número digitado pelo usuário**

```python
fim = int(input("Digite o último número a ser impresso >> "))
x = 0;                                                           1
while(x <= fim):
    if x % 2 == 0:                                               2
        print(x)                                                 3
    x = x + 1
```

Veja que, para começar a imprimir do 0, e não de 1, modificamos **1**. Um detalhe importante é que **3** é um bloco dentro de `if` **2**, sendo para isso deslocado à direita. Execute o programa e verifique seu resultado.

Agora, finalmente, estamos resolvendo o problema, mas poderíamos resolvê-lo de forma ainda mais simples se adicionássemos 2 a `x` a cada repetição. Isso garantiria que `x` sempre fosse par. Vejamos o programa abaixo:

**Impressão de números pares de 0 até um número digitado pelo usuário, sem if**

```python
fim = int(input("Digite o último a imprimir >> "))

x = 0
while(x <= fim):
    print(x)
    x = x + 2
```

Esses dois exemplos mostram que existe mais de uma solução para o problema, que podemos escrever programas diferentes o obter a mesma solução. Essas soluções podem ser às vezes mais complicadas, às vezes mais simples, mas ainda assim corretas.

**Exercício 4 -** Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas números ímpares.

**Exercício 5 -** Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

Vejamos outro tipo de problema. Imagine ter que imprimir a tabuada de adição de um número digitado pelo usuário. Essa tabuada deve ser impressa de 1 a 10, sendo `n` o número digitado pelo usuário. Teríamos, assim, n+1, n+2, ... n+10. Confira a solução abaixo:

**Tabuada simples**

```python
n = int(input("Tabuada de >> "))

x = 1
while(x <= 10):
    print(n+x)
    x = x + 1
```

Execute o programa anterior e experimente diversos valores.

**Exercício 6 -** Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4,...

**Exercício 7 -** Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

**Exercício 8 -** Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

**Exercício 9 -** Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão.Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo. 20 + 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

Contadores também podem ser úteis quando usados com condições dentro dos programas. Vejamos um programa para corrigir um teste de múltipla escolha com três questões. A resposta da primeira é "b"; da segunda, "a"; e da terceira, "d". O programa abaixo conta um ponto a cada resposta correta.

**Contagem de questões corretas**

```python
pontos = 0
questao = 1

while(questao <= 3);
    resposta = input("Resposta da questão %d: " % questao)
    if(questao == 1 and resposta == "b"):
        pontos = pontos + 1
    if(questao == 2 and resposta == "a"):
        pontos = pontos + 1
    if(questao == 3 and resposta == "d"):
        pontos = pontos + 1
    questao += 1
print("O aluno fez %d ponto(s)" % pontos)
```

Execute o programa e digite todas as respostas corretas, depois tente com respostas diferentes. Veja que estamos verificando apenas respostas simples de uma só letra e que consideramos apenas letras minúsculas. Em Python, uma letra minúscula é diferente de uma maiúscula. Se você digitar "A" na segunda questão em de "a", o programa não considerará essa resposta correta. Uma solução para esse tipo de problema é utilizar o operador lógico **or** e verificar a resposta maiúscula e minúscula. Por exemplo, `questao == 1 and (resposta == "b" or resposta == "B")`.

**Exercício 10 -** Modifique o programa anterior pra que ele aceite respostas com letras maiúsculas e minúsculas em todas as questões.

Embora essa verificação resolva o problema, veremos que, se digitarmos um espaço em branco antes ou depois da resposta, ela também será considerada errada. Sempre que trabalharmos com strings, esse tipo de problema deve contornado.

## Acumuladores

Nem só de contadores precisamos. Em programas para calcular o total de uma soma, por exemplo, precisaremos de acumuladores. A diferença entre um contador e um acumulador é que nos contadores o valor adicionado é constante e, nos acumuladores, variável. Vejamos um programa que calcule a soma de 10 números. Nesse caso, `soma` **1** é um acumulador e `n` **2** é um contador.

**Soma de 10 números**

```python
n = 1
soma = 0

while(n <= 10):
    x = int(input("Digite o %d número" %n))
    soma = soma + x                             1
    n = n + 1                                   2
print("Soma: %d" %soma)
```

Podemos definir a média aritméica como a soma de vários números divididos pela quantidade de números somados. Assim, se somarmos três números, 4, 5 e 6, teríamos a média aritméica como (4 + 5 + 6) / 3, onde 3 é a quantidade de números. Se acharmos o primeiro número de n1, o segundo de n2 e o terceiro de n3, teremos (n1 + n2 + n3) / 3.

Vejamos um programa que calcula a média de cinco números digitados pelo usuário no programa a seguir. Se acharmos o primeiro valor digitado de n1, o segundo de n2, e assim por diante, teremos que:

`media = (n1 + n2 + n3 + n4 + n5) / 5`

Em vez de utilizarmos cinco variáveis, vamos acumular os valores à medida que são lidos.

**Cálculo de média com acumulador**

```python
x = 1

soma = 0                                            1
while(x <= 5):
    n = int(input("%d Digite o número: " % x))
    soma = soma + n                                 2
    x = x + 1
print("Média: %5.2f" % (soma / 5))                  3
```

Nesse caso, temos `x` sendo um contador e `n` o valor digitado pelo usuário. A variável `soma` é criada em **1** e inicializada com 0. Diferetemente de `x`, que recebe 1 a cada passagem, a variável `soma`, em **2**, é adicionada do valor digitado pelo usuário. Podemos dizer que o incremento de `soma` não é um valor constante, pois varia com o valor digitado pelo usuário. Podemos também dizer que `soma` acumula os valores de `n` a cada repetição. Logo, diremos que a variável `soma` é um acumulador.

Acumuladores são muito interessantes quando não sabemos ou não conseguimos obter o total da soma pela simples multiplicação de dois números. No caso do cálculo da média, o valor de `n` pode ser diferente cada vez que o usuário digitar um valor.

**Exercício 11-** Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

**Exercício 12-** Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no ínicio de cada mês e você deve considerá-lo para o cálculo de juros do mês seguinte.

**Exercício 13-** Escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

## Interrompendo a repetição

Embora muito útil, a estrutura **while** só verifica sua condição de parada no início de cada repetição. Dependendo do problema, a habilidade de terminar **while** dentro do bloco a repetir pode ser interessante.

A instrução **brak** é utilizada para interromper a execução de **while** independentemente do valor atual de sua condição. Vejamos o exemplo da leitura de valores até que digitemos 0(zero) no programa abaixo:

**Interrompendo a repetição**

```python
```
