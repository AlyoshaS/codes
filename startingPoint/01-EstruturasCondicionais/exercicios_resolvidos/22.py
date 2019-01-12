"""
22 - Faça um programa que receba:
  * O código do produto comprado;
  * A quantidade comprada do produto.
  
Calcule e mostre:

  * O preço unitário do produto comprado, seguindo a Tabela I;
  * O preço total da nota;
  * O valor do desconto, seguindo a tabela II e aplicado sobre o preço total da nota;
  * O preço final da nota depois do desconto.

  **TABELA I**

| CÓDIGO                     | PREÇO           |
|----------------------------|-----------------|
| 1 a 10                     | R$ 10,00        |
| 11 a 20                    | R$ 15,00        |
| 21 a 30                    | R$ 20,00        |
| 31 a 40                    | R$ 30,00        |

**TABELA II**

| PREÇO TOTAL DA NOTA          | % DE DESCONTO   |
|------------------------------|-----------------|
| Até R$ 250,00                | 5%              |
| Entre R$ 250,00 e R$ 500,00  | 10%             |
| Acima de R$ 500,00           | 15%             |
"""
codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

if codigo <= 10:
    preco_total = quantidade * 10.00
    print("O preço unitário do produto é R$%.2f. O preço total da nota, sem desconto, é R$%.2f." %(10.00, preco_total))
elif codigo <= 20:
    preco_total = quantidade * 15.00
    print("O preço unitário do produto é R$%.2f. O preço total da nota, sem desconto, é R$%.2f." %(15.00, preco_total))
elif codigo <= 30:
    preco_total = quantidade * 20.00
    print("O preço unitário do produto é R$%.2f. O preço total da nota, sem desconto, é R$%.2f." %(20.00, preco_total))
elif codigo <= 40:
    preco_total = quantidade * 30.00
    print("O preço unitário do produto é R$%.2f. O preço total da nota, sem desconto, é R$%.2f." %(30.00, preco_total))
else:
    preco_total = None
    print("Código de produto invalido, por favor digite um código válido.")

if preco_total == None:
    print("Sem um código de produto válido, o preço final da nota não pode ser definido.")
elif preco_total < 250:
    print("Com desconto de R$%.2f, o preço final da nota é R$%.2f." %(preco_total * 0.05, preco_total - (preco_total * 0.05)))
elif preco_total <= 500:
    print("Com desconto de R$%.2f, o preço final da nota é R$%.2f." %(preco_total * 0.10, preco_total - (preco_total * 0.10)))
else:
    print("Com desconto de R$%.2f, o preço final da nota é R$%.2f." %(preco_total * 0.15, preco_total - (preco_total * 0.15)))
                                     
