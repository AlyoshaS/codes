"""
11 - Faça um promaga que receba o salário bruto de um funcionário e, usando a tabela a seguir, calcule e mostre o valor a receber. Sabe-se que
este é composto pelo salário do funcionário acrescido de gratificação e descontando o imposto de 7% sobre o salário sem gratificação.

| SALÁRIO                       | GRATIFICAÇÃO                         |
|-------------------------------|--------------------------------------|
| Até R$ 350,00                 | R$ 100,00                            |
| R$ 350,00 °----* R$ 600,00    | R$ 75,00                             |
| R$ 600,00 °----* R$ 900,00    | R$ 50,00                             |
| Acima de R$ 900,00            | R$ 35,00                             |
"""
salario_bruto = float(input("Digite o valor do salário bruto: "))

if (salario_bruto < 350):
	print("Seu salário líquido será de R$ %.2f." % ((salario_bruto + 100) - (salario_bruto * 0.07)))

elif (salario_bruto < 600):
	print("Seu salário líquido será de R$ %.2f." % ((salario_bruto + 75) - (salario_bruto * 0.07)))

elif (salario_bruto < 900):
	print("Seu salário líquido será de R$ %.2f." % ((salario_bruto + 50) - (salario_bruto * 0.07)))

else:
        print("Seu salário líquido será de R$ %.2f." % ((salario_bruto + 35) - (salario_bruto * 0.07)))
