# 1. Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão tirar para serem aprovados, considerando que a média exibida é 6,0.

#MÉDIA ARITMÉTICA	MENSAGEM
#0,0 +-----------+ 3,0	Reprovado
#3,0 +----------+ 7,0	Exame
#7,0 +-----------\* 10,0	Aprovado


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
media = round(media, 2)

print("A média aritimética é: ", media)

if media >= 0 and media < 3:
    print("reprovado.")
if media >= 3 and media < 7:
    print("Exame.")
    nota_exame = 12 - media
    print("Deve tirar nota", nota_exame, "para ser aprovado")
if media >=7 and media <= 10:
    print("Aprovado!")
