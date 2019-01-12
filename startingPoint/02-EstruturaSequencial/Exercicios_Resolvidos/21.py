"""
23. Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui. Ela vai passar por vários países e precisa converter seu dinheiro em dólares, marco alemão e libra esterlina. Sabe-se que a cotação do dólar é de R$ 1,80, do marco alemão é de R$ 2,00 e da libra esterlina é de R$ 1,57. O programa deve fazer as conversões e mostrá-las.
"""

dinheiro = int(input("Digite a quantidade de dinheiro disponível para a viagem: "))

#conversão

dolar = round(dinheiro * 1.80, 2)
marco_ale = round(dinheiro * 2, 2)
libra_est = round(dinheiro * 1.57, 2)

print("R$ {3} equivale a {0} em dólar, {1} em marco alemão e em libra esterlina {2}".format(dolar, marco_ale,libra_est, dinheiro))
















