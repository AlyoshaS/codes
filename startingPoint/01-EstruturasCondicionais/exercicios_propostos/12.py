""" 12 - Faça um programa que apresente o menu a seguir, permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. 
Verifique a possibilidade de opção inválida e não se preocupe com restrições, como salário negativo.
Menu de opções:
Imposto
Novo salario
Classificação
Digite a opção desejada

Na opção 1: Receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras a seguir:
SALÁRIO	PERCENTUAL DO IMPOSTO
Menor que R$ 500,00	5%
de R$ 500,00 a R$ 850,00	10%
Acima de R$ 850,00	15%

Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor do novo saláriom usando as regras a seguir:
SALÁRIO	AUMENTO
De R$ 750,00(inclusive) a R$ 1.500,00(inclusive)	R$ 50,00
De R$ 450,00(inclusive) a R$ 750,00	R$ 75,00
Menor que R$ 450,00	R$ 100,00

Na opção 3: receber o salário de um funcionário e mostrar sua classificação usando a tabela a seguir:
SALÁRIO	Classificação
Até R$ 750,00(inclusive)	Mal remunerado
Maiores que R$ 750,00	Bem remunerado
"""

# DEFINE OS PERCENTUAIS DE IMPOSTO
percentual_imp_5 = 0.05
percentual_imp_10 = 0.10
percentual_imp_15 = 0.15

# DEFINE OS VALORES DE AUMENTO
aumento_25 = 25
aumento_50 = 50
aumento_75 = 75
aumento_100 = 100

# DEFINE A CLASSIFICAÇÃO
classificado_message_bad = "Mal remunerado"
classificado_message_good = "Bem remunerado"

print("+══════════════════+")
print("║Menu de opções:   ║")
print("║1. Imposto        ║")
print("║2. Novo salário   ║")
print("║3. Classificação. ║")
print("+══════════════════+")

op = int(input("Digite a opção desejada: "))

if(op == 1):
    salario = int(input("Digite o valor do salário: "))
    if salario < 500:
        imposto = salario * percentual_imp_5
    if salario >= 500 and salario <= 850:
        imposto = salario * percentual_imp_10
    if salario > 850:
        imposto = salario * percentual_imp_15
    print("O valor imposto é R$", imposto)

if(op == 2):
    salario = int(input("Digite o valor do salário: "))
    if salario > 1500:
        aumento = aumento_25
    if salario >= 750 and salario <= 1500:
        aumento = aumento_50
    if salario >= 450 and salario < 750:
        aumento = aumento_75
    if salario < 450:
        aumento = aumento_100
    novo_salario = salario + aumento
    print("Se novo salário será R$", novo_salario)

if(op == 3):
    salario = int(input("Digite o valor do salário: "))
    if salario <= 700:
        print(classificado_message_bad)
    if salario > 700:
        print(classificado_message_good)

elif(op < 1) or (op > 3):
    print("Opção inválida!")
    

