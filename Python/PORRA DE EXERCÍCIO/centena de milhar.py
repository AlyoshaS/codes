# Faça um Programa que leia um número inteiro menor que 1.000.000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

numero = (input("Digite um numero menor que 1.000.000: "))
qt_numero = len(numero)

if qt_numero == 6:
    centena_de_milhar = numero [0:1]
    dezena_de_milhar = numero [1:2]
    unidade_de_milhar = numero [2:3]
    centena = numero [3:4]
    dezena = numero [4:5]
    unidade = numero [5:6]
    print("Centena de milhar {0}, dezena de milhar {1}, unidade de milhar {2}, centena {3}, dezena {4} e unidade {5}.".format(centena_de_milhar, dezena_de_milhar, unidade_de_milhar, centena, dezena, unidade))
                                                                                                                              
if qt_numero == 5:
    dezena_de_milhar = numero [0:1]
    unidade_de_milhar = numero [1:2]
    centena = numero [2:3]
    dezena = numero [3:4]
    unidade = numero [4:5]
    print("Dezena de milhar {0}, unidade de milhar {1}, centena {2}, dezena {3} e unidade {4}.".format(dezena_de_milhar, unidade_de_milhar, centena, dezena, unidade))
                                                                                                                              
if qt_numero == 4:
    unidade_de_milhar = numero [0:1]
    centena = numero [1:2]
    dezena = numero [2:3]
    unidade = numero [3:4]
    print("Unidade de milhar {0}, centena {1}, dezena {2} e unidade {3}.".format(unidade_de_milhar, centena, dezena, unidade))

if qt_numero == 3:
    centena = numero [0:1]
    dezena = numero [1:2]
    unidade = numero [2:3]
    print("Centena %s, dezena %s e unidade %s" % (centena, dezena, unidade))

if qt_numero == 2:
    dezena = numero [0:1]
    unidade = numero [1:2]
    print("Dezena {0} e unidade {1}.".format(dezena, unidade))

if qt_numero == 1:
    unidade = numero [0:1]
    print(unidade, "unidades.")
