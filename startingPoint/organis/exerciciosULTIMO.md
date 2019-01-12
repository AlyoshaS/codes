# Exercícios resolvidos sobre estruturas condicionais

**00** - A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.  Média das três notas mencionadas obedece ao pesos a seguir:

|NOTA   |PESO   |
|---|:-:|
| Trabalho de laboratório  | 2  |
| Avaliacao semestral  | 3  |
| Exame final  | 5  |


Faça um programa que receba as três notas, calcule e mostre a média e o conceito que segue a tabela:

|MÉDIA PONDERADA   |CONCEITO   |
|---|:-:|
| 8,0 **+**-----------**+** 10,0 | A  |
| 7,0 **+**----------**\*** 8,0  | B  |
| 6,0 **+**-----------**\*** 7,0  | C  |
| 5,0 **+**-----------**\*** 6,0  | D  |
| 0,0 **+**-----------**\*** 5,0  | E  |


```
DECLARE nota_trab, aval_sem, exame, media NUMÉRICO

ESCREVA "Digite a nota do trabalho de laboratório: "
LEIA nota_trab

ESCREVA "Digite a nota de avaliação semestral: "
LEIA aval_sem

ESCREVA "Digite a nota do exame final: "
LEIA exame

media <- (nota_trab * 2 + aval_sem * 3 + exame * 5) / 10

SE media >= 8 E media <= 10
	ENTÃO ESCREVA "Obteve conceito A"
SE media >= 7 E media < 8
	ENTÃO ESCREVA "Obteve conceito B"
SE media >= 6 E media < 7
	ENTAO ESCREVA "Obteve conceito C"
SE media >= 5 E media < 6
	ENTÃO ESCREVA "Obteve conceito D"
SE media >= 0 E media < 5
	ENTÃO ESCREVA "Obteve conceito E"

```
----

**01** - Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão tirar para serem aprovados, considerando que a média exibida é 6,0.

|MÉDIA ARITMÉTICA   | MENSAGEM   |
|---|:-:|
| 0,0 **+**-----------**+** 3,0 | Reprovado  |
| 3,0 **+**----------**\+** 7,0  | Exame  |
| 7,0 **+**-----------**\*** 10,0  | Aprovado  |

```
DECLARE nota1, nota2, nota3, media, nota_exame NUMÉRICO

ESCREVA "Digite a primeira nota: "
LEIA nota1

ESCREVA "Digite a segunda nota: "
LEIA nota2

ESCREVA "Digite a terceira nota: "
LEIA nota3

media <- (nota1 + nota2 + nota3) / 3

ESCREVA "Media aritmética: ", media

SE media >= 0 E media < 3
	ENTAO ESCREVA "Reprovado"

SE media >= 3 E media < 7
	ENTAO INICIO
		ESCREVA "Exame"
		nota_exame <- 12 - media
		ESCREVA "Deve tirar nota", nota_exame, "para ser aprovado"
	FIM
SE media >= 7 E media <= 10
	ENTAO ESCREVA "Aprovado"

```
----

**02** - Faça um programa que receba dois números e mostre o maior

```
DECLARE num1, num2 NUMERICO

ESCREVA "Digite o primeiro numero: "
LEIA num1

ESCREVA "Digite o segundo numero: "
LEIA num2

SE num1 > num2
	ENTAO ESCREVA "O maior numero é ", num1

SE num1 < num2
	ENTAO ESCREVA "O maior numero é ", num2
	
SE num1 == num2
	ENTAO ESCREVA "Os numeros sao iguais!"
```

----

**03** - Faça um programa que receba três números e mostre-os em ordem crescente. Suponha que o usuário digitará três números diferentes.

```
DECLARE num1, num2, num3 NUMERO

ESCREVA "Digite o primeiro numero: "
LEIA num1

ESCREVA "Digite o segundo numero: "
LEIA num2

ESCREVA "Digite o terceiro numero: "
LEIA num3

SE num1 < num2 E num1 < num3
	ENTAO SE num2 < num3
		ENTAO ESCREVA "A ordem crescente é: ", num1, "-", num2, "-", num3
		SENAO ESCREVA "ESCREVA "A ordem crescente é: ", num1, "-", num3, "-", num2"

	SE num2 < num1 E num2 < num3
		ENTAO SE num1 < num3
			ENTAO ESCREVA "A ordem crescente é: ", num2, "-", num1, "-", num3
			SENAO ESCREVA "ESCREVA "A ordem crescente é: ", num2, "-", num3, "-", num1"
	
	SE num3 < num1 E num3 < num2
		ENTAO SE num1 < num2
			ENTAO ESCREVA "A ordem crescente é: ", num3, "-", num1, "-", num2
			SENAO ESCREVA "ESCREVA "A ordem crescente é: ", num3, "-", num2, "-", num1"

```

----

**04** - Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga essa regra, Mostre, em seguida, os quatro números em ordem decrescente. Suponha que o usuário digitará quatro números diferentes.

