#!/usr/bin/python
# coding: latin-1

"""15 - Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e mostre o salário a receber seguindo estas regras:
a hora trabalhada vale a metade do salário mínimo.
o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
o imposto equivale a 3% do salário bruto.
o salário a receber equivale ao salário bruto menos o impostos"""

horas_t = int(input("Digite as horas trabalhadas: "))
vlr_sal_min = int(input("Digite o valor do salário mínimo: "))

vlr_hora_t = (vlr_sal_min / 2)
vlr_sal_bru =  (vlr_hora_t * horas_t)
imp = vlr_sal_bru * (3 / 100)
vlr_sal_liq = vlr_sal_bru - imp

print("o valor do salário líquido é: R$", vlr_sal_liq)
