# 10 - Faça um programa que receba o valor so salário mínimo e o valor do salário de um funcionário, calcule e mostre a quantidade de salários
# mínimos que esse funcionário ganha.

sal_minimo, sal_funcionario = [float(x) for x in input("Digite o valor do salário mínimo e o valor do seu salário; ").split()]

quant_sal_minimo = sal_funcionario / sal_minimo
quant_sal_minimo = round(quant_sal_minimo, 2)

print("Você recebe {0} salário(s) minimo(s)".format(quant_sal_minimo))

      