```
DECLARE num1, num2, num3, num4 NUMERICO

ESCREVA "Digite três números em ordem crescente: "
LEIA num1
LEIA num2
LEIA num3

ESCREVA "Digite o número (fora de ordem): "
LEIA num4

SE num4 > num3
	ENTAO ESCREVA "A ordem decrescente é: ", num4, "-", num3, "-", num2, "-", num1

SE num4 > num2 E num4 < num3
	ENTAO ESCREVA "A ordem decrescente é: ", num3, "-", num4, "-", num2, "-", num1

SE num4 > num1 E num4 < num2
	ENTAO ESCREVA "A ordem decrescente é: ", num3, "-", num2, "-", num4, "-", num1

SE num4 < num1
	ENTAO ESCREVA "A ordem decrescente é: ", num3, "-", num2, "-", num1, "-", num4
```

----

**05** - Faça um programa que receba um número inteiro e verifique se é par ou ímpar

```
DECLARE num, r

ESCREVA "Digite um número: "
LEIA num

r <- RESTO(num / 2)

SE r = 0
	ENTAO ESCREVA "O numero é par"
	SENAO ESCREVA "O numero é impar"
```

----

**06** - Faça um programa que receba quatro valores I, A, B, C. Desses valores, I é inteiro e positivo, A, B e C são reais. Escreva os números A, B e C obedecendo à tabela a seguir.

Suponha que o valor digitado para I seja sempre um valor válido, ou seja, 1, 2 ou 3, e que os números digitados sejam diferentes um do outro.

|VALOR DE I   | FORMA DE ESCREVER   |
|---|:-:|
| 1 | A, B, C em ordem crescente  |
| 2  | A, B, C em ordem decrescente  |
| 2  | O maior fica entre os outros dois números |


```
DECLARE A, B, C, I NUMERICO
ESCREVA "DIGITE um valor para A"
LEIA A

ESCREVA "DIGITE um valor para B"
LEIA B

ESCREVA "DIGITE um valor para C"
LEIA C

ESCREVA "DIGITE um valor para I (1, 3, ou 3)"
LEIA I

SE(I == 1)
	SE(A < B) E (A < C)
		SE(B < C)
			ESCREVA "A ordem crescente dos números é: ", A, "-", B, "-", C
		SENAO
			ESCREVA "A ordem crescente dos números é: ", A, "-", C, "-", B 
	SE(B < A) E (B < C)
		SE(A < C)
			ESCREVA "A ordem crescente dos números é: ", B, "-", A, "-", C
		SENAO
			ESCREVA "A ordem crescente dos números é: ", B, "-", C, "-", A
	SE(C < A) E (C < B)
		SE(A < B)
			ESCREVA "A ordem crescente dos números é: ", C, "-", A, "-", B
		SENAO
			ESCREVA "A ordem crescente dos números é: ", C, "-", B, "-", A
	
SE(I == 2)
	SE(A > B) E (A > C)
		SE(B > C)
			ESCREVA "A ordem decrescente dos números é: ", A, "-", B, "-", C
		SENAO
			ESCREVA "A ordem crescente dos números é: ", A, "-", C, "-", B
	SE(B > A) E (B > C)
		SE(A > C)
			ESCREVA "A ordem crescente dos números é: ", B, "-", A, "-", C
		SENAO
			ESCREVA "A ordem crescente dos números é: ", B, "-", C, "-", A
	SE(C > A) E (C > B)
		SE(A > B)
			ESCREVA "A ordem crescente dos números é: ", C, "-", A, "-", B
		SENAO
			ESCREVA "A ordem crescente dos números é: ", C, "-", B, "-", A

SE(I == 3)
	SE(A > B) E (A > C)
		ESCREVA "A ordem desejada é: ", B, "-", A, "-", C
	SE(B > A) E (B > C)
		ESCREVA "A ordem desejada é: ", A, "-", B, "-", C
	SE(C > A) E (C > B)
		ESCREVA "A ordem desejada é: ", A, "-", C, "-", B
```

----

**07** - Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários para executar cada operação.

Menu de opções:

1. Somar dois números
2. Raiz Quadrada de um número.

Digite a opção desejada

```
DECLARE num1, num2, soma, raiz, op NUMERICO
ESCREVA " MENU"
ESCREVA "1 - Somar dois números"
ESCREVA "2 - Raiz quadrada de um número"
ESCREVA "Digite sua opção: "
LEIA op

SE(op == 1)
	ESCREVA "Digite o valor para o primeiro número: "
	LEIA num1
	
	ESCREVA "Digite um valor para o segundo número: "
	LEIA num2
	soma <- num1 + num2
	ESCREVA "A soma de ",num1," e ",num2," é ",soma

SE(op == 2)
	ESCREVA "Digite um valor: "
	LEIA num1
	raiz <- raizq(num1)
	ESCREVA "A raiz quadrada de ",num1," é ",raiz

SE(op != 1) E (op != 2)
	ESCREVA "Opção inválida!"
	
```

----

**08** - Faça um programa que mostre a data e a hora do sistema nos seguintes formatos DD/MM/AAAA - mês por extenso e hora:minuto

