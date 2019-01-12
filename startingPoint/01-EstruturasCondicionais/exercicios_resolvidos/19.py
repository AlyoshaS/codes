"""
**19** - Faça um programa que receba a idade de um nadador e mostre sua categoria, usando as regras a seguir. Para idade inferior a 5,
deverá mostrar a mensagem.

| CATEGORIA                  | IDADE           |
|----------------------------|-----------------|
| Infantil                   | 5 a 7           |
| Juvenil                    | 8 a 10          |
| Adolescente                | 11 a 15         |
| Adulto                     | 16 a 30         |
| Sênior                     | acima de 30     |
"""
idade = int(input("Digite a idade do nadador: "))

if idade < 5:
        print("Idade inferior a 5 anos não se enquadra em nenhuma das categorias")
elif idade <= 7:
	print("Categoria: infantil.")
elif idade <= 10:
	print("Categoria: juvenil.")
elif idade <= 15:
	print("Categoria: adolescente.")
elif idade <= 30:
	print("Categoria: adulto.")
else:
        print("Categoria: sênior.")


