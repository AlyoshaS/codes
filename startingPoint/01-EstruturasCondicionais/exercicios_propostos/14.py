""" 14 - Faça um programa que receba o valor do salário mínimo, o número de horas trabalhadas, o número de dependentes do funcionário e a quantidade de horas extras trabalhadas. 
Calcule e mostre o salário a receber do funcionário de acordo com as regras a seguir:

O valor da hora trabalhada é igual a quinta parte do salário mínimo.
O salário do mês é igual ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
Para cada dependente, acrescentar R$ 32,00.
Para cada hora extra trabalhada, calcular o calor da hora trabalhada acrescida de 50%.
O salário bruto é igual ao salário do mês mais o valor dos dependentes mais o valor das horas extras.

Calcular o valor do imposto de renda retido na fonte de acordo com a tabela a seguir:
IRRF	SALÁRIO BRUTO
Isento	Inferior a R$ 200,00
10%	De R$ 200,00 até R$ 500,00
20%	Superior a R$ 500,00
O salário líquido é igual ao salário bruto menos IRRF.

A gratificação de acordo com a tabela a seguir:
SALÁRIO LÍQUIDO	GRATIFICAÇÃO
Até R$ 350,00	R$ 100,00
Superior a R$ 350,00	R$ 50,00

O salário a receber do funcionário é igual ao salário líquido mais a gratificação.
"""

# DEFINE O IMPOSTO DE RENDA
imposto_0 = 0
imposto_10 = 0.10
imposto_20 = 0.20

# DEFINE A GRATIFICACAO
gratificacao_100 = 100
gratificacao_50 = 50

salario_min = int(input("Digite o valor do salário mínimo: "))
numero_horast = int(input("Digite o número de horas trabalhadas: "))
dependentes = int(input("Digite o número de dependentes: ")) 
numero_horas_extrast = int(input("Digite o número de horas extras trabalhadas: "))

# DEFINE SALARIO BRUTO

valor_hora = 1 / 5 * salario_min
salario_mes = numero_horast * valor_hora
valor_dependentes = 32 * dependentes
valor_horae = numero_horas_extrast * (valor_hora + (valor_hora * 50 / 100))
salario_bruto = salario_mes + valor_dependentes  + valor_horae

# CALCULA IMPOSTO:

if(salario_bruto < 200):
    imposto = imposto_0

if(salario_bruto >= 200) and (salario_bruto <= 500):
    imposto = salario_bruto * imposto_10

if(salario_bruto> 500):
    imposto = salario_bruto * imposto_20

salario_liquido = salario_bruto - imposto

# CALCULA GRATIFICACAO:

if(salario_liquido <= 350):
    gratificacao = gratificacao_100

if(salario_liquido > 350):
    gratificacao = gratificacao_50

# DEFINE SALARIO A RECEBER:

salario_receber = salario_liquido + gratificacao
print("O salário à receber será: R$", salario_receber)
    
                            


    