```
DECLARE t, d, dia, mes, ano, hora, min NUMERICO
d <- OBTENHA_DATA
dia <- OBTENHA_DIA(d)
mes <- OBTENHA_MES(d)
ano <- OBTENHA_ANO(d)

ESCREVA "Data Atual: ", dia, "/", mes, "/", ano, " - "
SE(mes = 1)
	ESCREVA "janeiro"
SE(mes = 2)
	ESCREVA "fevereiro"
SE(mes = 3)
	ESCREVA "março"
SE(mes = 4)
	ESCREVA "abril"
SE(mes = 5)
	ESCREVA "maio"
SE(mes = 6)
	ESCREVA "junho"
SE(mes = 7)
	ESCREVA "julho"
SE(mes = 8)
	ESCREVA "agosto"
SE(mes = 9)
	ESCREVA "setembro"
SE(mes = 10)
	ESCREVA "outubro"
SE(mes = 11)
	ESCREVA "novembro"
SE(mes = 12)
	ESCREVA "dezembro"

t <- OBTENHA_HORA(t)
hora <- OBTENHA_MINUTO(t)
ESCREVA "Hora Atual: "
ESCREVA hora, ":", min
```

----

**09** - Faça um programa que determine a data cronologicamente maior entre duas datas fornecidas pelo usuário. Cada data deve ser composta por três valores inteiros, em que o primeiro representa o dia, o segundo, o mês e o terceiro, o ano.

```
DECLARE d1, m1, a1, d2, m2, a2 NUMERICO
ESCREVA "Digite a primeira data"
ESCREVA " dia (dd): "
LEIA d1

ESCREVA " mês (mm): "
LEIA m1

ESCREVA " ano (aaaa): "
LEIA a1

ESCREVA "Digite a segunda data"
ESCREVA " dia (dd): "
LEIA d2

ESCREVA " mês (mm): "
LEIA m2

ESCREVA " ano (aaaa): "
LEIA a2

SE(a1 > a2)
	ESCREVA "A maior data é: ",d1,"-",m1,"-",a1
SENAO SE(a2 > a1)
	ESCREVA "A maior data é: ",d2,"-",m2,"-",a2
	SENAO SE(m1 > m2)
		ESCREVA "A maior data é: ",d1,"-",m1,"-",a1
		SENAO SE(m2 > m1)
			ESCREVA "A maior data é: ",d2,"-",m2,"-",a2
			SENAO SE(d1 > d2)
				ESCREVA "A maior data é: ",d1,"-",m1,"-",a1
				SENAO SE(d2 > d1)
					ESCREVA "A maior data é: ",d2,"-",m2,"-",a2
					SENAO
						ESCREVA "As datas são iguais!"
```

----

**10** - Faça um programa que receba a hora do início de um jogo e a hora final (cada hora é composta por duas variáveis inteiras: hora e minuto). Calcule e mostre a duração do jogo(horas e minutos), sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia seguinte

```
DECLARE hora_i, min_i, hora_f, min_f, hora_d, min_d NUMERICO
ESCREVA "Digite o horário inicial"
ESCREVA "hora: "
LEIA hora_i
ESCREVA "minuto: "
LEIA min_i

ESCREVA "Digite o horário final "
ESCREVA "hora: "
LEIA hora_f
ESCREVA "minuto: "
LEIA min_f

SE(min_i > min_f)
	min_f <- min_f + 60
	hora_f <- hora_f -1

SE(hora_i > hora_f)
	hora_f <- hora_f + 24

min_d <- min_f - min_i
hora_d <- hora_f - hora_i

ESCREVA "O jogo durou ",hora_d," hora(s) e ",min_d," minutos(s)"
```

----

**11** - Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargo estão na tabela abaixo.

|  CÓDIGO  |  CARGO  |  PERCENTUAL  |
|---| --- |:-:|
|  1  |  Escrituário  |  50%  |
|  2  |  Secretário   |  35%  |
|  3  |  Caixa  	  |  20%  |
|  4  |  Gerente  	  |  10%  |
|  5  |  Diretor  	  |  Não tem aumento  |


```
DECLARE salario, aumento, novo_sal, cargo NUMERICO
ESCREVA "Digite o cargo do funcionário (1, 2, 3, 4 ou 5)"
LEIA cargo
ESCREVA "Digite o valor do salário: "
LEIA salario

SE(cargo == 1)
	ESCREVA "O cargo é Escrituário"
	aumento <- salario * 50 / 100
	ESCREVA "O valor do aumento é: ",aumento
	novo_sal <- salario + aumento
	ESCREVA "O novo salario é ", novo_sal
	
SENAO SE(cargo == 2)
	ESCREVA "O cargo é Secretário"
	aumento <- salario * 35 / 100
	ESCREVA "O valor do aumento é: ",aumento
	novo_sal <- salario + aumento
	ESCREVA "O novo salario é ", novo_sal
	
SENAO SE(cargo == 3)
	ESCREVA "O cargo é Caixa"
	aumento <- salario * 20 / 100
	ESCREVA "O valor do aumento é: ",aumento
	novo_sal <- salario + aumento
	ESCREVA "O novo salario é ", novo_sal	
		
SENAO SE(cargo == 4)
	ESCREVA "O cargo é Gerente"
	aumento <- salario * 10 / 100
	ESCREVA "O valor do aumento é: ",aumento
	novo_sal <- salario + aumento
	ESCREVA "O novo salario é ", novo_sal
			
SENAO SE(cargo == 5)
	ESCREVA "O cargo é Diretor"
	aumento <- salario * 0 / 100
	ESCREVA "O valor do aumento é: ",aumento
	novo_sal <- salario + aumento
	ESCREVA "O novo salario é ", novo_sal	
	
	SENAO
		ESCREVA "Cargo Inexistente!"
```

