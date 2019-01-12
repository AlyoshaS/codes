#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

#Faça um programa que receba o peso de uma pessoa, calcule e mostre:
#    o novo peso, se a pessoa engordar 15% sobre o peso digitado;
#    o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

print "Digite seu peso >> ";
my $peso = <>;
chomp $peso;

my $porcento_15_do_peso = $peso * 15 / 100;
my $porcento_20_do_peso = $peso * 20 / 100;

printf "15 por cento do seu peso a mais é: %.2f \n", ($peso + $porcento_15_do_peso);
printf "20 por cento do seu peso a menos é: %.2f \n", ($peso - $porcento_20_do_peso);
