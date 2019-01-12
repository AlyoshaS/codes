"""22 - Faça um programa que receba o salário base e o tempo de serviço de um funcionário. Calcule e mostre:

* O imposto, apresentado na tabela a seguir.

| SALÁRIO BASE                        | % SOBRE O SALÁRIO BASE |
|-------------------------------------|------------------------|
| < R$ 200,00                         | isento                 |
| Entre R$ 200,00(inc) e R$ 450(inc)  | 3%                     |
| Entre R$ 450,00 e R$ 700,00         | 8%                     |
| >= R$ 700,00                        | 12%                    |

* A gratificação, que se encontra na tabela abaixo.

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

* O salário líquido, ou seja, salário base menos imposto mais gratificação
* A categoria, que está na tabela a seguir

| SALÁRIO LÍQUIDO                     | CLASSIFICAÇÃO          |
|-------------------------------------|------------------------|
| Até R$ 350,00                       | A                      |
| Entre R$ 350,00 e R$ 600,00         | B                      |
| De R$ 600,00 para cima              | C                      |
""" 

# Entrada de dados:

salario_base = int(input("Digite o salário base: "))
tempo_servico = int(input("Digite o tempo de serviço: "))

# Define o imposto:

if salario_base < 200:
	imposto = 0
elif salario_base >= 200 and salario_base <= 450:
	imposto = salario_base * 0.03
elif salario_base > 450 and salario_base < 700:
	imposto = salario_base * 0.08
elif imposto = salario_base * 0.12

print("O valor do imposto é de: R$", imposto)

# Define gratificação:

if salario_base > 500:
	if tempo_servico <= 3:
		gratificacao = 20
	else tempo_servico > 3:
		gratificacao = 30
else:
	if tempo_servico <= 3:
		gratificacao = 23
	elif tempo_servico < 6:
		gratificacao = 35
	else:
		gratificacao = 33

salario_liquido = (salario_base - imposto) + gratificacao
print("O valor do salário líquido é: R$", salario_liquido)


# Define a categoria:

if salario_liquido <= 350:
	print("Classificação A.")
elif salario_liquido < 600:
	print("Classificação B.")
else:
	print("Classificação C.")