"""
12. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:

a idade dessa pessoa em anos;
a idade dessa pessoa em meses;
a idade dessa pessoa em dias;
a idade dessa pessoa em semanas.
"""
ano_nasc, ano_atual = [int(x) for x in input("Digite seu ano de nascimento e o ano atual: ").split()]

idade_anos = ano_atual - ano_nasc
idade_meses = idade_anos * 12
idade_dias = idade_meses * 30
idade_semanas = idade_dias / 7
                 
print("A idade em anos é: ", idade_anos)
print("A idade em meses é: ", idade_meses)
print("A idade em dias é: ", idade_dias)
print("A idade em semanas é: ", idade_semanas)

