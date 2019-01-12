#!/usr/bin/python
# coding: latin-1

"""
As tarifas de certo parque de estacionamento são as seguintes:
• 1ª e 2ª hora - R$ 1,00 cada
• 3ª e 4ª hora - R$ 1,40 cada
• 5ª hora e seguintes - R$ 2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas,
que é o mesmo que pagaria se tivesse permanecido 120 minutos.
Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representará “dez para a uma da tarde”.
Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo
estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas.
Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, antes significará que a partida
ocorreu no dia seguinte ao da chegada.
"""
hora_chegada, min_chegada = [int(x) for x in input("Digite a hora e minuto de chegada (** **  e ** **): ").split()]
hora_partida, min_partida = [int(x) for x in input("Digite a hora e minuto de saída (** **  e ** **): ").split()]

# Define horario:
if hora_chegada > hora_partida:
    hora_partida = hora_partida + 24
if min_chegada > min_partida:
    min_partida = min_partida + 60
    hora_partida = hora_partida - 1

min_final = min_partida - min_chegada
hora_final = hora_partida - hora_chegada

if hora_final >= 1:
    if min_final > 1:
        print("O carro ficou estacionado durante %d horas e %d minutos." % (hora_final, min_final))
    else:
        print("O carro ficou estacionado durante %d horas." % (hora_final))
else:
    print("O carro ficou estacionado durante %d minutos." % (min_final))

# Define valores:
min_total = int((hora_final * 60) + min_final)

if min_total <= 120:
    if min_total <= 60:
        preco = 1.00
        print("Preço total: R$%.2f." % (preco))
    else:
        preco = 2
        print("Preço total: R$%.2f." % (preco))
elif min_total <= 240:
    if min_total <= 180:
        preco = 2 + 1.40
        print("Preço total: R$%.2f." % (preco))
    else:
        preco = 2 + (1.40 * 2)
        print("Preço total: R$%.2f." % (preco))
else:
    hora_total = int(min_total // 60)
    preco = 4.40 + ((hora_total - 4) * 2)
    print("Preço total: R$%.2f." % (preco))


    while questao <= 3:
        resposta = input("Resposta da questão %d: " % (questao))
        if questao == 1 and resposta == "b":
            pontos = pontos + 1
        if questao == 2 and resposta == "a":
            pontos = pontos + 1
        if questao == 3 and resposta == "d":
            pontos = pontos + 1
        questao +=1

    print  ("O aluno fez %d ponto(s)" % pontos)
