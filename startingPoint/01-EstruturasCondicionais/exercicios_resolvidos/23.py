"""
23 - Faça um programa que receba o preço, a categoria(1 - limpeza, 2 - alimentação ou 3 - vestuário) e a situação(R - produtos que necessitam de
refrigeração e N - produtos que não necessitam de refrigeração).

Calcule e mostre:
  * O valor do aumento, usando as regras que se seguem.
  
  <img src="http://i.imgur.com/A8Z7FLQ.png" />
  
  * O valor do imposto, usando as regras a seguir.
  
    O produto que preencher **pelo menos** um dos seguintes requisitos pagará imposto equivalente a 5% do preço; caso contrário, pagará 8%. 
    Os requisitos são:
      * **Categoria:** 2
      * **Situação:** R
  
  * O novo preço, ou seja, o preço mais aumento menos imposto.
  * A classificação, usando as regras a seguir.
  
    | NOVO PREÇO                   | CLASSIFICAÇÃO   |
    |------------------------------|-----------------|
    | <= R$ 50,00                  | Barato          |
    | Entre R$ 50,00 e R$ 120,00   | Normal          |
    | >= R$ 120,00                 | Caro            |
"""
preco = float(input("Digite o preço do produto: "))
categoria = int(input("Digite a categoria (1- limpeza, 2- alimentação ou 3- vestuário): "))
situacao = input("Digite a situação(R- Refrigerado e N - não necessita refrigeração): ")

# Define e mostra o aumento:
if preco >= 25:
  if categoria == 1:
    aumento = preco * 0.05
    print("O valor do aumento é de R$%.2f" % (preco + aumento))
  elif categoria == 2:
    aumento = preco * 0.08
    print("O valor do aumento é de R$%.2f" % (preco + aumento))
  elif categoria == 3:
    aumento = preco * 0.10
    print("O valor do aumento é de R$%.2f" % (preco + aumento))
  else:
    categoria == None
    print("Categoria inválida")
else:
  if categoria == 1:
    print("O valor do aumento é de R$%.2f" % (preco + (preco * 0.12)))
  elif categoria == 2:
    print("O valor do aumento é de R$%.2f" % (preco + (preco * 0.15)))
  elif categoria == 3:
    print("O valor do aumento é de R$%.2f" % (preco + (preco * 0.18)))
  else:
    categoria == None
    print("Categoria inválida")

  """* O valor do imposto, usando as regras a seguir.
  
    O produto que preencher **pelo menos** um dos seguintes requisitos pagará imposto equivalente a 5% do preço; caso contrário, pagará 8%. 
    Os requisitos são:
      * **Categoria:** 2
      * **Situação:** R
      """
# Define e mostra valor do imposto:
if categoria == 2 or situacao == 'R':
  print("O valor do imposto é de R$%.2f" % ((preco * 0.05)))
else:
  print("O valor do imposto é de R$%.2f" % ((preco * 0.08)))



