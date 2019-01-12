#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o valor so salário mínimo e o valor do salário de um funcionário, calcule e mostre a quantidade de salários mínimos que esse funcionário ganha.

print "Digite o valor do salário mínimo >> ";
my $salario_minimo = <>;
chomp $salario_minimo;

print "Digite o valor do salário do funcionário >> ";
my $salario_funcionario = <>;
chomp $salario_funcionario;

my $total_salarios = $salario_funcionario / $salario_minimo;

printf "O funcionário ganha %d salário(s) mínimo(s) \n", $total_salarios;