----

**12** - Faça um programa que apresente o menu a seguir, permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. Verifique a possibilidade de opção inválida e não se preocupe com restrições, como salário negativo.

Menu de opções:

1. Imposto
2. Novo salario
3. Classificação

Digite a opção desejada

**Na opção 1:** Receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras a seguir:

|  SALÁRIO  |  PERCENTUAL DO IMPOSTO
|---| :-:|
|  Menor que R$ 500,00  |  5%
|  de R$ 500,00 a R$ 850,00  |  10%
|  Acima de R$ 850,00 |  15%

**Na opção 2:** receber o salário de um funcionário, calcular e mostrar o valor do novo saláriom usando as regras a seguir:

|  SALÁRIO  |  AUMENTO
|---| :-:|
|  Maior que R$ 1.500,00  |  R$ 25,00
|  De R$ 750,00(inclusive) a R$ 1.500,00(inclusive)  |  R$ 50,00
|  De R$ 450,00(inclusive) a R$ 750,00 | R$ 75,00
|  Menor que R$ 450,00  |  R$ 100,00

**Na opção 3:** receber o salário de um funcionário e mostrar sua classificação usando a tabela a seguir:

|  SALÁRIO  |  CLASSIFICAÇÃO
|---| :-:|
|  Até R$ 750,00(inclusive)  |  Mal remunerado
|  Maiores que R$ 750,00 |  Bem remunerado


```
DECLARE op, sal, imp, aum, novo_sal
LEIA op

SE op == 1
	LEIA sal
	SE sal < 500
		imp <- sal * 5 / 100
	SE sal >= 500 E sal <= 850
		imp <- sal * 10/100
	SE sal > 850
		imp <- sal * 15/100
	
	ESCREVA imp

SE op == 2
	LEIA sal
	SE sal > 1500
		aum <- 25
	SE sal >= 750 E sal <= 1500
		aum <- 50
	SE sal >= 450 E sal < 750
		aum <- 75
	SE sal < 450
		aum <- 100
	novo_sal <- sal + aum
	ESCREVA novo_sal

SE op == 3
	LEIA sal
	SE sal <= 700
		ESCREVA "Mal Remunerado"
	SE sal > 700
		ESCREVA "Bem Remunerado"

SE op < 1 OU op > 3
	ESCREVA "Opção Inválida"
```

----

**13** - Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, acrescido de bonificação e auxílio escola.

|  SALÁRIO  |  CLASSIFICAÇÃO
|---| :-:|
| Até R$ 500,00 | 5% do salário
| Entre R$ 500,00 e R$ 1.200,00 | 12% do salário
| Acima de R$ 1.200,00 | Sem bonificação

|  SALÁRIO  |  AUXÍLIO ESCOLA
|---| :-:|
| Até R$ 600,00 | R$ 150,00
| Mais que R$ 600,00 | R$ 100,00


```
DECLARE sal, novo_sal, boni, aux
LEIA sal
SE sal <= 500
	boni <- sal * 5 / 100
SENAO SE sal <= 1200
	boni <- sal * 12 / 100
SENAO
	boni <- 0

SE SAL <= 600
	aux <- 150
SENAO 
	aux <- 100

novo_sal <- sal + boni + aux
ESCREVA novo_sal
```

----

**14** - Faça um programa que receba o valor do salário mínimo, o número de horas trabalhadas, o número de dependentes do funcionário e a quantidade de horas extras trabalhadas. Calcule e mostre o salário a receber do funcionário de acordo com as regras a seguir:

* O valor da hora trabalhada é igual a quinta parte do salário mínimo.
* O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
* Para cada dependente, acrescentar R$ 32,00.
* Para cada hora extra trabalhada, calcular o calor da hora trabalhada acrescida de 50%.
* O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas extras.
* Calcular o valor do imposto de renda retido na fonte de acordo com a tabela a seguir

|  IRRF  |  SALÁRIO BRUTO
|---| :-:|
| Isento | Inferior a R$ 200,00
| 10% | De R$ 200,00 até R$ 500,00
| 20% | Superior a R$ 500,00

* O salário líquido é igual ao salário bruto menos IRRF.
* A gratificação de acordo com a tabela a seguir:

|  SALÁRIO LÍQUIDO  |  GRATIFICAÇÃO
|---| :-:|
| Até R$ 350,00 | R$ 100,00
| Superior a R$ 350,00 | R$ 50,00

* O salário a receber do funcionário é igual ao salário líquido mais a gratificação.

