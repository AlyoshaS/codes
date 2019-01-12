# Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.

valor_em_real = int(input("Digite aqui o valor em real: "))

cotacao_dolar = 3.14
conversao_dolar = (valor_em_real / cotacao_dolar)
conversao = round(conversao_dolar, 2)

print("O valor em dólar é:", conversao)
