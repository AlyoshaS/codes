# Estruturas Sequenciais

### 1 - Faça um programa que receba quatro números inteiros, calcule e mostre a soma desses números

**Algoritmo**

```
ALGORITMO
    DECLARE n1, n2, n3, n4, soma NUMÉRICO
    LEIA n1, n2, n3, n4

    soma <- n1 + n2 + n3 + n4
    
    ESCREVA soma
FIM_ALGORITMO
```

### 2 - Faça um programa que receba três notas, calcule e mostre a média aritimética entre elas

**Algoritmo**

```
ALGORITMO
    DECLARE nota1, nota2, nota3, média NUMÉRICO
    LEIA nota1, nota2, nota3
    
    media <- (nota1 + nota2 + nota3) / 3
    
    ESCREVA media
FIM_ALGORITMO
```
**Algoritmo 1**

```
ALGORITMO
    DECLARE nota1, nota2, nota3, média NUMÉRICO
    LEIA nota1, nota2, nota3
    
    soma <- nota1 + nota2 + nota3
    media <- soma / 3
    
    ESCREVA media
FIM_ALGORITMO
```

### 3 - Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas

**Algoritmo**

```
ALGORITMO
    DECLARE nota1, nota2, nota3, peso1, peso2, peso3, media NUMÉRICO
    LEIA nota1, nota2, nota3, peso1, peso2, peso3
    
    media <- (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    
    ESCREVA media
FIM_ALGORITMO
```

**Algoritmo 1**

```
ALGORITMO
    DECLARE nota1, nota2, nota3, peso1, peso2, peso3, media NUMÉRICO
    LEIA nota1, nota2, nota3, peso1, peso2, peso3
    
    soma1 <- nota1 * peso1
    soma2 <- nota2 * peso2
    soma3 <- nota3 * peso3
    total <- peso1 + peso2 + peso3
    media <- (soma1 + soma2 + soma3) / total
    
    ESCREVA media
FIM_ALGORITMO
```

### 4 - Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%

**Algoritmo**

```
ALGORITMO
    DECLARE sal, novosal NUMÉRICO
    LEIA sal
    
    novosal <- sal + (sal * 25 / 100)
    
    ESCREVA novosal
FIM_ALGORITMO
```
**Algoritmo 1**

```
ALGORITMO
    DECLARE sal, novosal NUMÉRICO
    LEIA sal
    aumento <- sal * 25/100
    novosal = sal + aumento
    ESCREVA novosal
FIM_ALGORITMO
```

### 5 - Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor de aumento e novo salário

**Algoritmo**

```
ALGORITMO
    DECLARE sal, perc, aumento, novosal NUMÉRICO
    LEIA sal, perc
    aumento <- sal * perc/100
    ESCREVA aumento
    novosal <- sal + aumento
    ESCREVA novosal
FIM_ALGORITMO
```

### 6 - Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% sobre este salário

**Algoritmo**

```
ALGORITMO
    DECLARE sal, salreceber, grat, imp NUMÉRICO
    LEIA sal
    grat <- sal * 5/100
    imp <- sal * 7/100
    salreceber <- sal + grat - imp
    ESCREVE salreceber
FIM_ALGORITMO
```

### 7 - Faça um programa que receba o salário base de um funcionári, calcule e mostre o seu salário a receber, sabendo-se que o funcionário tem gratificação de R$50 e paga imposto de 10% sobre o salário base

**Algoritmo**

```
ALGORITMO
    DECLARE sal, salreceber, imp NUMÉRICO
    LEIA sal
    imp <- sal * 10/100
    salreceber <- sal + 50 - imp
    ESCREVA salreceber
FIM_ALGORITMO
```

### 8 - Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento

**Algoritmo**

```
ALGORITMO
    DECLARE dep, taxa, rend, total NUMÉRICO
    LEIA dep, taxa
    rend <- dep * taxa / 100
    total <- dep + rend
    ESCREVA rend
    ESCREVA total
FIM_ALGORITMO
```

### 9 - Faça um programa que calcule e mostre a área de um triangulo. Sabe-se que: Área = (base * altura) / 2

**Algoritmo**

```
ALGORITMO
    DECLARE base, altura, area NUMÉRICO
    LEIA base, altura
    area = (base * altura) / 2
    ESCREVA area   
FIM_ALGORITMO
```

### 10 - Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = PI * R²

```
ALGORITMO
    DECLARE area, raio NUMÉRICO
    LEIA raio
    area <- 3.1415 * raio²
    ESCREVA area
FIM_ALGORITMO
```

### 11 - Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
* o número digitado ao quadrado;
* o número digitado ao cubo;
* a raiz quadrada do número digitado;
* a raiz cúbica do número digitado;

**Algoritmo**

```
ALGORITMO
    DECLARE num, quad, cubo, r2, r3 NUMÉRICO
    LEIA num
    quad <- num²
    cubo <- num³
    r2 <- ²√num
    r3 <- ³√num
    ESCREVA quad, cubo, r2, r3
FIM_ALGORITMO
```

### 12 - Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro

**Algoritmo**