```
DECLARE sal_min, nht, ndep, nhet
		sal_receber, vh, smes, vdep, vhe, imp
		sbruto, sliq, grat

LEIA sal_min, nht, ndep, nhet
vh <- 1 / 5 * sal_min
smes <- nht * vh
vdep <- nhet * (vh * 50 / 100)
sbruto <- smes + vdep + vhe

SE sbruto < 200
	imp <- 0

SE sbruto >= 200 E sbruto <= 500
	imp <- sbruto * 10 / 100
SE sbruto > 500
	imp <- sbruto * 20 / 100

sliq <- sbruto - imp

SE sliq <= 350
	grat <- 100
SE sliq > 350
	grat <- 50

sal_receber <- sliq + grat
ESCREVA sal_receber

```

----

**15** - Um supermercado deseja reajustar os preços de seus produtos usando o seguinte critério: o produto poderá ter seu preço aumentado ou diminuído. Para o preço ser alterado, o produto deve preencher pelo menos um dos requisitos a seguir:

|  VENDA MÉDIA MENSAL  |  PREÇO ATUAL | % DE AUMENTO | %DE DIMINUIÇÃO
|---|---|---| :-:|
| < 500 | < R$ 30,00 | 10 | -
| >= 500 e < 1.200 | >= R$ 30,00 e < R$ 80,00 | 15 | -
| >= 1.200 | >= R$ 80,00 | - | 20

Faça um programa que receba o preço atual e a venda média mensal do produto, calcule e mostre o novo preço.

```
DECLARE pre, venda, novo_pre
LEIA pre, venda

SE venda < 500 OU pre < 30
	novo_pre <- pre + 10/100 * pre
SENAO SE(venda >= 500 E venda < 1200) OU (pre >= 30 E pre < 80)
	novo_pre <- pre + 15 / 100 * pre
SENAO SE venda >= 1200 OU pre >= 80
	novo_pre <- pre - 20 / 100 * pre
	
ESCREVA novo_pre
```

----

**16** - Faça um programa para resolver equações do 2° grau.

```
ax² + bx + c = 0
A variável a deve ser diferente de zero.
∆ = b² - 4 * a * c
∆ < 0 -> não existe raiz real
∆ = 0 -> existe uma raiz real
x = (-b) / (2 * a)
∆ > 0 -> existem duas raízes reais
x1 = (-b + raizq(∆) / (2 * a))
x2 = (-b - raizq(∆) / (2 * a))
```

```
DECLARE a, b, c, delta, x1, x2
LEIA a, b, c
SE a = 0
	ESCREVA "Estes valores não formam uma equação do segundo grau"
SENAO
	delta <- (b * b) - (4 * a * c)
	SE delta < 0
		ESCREVA "Não existe raiz real"
	SE delta = 0
		ESCREVA "Existe uma raiz real"
		x1 = <- (-b) / (2 * a)
		ESCREVA x1
	SE delta > 0
		ESCREVA "Existe duas raízes reais"
		x1 <- (-b + raizq(∆)) / (2 * a)
		x2 <- (-b - raizq(∆)) / (2 * a)
		ESCREVA x1, x2
```

----

**17** - Dados três valores X, Y e Z, verifique se eles podem ser os comprimentos dos lados de um triângulo e, se forem, 
verifique se é um triângulo equilátero, isóceles ou escaleno. Se eles não formarem um triângulo, escreva uma mensagem. 
Considere que:

* O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
* Chama-se equilátero o triângulo que tem três lados iguais.
* Denomina-se isóceles o triângulo que tem o comprimento de dois lados iguais.
* Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

```
DECLARE x, y, z
LEIA x, y, z
SE ( (x < y + z) E (y < x + z) E (z < x + y) )
	SE ( (x == y) E (y == z) )
		ESCREVA "Triangulo Equilátero"
	SENAO SE( (x == y) OU (x == z) OU (y == z) )
		ESCREVA "Triangulo Isóceles"
	SENAO SE( (x != y) E (x != z) E (y != z) )
		ESCREVA "Triangulo Escaleno"
SENAO
	ESCREVA "Essas medidas não formam um triângulo"
```

----

**18** - Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre a cassificação dessa pessoa.

```
+------------------+------------------------------------------------------+
|                  |                       PESO                           |
|    ALTURA        +------------------------------------------------------+
|                  | Até 60      Entre 60 e 90(inclusive)    Acima de 90  |
+------------------+------------------------------------------------------+
|Menores que 1,20  |   A                     D                     G      |
|De 1,20 a 1,70    |   B                     E                     H      |
|Maiores que 1,70  |   C                     F                     I      |
+------------------+------------------------------------------------------+
```

```
DECLARE altura, peso NUMERICO
LEIA altura, peso

SE altura < 1.20
    SE peso <= 60
        ESCREVA "A"
    SE peso > 60 E peso <= 90
        ESCREVA "D"
    SE peso > 90
        ESCREVA "G"

SE altura >= 1.20 E altura <= 1.70
    SE peso <= 60
        ESCREVA "B"
    SE peso > 60 E peso <= 90
        ESCREVA "E"
    se peso > 90
        ESCREVA "H"

SE altura > 1.70
    SE peso <= 60
        ESCREVA "C"
    SE peso > 60 E peso <= 90
        ESCREVA "F"
    SE peso > 90
        ESCREVA "I"
```

