""" 13 - Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, acrescido de bonificação e auxílio escola.

SALÁRIO	CLASSIFICAÇÃO
Até R$ 500,00	5% do salário
Entre R$ 500,00 e R$ 1.200,00	12% do salário
Acima de R$ 1.200,00	Sem bonificação

SALÁRIO	AUXÍLIO ESCOLA
Até R$ 600,00	R$ 150,00
Mais que R$ 600,00	R$ 100,00
"""

# DEFINE A CLASSIFICAÇÃO DOS SALÁRIOS
percentual_sal_5 = 0.05
percentual_sal_12 = 0.12
percentual_sal_0 = 0

# DEFINE O AUXÍLIO ESCOLA
auxilio_150 = 150
auxilio_100 = 50

salario = int(input("Digite o valor do salário: "))

if(salario <= 500):
    bonificacao = salario * percentual_sal_5
elif(salario <= 1200):
    bonificacao = salario * percentual_sal_12
else:
    bonificacao = 0

if(salario <= 600):
    auxilio = auxilio_150
else:
    auxilio = auxilio_100

novo_salario = salario + bonificacao + auxilio
print("O novo salário será de: R$", novo_salario)
        
   

    

