"""
**14** - Uma agência bancária possui dois tipos de investimentos, conforme o quadro a seguir. Faça um programa que receba o tipo de investimento 
e seu valor e que calcule e mostre o valor corrigido, de acordo com o tipo de investimento.

| TIPO | DESCRIÇÃO            |  RENDIMENTO MENSAL  |
|------|----------------------|---------------------|
|1     | Poupança             | 3%                  |
|2     | Fundos de ordem fixa | 4%                  |
"""
investimento = int(input("Digite o tipo de investimento (1 para Poupança e 2 para Fundos de ordem fixa): "))
valor = float(input("Digite o valor do investimento: "))

print("O valor corrigido, de acordo com a opção %d, é de R$%.2f." % (investimento, valor + (valor * 0.03)) if investimento == 1 else "O valor corrigido, de acordo com a opção %d, é de R$%.2f." % (investimento, valor + (valor * 0.04)))

