"""
20. Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de horas extras trabalhadas, calcule e mostre o salário a receber,
seguindo as regras abaixo:
a hora trabalhada vale 1/8 do salário mínimo;
a hora extra vale 1/4 do salário mímino;
o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra;
o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras
"""

horas_trab, vlr_sal_min, qtd_hora_extra = [int(x) for x in input("Digite a quantidade de horas trabalhadas, o valor do salário mínimo e a quantidade de hora extra: ").split()]

vlr_hora = vlr_sal_min / 8
vlr_hr_extra = vlr_sal_min / 4
sal_bruto = horas_trab * vlr_hora
hora_extra = qtd_hora_extra * vlr_hr_extra
salario = sal_bruto + hora_extra

print("O salário à receber é de: R$", salario)
















