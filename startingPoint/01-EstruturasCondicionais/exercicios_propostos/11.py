"""11 - Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargo estão na tabela abaixo.

CÓDIGO	CARGO	PERCENTUAL
1	Escrituário	50%
2	Secretário	35%
3	Caixa	20%
4	Gerente	10%
5	Diretor	Não tem aumento
"""

cargo = int(input("Digite o cargo do funcionário (1, 2, 3, 4 ou 5): "))
salario = int(input("Digite o valor do salário: "))

if(cargo == 1):
    print("O cargo é Escrituário.")
    aumento = salario * 50 / 100
    print("O valor do aumento é: ", aumento)
    novo_sal = salario + aumento
    print("O novo salário é ", novo_sal)

elif(cargo == 2):
          print("O cargo é Secretário.")
          aumento = salario * 35 / 100
          print("O valor do aumento é: ",aumento)
          novo_sal = salario + aumento
          print("O novo salario é ", novo_sal)

elif(cargo == 3):
          print("O cargo é Caixa")
          aumento = salario * 20 / 100
          print("O valor do aumento é: ",aumento)
          novo_sal = salario + aumento
          print("O novo salario é ", novo_sal)

elif(cargo == 4):
          print("O cargo é Gerente")
          aumento = salario * 10 / 100
          print("O valor do aumento é: ",aumento)
          novo_sal = salario + aumento
          print("O novo salario é ", novo_sal)

elif(cargo == 5):
          print("O cargo é Diretor")
          aumento = salario * 0 / 100
          print("O valor do aumento é: ",aumento)
          novo_sal = salario + aumento
          print("O novo salario é ", novo_sal)
            
          
else:
          print("Cargo inesistente!")