----

**19** - Faça um programa que receba:

* O código de um produto comprado, supondo que a digitação do código do produto seja sempre válida, ou seja, um número inteiro entre 1 e 10.
* O peso do produto em quilos.
* O código do país de origem, supondo que a digitação do código seja sempre válida, ou seja, um número inteiro entre 1 e 3

Tabelas:

| CÓDIGO DO PAÍS DE ORIGEM | IMPOSTO |
|--------------------------|---------|
|                        1 | 0%      |
|                        2 | 15%     |
|                        3 | 25%     |

| CÓDIGO DO PRODUTO | PREÇO POR GRAMA |
|-------------------|-----------------|
| 1 a 4             |              10 |
| 5 a 7             |              25 |
| 8 a 10            |              35 |


Calcule e mostre:

* O peso do produto convertido em gramas.
* O preço total do produto comprado.
* O valor do imposto, sabendo-se que ele é cobrado sobre o preço total do produto e depende do país de origem.
* O valor total, preço total do produto mais imposto

```
DECLARE cod_prod, peso_quilos, NUMERICO
        cod_pais, peso_gramas, pre_total NUMERICO
        imposto, valor_total, pre_grama NUMERICO

LEIA cod_prod, peso_quilos, cod_pais
peso_gramas <- peso_quilos * 1000
ESCREVA peso_gramas

SE cod_prod >= 1 E cod_prod <= 4
    pre_grama <- 10
SE cod_prod >= 5 E cod_pais <= 7
    pre_grama <- 25
SE cod_prod >= 8 E cod_prod <= 10
    pre_grama <- 35

pre_total <- peso_gramas * pre_grama
ESCREVA pre_total

SE cod_pais == 1
    imposto <- 0
SE cod_pais == 2
    imposto <- pre_total * 15/100
SE cod_pais == 3
    imposto <- pre_total * 25/100

ESCREVA imposto
valor_total <- pre_total + imposto
ESCREVA valor_total
```

----

**20** - Faça um programa que receba:

* O código do estado de origem da carga de um caminhão, supondo que a digitação do código do estado seja sempre válida, ou seja, um número inteiro entre 1 e 5
* O peso da carga do caminhão em toneladas.
* O código da carga, supondo que a digitação do código seja sempre válida, ou seja, um número inteiro entre 10 e 40.

Tabelas:

| CÓDIGO DO ESTADO  | IMPOSTO |
|-------------------|---------|
| 1                 |   35%   |
| 2                 |   25%   |
| 3                 |   15%   |
| 4                 |    5%   |
| 5                 |  Isento |


| CÓDIGO DA CARGA  | PREÇO POR QUILO |
|------------------|-----------------|
| 10 a 20          | 100             |
| 21 a 30          | 250             |
| 31 a 40          | 340             |

Calcule e mostre:

* O peso da carga do caminhão convertido em quilos.
* O preço da carga do caminhão
* O valor do imposto, sabendo-se que o imposto é cobrado sobre o preço da carga do caminhão e depende do estado de origem
* O valor total transportado pelo caminhão, preço da carga mais imposto.

```
DECLARE cod_est, cod_carga, peso_toneladas NUMERICO
        peso_quilos, pre_carga, imposto, valor_total NUMERICO

LEIA cod_est, peso_toneladas, cod_carga
peso_quilos <- peso_toneladas * 1000
ESCREVA peso_quilos

SE cod_carga >= 10 E cod_carga <= 20
    pre_carga <- 100 * peso_quilos
SE cod_carga >= 21 E cod_carga <= 30
    pre_carga <- 250 * peso_quilos
SE cod_carga >= 31 E cod_carga <= 40
    pre_carga <- 340 * peso_quilos
ESCREVA pre_carga

SE cod_est == 1
    imposto <- 35/100 * pre_carga
SE cod_est == 2
    imposto <- 25/100 * pre_carga
SE cod_est == 3
    imposto <- 15/100 * pre_carga
SE cod_est == 4
    imposto <- 5/100 * pre_carga
SE cod_est = 5
    imposto <- 0

ESCREVA imposto
valor_total <- pre_carga + imposto
ESCREVA valor_total
```

----

**21** - Faça um programa que receba o salário base e o tempo de serviço de um funcionário. Calcule e mostre:

* O imposto, apresentado na tabela a seguir.

| SALÁRIO BASE                        | % SOBRE O SALÁRIO BASE |
|-------------------------------------|------------------------|
| < R$ 200,00                         | isento                 |
| Entre R$ 200,00(inc) e R$ 450(inc)  | 3%                     |
| Entre R$ 450,00 e R$ 700,00         | 8%                     |
| >= R$ 700,00                        | 12%                    |

* A gratificação, que se encontra na tabela abaixo.

