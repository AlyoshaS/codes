"""
**13** - Faça um programa que receba o salário de um funcionário e, usando a tabela a seguir, calcule e mostre o novo salário.

| FAIXA SALARIAL                         | % DE AUMENTO                         |
|----------------------------------------|--------------------------------------|
| Até R$ 300,00                          | 50%                                  |
| R$ 300,00 °----* R$ 500,00             | 40%                                  |
| R$ 500,00 °----* R$ 700,00             | 30%                                  |
| R$ 700,00 °----* R$ 800,00             | 20%                                  |
| R$ 800,00 °----* R$ 1.000,00           | 10%                                  |
| Acima de R$ 1.000,00                   | 5%                                   |
"""
salario = float(input("Digite o valor do salário atual: "))

if (salario < 300):
	print("Seu salário líquido será de R$ %.2f." % (salario + (salario * 0.50)))

elif (salario <= 500):
	print("Seu salário líquido será de R$ %.2f." % (salario + (salario * 0.40)))

elif (salario <= 700):
	print("Seu salário líquido será de R$ %.2f." % (salario + (salario * 0.30)))

elif (salario <= 800):
	print("Seu salário líquido será de R$ %.2f." % (salario + (salario * 0.20)))

elif (salario <= 1000):
	print("Seu salário líquido será de R$ %.2f." % (salario + (salario * 0.10)))

else:
	print("Seu salário líquido será de R$ %.2f." % (salario + (salario * 0.05)))
