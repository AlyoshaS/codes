"""
**07** - Faça um programa para calcular e mostrar o salário reajustado de um funcionário. O percentual de aumento encontra-se 
na tabela a seguir.

| SALÁRIO                       | PERCENTUAL DE AUMENTO                |
|-------------------------------|--------------------------------------|
| Até R$ 300,00                 | 35%                                  |
| Acima de R$ 300,00            | 15%                                  |
"""
salario = float(input("Digite o valor do seu salário: "))

print("O valor do novo salário é: R$ %.2f" % ((salario * 0.35) + salario) if salario <= 300 else "O valor do novo salário é: R$ %.2f" % ((salario * 0.15) + salario))
