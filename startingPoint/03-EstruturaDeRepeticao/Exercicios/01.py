"""
01 - Um funcionário de uma empresa recebe aumento salario anualmente. Sabe-se que:
Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00.
Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
A partir de 2007(inclusive), os aumentos salariais sempre corresponderam a 1.3 do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.

DECLARE i, ano_atual, salario, novo_salario, percentual NUMERICO
LEIA ano_atual

salario <- 1000
percentual <- 1,5/100
novo_salario <- salario + percentual * salario

PARA i <- 2007 ATÉ ano_atual FAÇA
    percentual <- 1.3 * percentual
    novo_salario <- novo_salario + percentual * novo_salario

ESCREVA novo_salario
"""
ano_atual = int(input("Digite o ano atual: "))
salario = 1000
percentual = 0.015
novo_salario = salario + (percentual * salario)

for i in range(2007, ano_atual + 1):
	percentual = 1.3 * percentual
	novo_salario = salario + (percentual * salario)

print("Novo salário: R$%.2f" % novo_salario)
