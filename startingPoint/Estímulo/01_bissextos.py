"""
01 - Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. 
- Teste a validade desta data para saber se esta é uma data válida. 
- Teste se o dia fornecido é um dia válido: dia > 0, dia ≤ 28 para o mês de fevereiro (29 se o ano for bissexto) 
- dia ≤ 30 em abril, junho, setembro e novembro, 
- dia ≤ 31 nos outros meses. 
- Teste a validade do mês: mês > 0 e mês < 13. 
- Teste a validade do ano: ano ≤ ano atual (use uma constante definida com o valor igual a 2008). 
Imprimir: “data válida” ou “data inválida” no final da execução do programa. 
Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.
"""
dia, mes, ano = [int(x) for x in input("Digite dia, mês e ano de nascimento (** ** ****): ").split()]
ano_atual = 2008

if ano <= ano_atual:
	if mes > 0 and mes < 13:
		if mes == 2:
			if dia <= 28:
				dia = dia_valido
			elif dia == 29:
				verifica_ano = ano / 400
				if verifica_ano %400 > 0:
					ano = ano_valido
				else:
					ano = ano_invalido
		elif mes == 4 or mes == 6 or mes == 9 or mes == 11::
			if dia <= 30:
				dia = dia_valido
			else:
				dia = dia_invalido
		else:
			if dia <= 31:
				dia = dia_valido
			else:
				dia = dia_invalido
else:
	ano = ano_invalido



#teste ano:
if ano <= ano_atual:
	virifica_ano = ano / 400
	if verifica_ano %400 > 0:
		if mes == 2:
			


	if dia == 29:
		if mes == 02:
			dia = dia_valido
		else:
			dia = None


# Define e mostra o tipo do ano:
if data == data_valida:
	print("Data válida!")
else:
	print("Data inválida!")