"""
**10** - Faça um programa que receba o salário atual de um funcionário e, usando a tabela a seguir, calcule e mostre o valor
do aumento e o novo salário.

| SALÁRIO                       | PERCENTUAL DE AUMENTO                |
|-------------------------------|--------------------------------------|
| Até R$ 300,00                 | 15%                                  |
| R$ 300,00 °----* R$ 600,00    | 10%                                  |
| R$ 600,00 °----* R$ 900,00    | 5%                                   |
| Acima de R$ 900,00            | 0%                                   |
"""
salario_atual = float(input("Digite o valor do seu salário atual: "))

if (salario_atual < 300):
	print("Você recerá um aumento de %.2f e seu novo salário será %.2f." % ((salario_atual * 0.15), (salario_atual + (salario_atual * 0.15))))

elif (salario_atual < 600):
	print("Você recerá um aumento de %.2f e seu novo salário será %.2f." % ((salario_atual * 0.10), (salario_atual + (salario_atual * 0.10))))

elif (salario_atual < 900):
	print("Você recerá um aumento de %.2f e seu novo salário será %.2f." % ((salario_atual * 0.05), (salario_atual + (salario_atual * 0.05))))

else:
        print("Não houve aumento para sua faixa salárial, seu salário continua %.2f" % (salario_atual))
