"""
06 - Um empresa decide dar um aumento de 30% aos funcionários com salários inferiores a R$ 500,00. Faça um programa  que 
receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, caso ele não tenha direito ao aumento.
"""
salario = float(input("Digite o valor do seu salário: "))

print("O valor do novo salário é: R$ %.2f" % ((salario * 0.30) + salario) if salario <= 500 else "Você não tem direito a aumento.")