```
ALGORITMO
    DECLARE num1, num2, r1, r2 NUMÉRICO
    LEIA num1, num2

    r1 <- num1 ** num2
    r2 <- num2 ** num1
    
    ESCREVA r1, r2
FIM_ALGORITMO
```

### 13 - Sabe-se que: 1 pé = 12 polegadas; 1 jarda = 3 pés; 1 milha = 1.760 jardas. Faça um programa que receba a medida em pés, faça as conversões a seguir e mostre os resultados.

* polegadas
* jardas 
* milhas

**Algoritmo**

```
ALGORITMO
    DECLARE pes, polegadas, jardas, milhas NUMÉRICO
    LEIA pes

    polegadas <- pes * 12
    jardas <- pes / 3
    milhas <- jardas / 1760
    
    ESCREVA polegadas, jardas, milhas
FIM_ALGORITMO
```

### 14 - Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:

* a idade da pessoa
* quantos anos ela terá em 2050

**Algoritmo**

```
ALGORITMO
	DECLARE ano_atual, ano_nascimento, idade_atual, idade_2050 NUMÉRICO
	LEIA ano_atual
	LEIA ano_nascimento

	idade_atual <- ano_atual - ano_nascimento
	idade_2050 <- 2050 - ano_nascimento
	
	ESCREVA idade_atual
	ESCREVA idade_2050	
FIM_ALGORITMO
```

### 15 - O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:

* o valor correspondente ao lucro do distribuidor;
* o valor correspondente aos impostos;
* o preço final do veículo.

**Algoritmo**

```
ALGORITMO
	DECLARE p_fab, perc_d, perc_i, vlr_d, vlr_i, p_final NUMÉRICO
	LEIA p_fab
	LEIA perc_d
	LEIA perc_i
	
	vlr_d <- p_fab * perc_d / 100
	vlr_i <- p_fab * perc_i / 100
	p_final <- p_fab + vlr_d + vlr_i
	
	ESCREVA vlr_d
	ESCREVA vlr_i
	ESCREVA p_final
FIM_ALGORITMO
```

### 16 - Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e mostre o salário a receber seguindo estas regras:

* a hora trabalhada vale a metade do salário mínimo.
* o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
* o imposto equivale a 3% do salário bruto.
* o salário a receber equivale ao salário bruto menos o impostos

**Algoritmo**

```
ALGORITMO
	DECLARE horas_t, vlr_sal_min, vlr_hora_t vlr_sal_bru, imp, vlr_sal_liq NUMÉRICO
	LEIA horas_t
	LEIA vlr_sal_min
	
	vlr_hora_t <- vlr_sal_min / 2
	vlr_sal_bru <- vlr_hora_t * horas_t
	imp <- vlr_sal_bru * 3 / 100
	vlr_sal_liq <- vlr_sal_bru - imposto
	
	ESCREVA vlr_sal_liq
FIM_ALGORITMO
```

### 17 - Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% e o saldo inicial da conta está zerado.

**Algoritmo**

```
ALGORITMO
	DECLARE salario, cheque1, cheque2, cpmf1, cpmf2, saldo NUMÉRICO
	LEIA salario
	LEIA cheque1
	LEIA cheque2
	
	cpmf1 <- cheque1 * 0.38 / 100
	cpmf2 <- cheque2 * 0.38 / 100
	saldo <- salario - cheque1 - cheque2 - cpmf1 - cpmf2
	
	ESCREVA saldo
FIM_ALGORITMO
```

### 18 - Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.

**Algoritmo**

```
ALGORITMO
	DECLARE peso_saco, racao_gato1, racao_gato2, total_final NUMÉRICO
	LEIA peso_saco
	LEIA racao_gato1
	LEIA racao_gato2
	
	racao_gato1 <- racao_gato1 / 1000
	racao_gato2 <- racao_gato2 / 1000
	total_final <- peso_saco - 5 * (racao_gato1 + racao_gato2)
	
	ESCREVA total_final
FIM_ALGORITMO
```

### 19 - Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que o usuário deseja alcançar subindo a escada, calcule e mostre quantos degraus ele deverá subir para atingir seus objetivo, sem se preocupar com a altura do usuário. Todas as medidas fornecidas devem estar em metros.

**Algoritmo**

```
ALGORITMO
	DECLARE a_degrau, a_usuario, qtd_degraus NUMÉRICO
	LEIA a_degrau
	LEIA a_usuario
	
	qtd_degraus <- a_usuario / a_degrau
	
	ESCREVA qtd_degraus
FIM_ALGORITMO
```

### 20 - Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão e econstada na parede e a altura da parede onde está a ponta da escada, calcule e mostre a medida desta escada. [imginfo](http://i.imgur.com/AaWpmRQ.png)

**Algoritmo**

```
ALGORITMO
	DECLARE ang, alt, escada, radiano NUMÉRICO
	LEIA ang
	LEIA alt
	
	radiano <- ang * 3.14 / 180
	escada <- alt / seno(radiano)
	
	ESCREVA escada
FIM_ALGORITMO
```

### 21 - Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência, calcule e mostre:

* o valor de cada quilowatt;
* o valor a ser pago por essa residência; 
* o valor a ser pago com desconto de 15%