```
+------------------+------------------------------------------------------+
| SALÁRIO BASE     | TEMPO DE SERVIÇO                       GRATIFICAÇÃO  |
+------------------+------------------------------------------------------+
|    SUPERIOR a    | Até 3 anos                                  20       |
|    R$ 500,00     | Mais de 3 anos                              30       |
+------------------+------------------------------------------------------+
|                  | Até 3 anos                                  23       |
|  Até R$ 500,00   | Entre 3 e 6 anos                            35       |
|                  | De 6 anos para cima                         33       |
+------------------+------------------------------------------------------+
```

* O salário líquido, ou seja, salário base menos imposto mais gratificação
* A categoria, que está na tabela a seguir

| SALÁRIO LÍQUIDO                     | CLASSIFICAÇÃO          |
|-------------------------------------|------------------------|
| Até R$ 350,00                       | A                      |
| Entre R$ 350,00 e R$ 600,00         | B                      |
| De R$ 600,00 para cima              | C                      |


```
DECLARE sal_base, tempo, imposto, grat NUMERICO
        sal_liq NUMERICO
LEIA sal_base, tempo

SE sal_base < 200
    imposto <- 0
SENAO SE sal_base <= 450
    imposto <- 3/100 * sal_base
SENAO SE sal_base < 700
    imposto <- 8/100 * sal_base
SENAO
    imposto <- 12/100 * sal_base

ESCREVA imposto

SE sal_base > 500
    SE tempo <= 3
        grat <- 20
    SENAO
        grat <- 30
SENAO
    SE temp <= 3
        grat <- 23
    SENAO SE tempo < 6
        grat <- 35
    SENAO <- 33

ESCREVA grat
sal_liq <- sal_base - imposto + grat
ESCREVA sal_liq

SE sal_liq <= 350
    ESCREVA "Classificação A"
SENAO SE sal_liq < 600
    ESCREVA "Classificação B"
SENAO
    ESCREVA "Classificação C"
```
----

**22** - Faça um programa que receba o valor do salário mínimo, o turno de trabalho (M - matutino, V - vespetino ou N - noturno), a categoria (O - operário, G - gerente) e o número de horas trabalhadas no mês de um funcionário. Suponha a digitação apenas de dados válidos e, quando houver digitação de letras, utilize maiúsculas. Calcule e mostre:

* O coeficiente do salário, de acordo com a tabela a seguir.

| TURNO DE TRABALHO                   | VALOR DO COEFICIENTE   |
|-------------------------------------|------------------------|
| M - Matutino                        | 10% do salario minimo  |
| V - Vespetino                       | 15% do salario minimo  |
| N - Noturno                         | 12% do salario minimo  |

* O valor do salário bruto, ou seja, o número de horas trabalhadas multiplicado pelo valor do coeficiente do usuário.
* O imposto, de acordo com a tabela a seguir

```
+-----------------+-------------------+--------------------------------+
|    CATEGORIA    |   SALÁRIO BRUTO   | IMPOSTO SOBRE O SALÁRIO BRUTO  |
+-----------------+-------------------+--------------------------------+
|                 | >= R$ 300,00      |              5%                |
|  O - Operário   | < R$ 300,00       |              3%                |
+-----------------+-------------------+--------------------------------+
|                 | >= R$ 400,00      |              6%                |
|  G - Gerente    | < R$ 400,00       |              4%                |
+-----------------+-------------------+--------------------------------+
```

* A gratificação, de acordo com as regras que seguem.

Se o funcionário preencher **todos** ps requisitos a seguir, sua gratificação será de R$ 50,00; caso contrário, será de R$ 30,00. Os requisitos são: <br />
**Turno:** Noturno <br />
**Número de horas trabalhadas:** Superior a 80 horas

* O auxílio alimentação, de acordo com as seguintes regras.

Se o funcionário preencher **algum** dos requisitos abaixo, seu auxílio alimentação será de um terço do seu salário bruto; caso contrário, será de metade do seu salário bruto. Os requisitos são:<br />
**Categoria:** Operário <br />
**Coeficiente do salário:** <= 25

* O salário líquido, ou seja, salário bruto menos imposto mais gratificação mais auxílio alimentação.
* A classificação, de acordo com a tabela a seguir.

| SALÁRIO LÍQUIDO                     | VALOR DO COEFICIENTE   |
|-------------------------------------|------------------------|
| Menor que R$ 350,00                 | Mal remunerado         |
| Entre R$ 350,00 e R$ 600,00         | Normal                 |
| Maior que R$ 600,00                 | Bem remunerado         |


```
DECLARE sal_min, nht, coeficiente, sal_bruto NUMERICO
        imposto, grat, auxilio, sal_liq NUMERICO
        turno, categoria STRING
LEIA sal_min, turno, categoria, nht

SE turno == "M":
    coeficiente <- 10/100 * sal_min
SE turno == "V"
    coeficiente <- 15/100 * sal_min
SE turno == "N":
    coeficiente <- 12/100 * sal_min

ESCREVA coeficiente
sal_bruto <- nht * coeficiente
ESCREVA sal_bruto

SE categoria == "O":
    SE sal_bruto >= 300
        imposto <- 5/100 * sal_bruto
    SENAO
        imposto <- 3/100 * sal_bruto
SENAO
    SE sal_bruto >= 400
        imposto <- 6/100 * sal_bruto
    SENAO
        imposto <- 4/100 * sal_bruto

ESCREVA imposto

SE turno == "N" E nht > 80
    grat <- 50
SENAO
    grat <- 30
    
SE categoria = "O" OU coeficiente <= 25
    auxilio <- 1/3 * sal_bruto
SENAO
    auxilio <- 1/2 * sal_bruto

ESCREVA auxilio
sal_liq <- sal_bruto - imposto + grat + auxilio
ESCREVA sal_liq

SE sal_liq < 350
    ESCREVA "Mal Remunerado"
SE sal_liq >= 350 E sal_liq <= 600
    ESCREVA "Normal"
SE sal_liq > 600
    ESCREVA "Bem Remunerado"
```

