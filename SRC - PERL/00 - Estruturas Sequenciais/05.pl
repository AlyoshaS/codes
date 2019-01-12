#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% sobre este salário'

print "Digite o salário base > ";
my $salario_base = <>;
chomp $salario_base;

my $gratificacao = $salario_base * 5 / 100;
my $imposto = $salario_base * 7 / 100;

my $novo_salario = $salario_base + $gratificacao - $imposto;

printf "O novo salário é R\$ %.2f", $novo_salario;
say "";