```
ALGORITMO
	DECLARE vlr_sal, qtd_kw, vlr_kw, vlr_reais, desc, vlr_desc NUMÉRICO
	LEIA vlr_sal
	LEIA qtd_kw
	
	vlr_kw <- vlr_sal / 5
	vlr_reais <- vlr_kw * qtd_kw
	desc <- vlr_reais * 15 / 100
	vlr_desc <- vlr_reais - 100
	
	ESCREVA vlr_kw
	ESCREVA vlr_reais
	ESCREVA vlr_desc
FIM_ALGORITMO
```

### 22 - Faça um programa que receba um número real, calcule e mostre:

* a parte inteira desse número;
* a parte fracionária desse número;
* o arredondamento desse número

**Algoritmo**

```
ALGORITMO
	DECLARE num, i, f, a NUMÉRICO
	LEIA num
	
	i <- parte inteira de num
	f <- num - i
	a <- arredonda(num)
	
	ESCREVA i
	ESCREVA f
	ESCREVA a
FIM_ALGORITMO
```

### 23 - Faça um programa que receba uma hora formada por hora e minutos(um número real), calcule e mostre a hora digitada apenas em minutos. Lembre-se de que:

* para quatro e meia, deve-se digitar 4.30;
* os minutos vão de 0 a 59

**Algoritmo**

```
ALGORITMO
	DECLARE hora, h, m, conversao NUMÉRICO
	LEIA hora
	
	h <- pegar parte inteira da variável hora
	m <- hora - h
	conversao <- (h * 60) + (m * 100)
	
	ESCREVA conversao
FIM_ALGORITMO
```

### 24 - Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deverá calcular e mostar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado

**Algoritmo**

```
ALGORITMO
	DECLARE custo, convite, qtd NUMÉRICO
	LEIA custo
	LEIA convite
	
	qtd <- custo / convite
	
	ESCREVA qtd
FIM_ALGORITMO
```

## Exercícios Propostos

1. Faça um programa que receba dois números, calcule e mostre a subtração do primeiro número pelo segundo.

2. Faça um programa que receba três núemros, calcule e mostre a multiplicação desses números.

3. Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar com validações.

4. Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira e peso 3 para a segunda.

5. Faça um programa que receba o peso de uma pessoa, calcule e mostre:
   * o novo peso, se a pessoa engordar 15% sobre o peso digitado;
   * o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

6. Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.

7. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = ((base maior + base menor) * altura) / 2

8. Faça um programa que calcule e mostre a área de um quadrado. Sabe-se que: A = lado * lado

9. Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * diagonal menor) / 2

10. Faça um programa que receba o valor so salário mínimo e o valor do salário de um funcionário, calcule e mostre a quantidade de salários mínimos que esse funcionário ganha.

11. Faça um programa que calcule e mostre a tabuada de um número digitado pelo usuário.

12. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
    * a idade dessa pessoa em anos;
    * a idade dessa pessoa em meses;
    * a idade dessa pessoa em dias;
    * a idade dessa pessoa em semanas.

13. João recebeu seu salário e precisa pagar duas contas atrasadas. Por causa do atraso, ele deverá pagar multa de 2% sobre cada conta. Faça um programa que calcule o mostre quanto restará do salário de João.

14. Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.

15. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e seu salário final.

16. Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

17. Faça um programa que receba o raio, calcule e mostre:
    * o comprimento de uma esfera; sabe-se que C = 2 * PI * R;
    * a área de uma esfera; sabe-se que A = PI * R²;
    * o volume de uma esfera; sabe-se que V = 3/4 * PI * R³.

18. Faça um programa que receba uma temperatura em Celcius, calcule e mostre essa temperatura em Fahrenheit. Sabe-se que F = 180 * (C + 32) / 100.

19. Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m² deve-se usar 18 W de potência. Faça um programa que receba as duas dimensões de um cômodo(em metros), calcule e mostre a sua área(em m²) e a potência de iluminação que deverá ser utilizada.

20. Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de horas extras trabalhadas, calcule e mostre o salário a receber, seguindo as regras abaixo:
    * a hora trabalhada vale 1/8 do salário mínimo;
    * a hora extra vale 1/4 do salário mímino;
    * o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
    * a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra;
    * o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras
    
21. Faça um programa que receba o número de lados de um polígono convexo, calcule e mostre o número de diagonais desse polígono. Sabe-se que ND = N * (N - 3) / 2, onde N é o número de lados do polígono.

22. Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo. Sabe-se que a soma dos ângulos de um triângulo é 180 graus.

23. Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui. Ela vai passar por vários países e precisa converter seu dinheiro em dólares, marco alemão e libra esterlina. Sabe-se que a cotação do dólar é de R$ 1,80, do marco alemão é de R$ 2,00 e da libra esterlina é de R$ 1,57. O programa deve fazer as conversões e mostrá-las.

24. Faça um programa que receba a hora(uma variável para hora e outra para minutos), calcule e mostre:
    * a hora digitada convertida em minutos;
    * o total dos minutos, ou seja, os minutos digitados mais a conversão do anterior;
    * o total dos minutos convertidos em segundos.


























