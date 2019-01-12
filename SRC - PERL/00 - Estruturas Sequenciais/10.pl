#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);


#	Faça um programa que receba um número positivo e maior que zero, calcule e mostre:

#	o número digitado ao quadrado;
#	o número digitado ao cubo;
#	a raiz quadrada do número digitado;
#	a raiz cúbica do número digitado;


print "Digite um número positivo maior que 0 > ";
my $numero = <>;
chomp $numero;

my $numero_ao_quadrado = $numero * $numero;
my $numero_ao_cubo = $numero_ao_quadrado * $numero;

my $raiz_quadrada_numero = $numero ** (1 / 2.0);
my $raiz_cubica_numero = $numero ** (1 / 3.0);

say "O número ", $numero, " ao quadrado é: ", $numero_ao_quadrado;
say "O número ", $numero, " ao cubo é: ", $numero_ao_cubo;
printf "A raiz quadrada do número %d é %.2f \n", $numero, $raiz_quadrada_numero;
printf "A raiz cubica do número %d é %.2f \n", $numero, $raiz_cubica_numero;
