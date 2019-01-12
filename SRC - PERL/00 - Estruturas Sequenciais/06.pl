#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o salário base de um funcionário, calcule e mostre o seu salário a receber, sabendo-se que o funcionário tem gratificação de R$50 e paga imposto de 10% sobre o salário base

print "Digite o salário base > ";
my $salario_base = <>;
chomp $salario_base;

my $imposto = $salario_base * 10 / 100;

my $novo_salario = $salario_base + 50 - $imposto;

printf "O novo salário é R\$ %.2f", $novo_salario;
say "";
