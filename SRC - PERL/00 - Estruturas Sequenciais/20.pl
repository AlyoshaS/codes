#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

#Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba o valor do salário mínimo e a quantidade de quilowatts consumida por uma residência, calcule e mostre:

#o valor de cada quilowatt; 	#o valor a ser pago por essa residência;	#o valor a ser pago com desconto de 15%

print "Digite o valor do salário mínimo > ";
my $salario_minimo = <>;
chomp $salario_minimo;

print "Digite a quantidade de quilowatts consumidas > ";
my $quantidade_kw = <>;
chomp $quantidade_kw;

my $valor_kw = $salario_minimo / 5;
my $valor_a_pagar = $valor_kw * $quantidade_kw;
my $desconto = $valor_a_pagar * 15 / 100;
my $valor_com_desconto = $valor_a_pagar - $desconto;

printf "O valor de cada quilowatt é %.2f \n", $valor_kw;
printf "O valor a ser pago pela residência é R\$ %.2f \n", $valor_a_pagar;
printf "O valor com desconto a ser pago é R\$ %.2f \n", $valor_com_desconto;

