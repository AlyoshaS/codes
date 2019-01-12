#!/usr/bin/python
# coding: latin-1
#16 - Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. Sabe-se que
#cada operação bancária de retirada paga CPMF de 0,38% e o saldo inicial da conta está zerado.

salario = int(input("Digite o valor do seu salário: R$"))
cheque1 = int(input("Digite o valor do primeiro cheque: R$"))
cheque2 = int(input("Digite o valor do segundo cheque: R$"))

cpmf1 = cheque1 * 0.38 / 100
cpmf2 = cheque2 * 0.38 / 100
saldo = salario - cheque1 - cheque2 - cpmf1 - cpmf2

saldo = round(saldo, 2)

print("O seu saldo será: R$", saldo)