----

**23** - Faça um programa que receba o preço, o tipo(A - alimentação, L - limpeza e V - vestuário) e a refrigeração(S - produto que necessita de refrigeração e N - produto que não necessita de refrigeração) de um produto. Suponha que haverá apenas a digitação de dados válidos e, quando houver digitação de letras, utilize maiúsculas. Calcule e mostre:

* O valor adicional, de acordo com a tabela a seguir.

<img src="http://i.imgur.com/GpssyIC.png" />

* O valor do imposto, de acordo com a regra a seguir.

| PREÇO                | PERCENTUAL SOBRE O PREÇO   |
|----------------------|----------------------------|
| < R$ 25,00           | 5%                         |
| >= R$ 25,00          | 8%                         |


* O preço de custo, ou seja, preço mais imposto.
* O desconto, de acordo com a regra a seguir.

O produto que **não** preencher nenhum dos requisitos abaixo terá desconto de 3% , caso contrário, 0(zero). Os requisitos são: <br />
**Tipo:** A <br />
**Refrigeração:** S

* O novo preço, ou seja, preço de custo mais adicional menos desconto.
* A classificação, de acordo com a regra a seguir.

| NOVO PREÇO                    | CLASSIFICAÇÃO              |
|-------------------------------|----------------------------|
| <= R$ 50,00                   | Barato                     |
| Entre R$ 50,00 e R$ 100,00    | Normal                     |
| >= R$ 100,00                  | Caro                       |


```
DECLARE pre, valor_adic, imposto NUMERICO
        pre_custo, desconto, novo_pre NUMERICO
        tipo, refrig STRING

LEIA pre, tipo, refrig

SE refrig = "N"
    SE tipo = "A"
        SE pre < 15
            valor_adic <- 2
        SENAO
            valor_adic <- 5
    SE tipo = "L"
        SE pre < 10
            valor_adic <- 1,50
        SENAO
            valor_adic <- 2,50
    SE tipo = "V"
        SE pre < 30
            valor_adic <- 3
        SENAO
            valor_adic <- 2,5
SENAO
    SE tipo = "A"
        valor_adic <- 8
    SE tipo = "L"
        valor_adic <- 0
    SE tipo = "V"
        valor_adic <- 0
ESCREVA valor_adic

SE pre < 25
    imposto <- 5/100 * pre
SENAO
    imposto <- 8/100 * pre
ESCREVA imposto

pre_custo <- pre + imposto
ESCREVA pre_custo

SE tipo != "A" E refrig != "S"
    desconto <- 3/100 * pre_custo
SENAO
    desconto <- 0
ESCREVA desconto
novo_pre <- pre_custo + valor_adic - desconto
ESCREVA novo_pre

SE novo_pre <= 50
    ESCREVA "Barato"
SENAO SE novo_pre < 100
    ESCREVA "Normal"
SENAO
    ESCREVA "Caro"
```

----

**24** - Faça um programa que receba a medida de um ângulo em graus. Calcule e mostre o quadrante em que se localiza esse ângulo. Considere os quadrantes da trigonometria e, para ângulos maiores que 360° ou menores que -360°, reduzi-los, mostrando também o número de voltas e o sentido da volta(horário ou anti-horário).

```
DECLARE angulo, volta NUMERICO
LEIA angulo

SE angulo > 360 OU angulo < -360
    voltas <- angulo / 360
    angulo <- RESTO(angulo / 360)
SENAO
    voltas <- 0

SE angulo == 0 OU angulo == 90 OU angulo == 180 OU angulo == 270 OU angulo == 360 OU angulo == -90 OU angulo == -180 OU angulo == -270 OU angulo == -360
    ESCREVA "Está em cima de algum dos eixos"
SE (angulo > 0 E angulo < 90) OU (angulo < -270 E angulo > -360)
    ESCREVA "1° quadrante"
SE (angulo > 90 E angulo < 180) OU (angulo < -180 E angulo > -270)
    ESCREVA "2° quadrante"
SE (angulo > 180 E angulo < 270) OU (angulo < -90 E angulo > -180)
    ESCREVA "3° quadrante"
SE (angulo > 270 E angulo < 360) OU (angulo < 0 E angulo > -90)
    ESCREVA "4° quadrante"
ESCREVA voltas, " volta(s)" no sentido "
SE angulo < 0
    ESCREVA "horário"
SENAO
    ESCREVA "anti-horário"
```