"""
13. João recebeu seu salário e precisa pagar duas contas atrasadas. Por causa do atraso, ele deverá pagar multa de 2% sobre cada conta. Faça um programa que calcule
o mostre quanto restará do salário de João.
"""


val_sal, conta1, conta2 = [float(x) for x in input("Digite o valor do seu salario, da primeira conta e da segunda conta a pagar: ").split()]

juros1 = conta1 * 2 / 100
juros2 = conta2 * 2 / 100
salario = val_sal - (juros1 + conta1) - (juros2 + conta2)

print("Neste mês, sobrará do seu salário o valor de: R$", salario)















