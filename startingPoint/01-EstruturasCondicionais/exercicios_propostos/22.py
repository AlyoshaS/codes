"""22 - Faça um programa que receba o valor do salário mínimo, o turno de trabalho (M - matutino, V - vespetino ou 
N - noturno), a categoria (O - operário, G - gerente) e o número de horas trabalhadas no mês de um funcionário. 
Suponha a digitação apenas de dados válidos e, quando houver digitação de letras, utilize maiúsculas. Calcule e mostre:

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
"""

# Entrada de dados:
salario_minimo = int(input("Digite o salário mínimo: "))
turno_de_trabalho = input("Digite o turno de trabalho (Considere: M para matutino, V para vespetino ou N para noturno): ")
categoria = input("Digite a categoria (Considere: O para operário ou G para gerente): ")
horas_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))

# Define coeficiente do salario:
if turno_de_trabalho == 'M':
	coeficiente = .10 * salario_minimo
if turno_de_trabalho == 'V':
	coeficiente = .15 * salario_minimo
if turno_de_trabalho == 'N':
	coeficiente = .12 * salario_minimo
print("Valor do coeficiente do salário: R$", coeficiente)
salario_bruto = horas_trabalhadas * coeficiente
print("Valor do salário bruto: R$", salario_bruto)

# Define valor do imposto:
if categoria == 'O':
	if salario_bruto >= 300.00:
		imposto = .05 * salario_bruto
	else:
		imposto = .03 * salario_bruto
else:
	if salario_bruto >= 400.00:
		imposto = .06 * salario_bruto
	else:
		imposto = .04 * salario_bruto
print("Valor do imposto: R$", imposto)

# Define o valor da gratificacao:
if turno_de_trabalho == 'N' and horas_trabalhadas > 80:
	gratificacao = 50.00
else:
	gratificacao = 30.00
print("Valor da gratificação: R$", gratificacao)

# Define auxilio alimentacao:
if categoria == 'O' or coeficiente <= 25:
	auxilio_alimentacao =  round(.33 * salario_bruto, 2)
else:
	auxilio_alimentacao = round(0.5 * salario_bruto, 2)

print("Valor do auxílio: R$", auxilio_alimentacao)        
salario_liquido = salario_bruto - imposto + gratificacao + auxilio_alimentacao
print("Valor do salário líquido: ", salario_liquido)

# Define classificacao:
if salario_liquido < 350.00:
	print("Classificação: Mal remunerado.")
elif salario_liquido <= 600.00:
	print("Classificação: Normal.")
else:
	print("Classificação: Bem remunerado.")
	






