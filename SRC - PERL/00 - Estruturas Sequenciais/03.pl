#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%

print "Digite o salário > ";
my $salario = <>;

my $novo_salario = $salario + ($salario * 25 / 100);

printf "O novo salário é R\$ %.2f", $novo_salario;
print "\n";


