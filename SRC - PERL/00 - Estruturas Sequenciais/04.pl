#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor de aumento e novo salário

print "Digite o valor do salário > ";
my $salario = <>;
chomp $salario;

print "Digite o percentual de aumento > ";
my $percentual = <>;
chomp $percentual;

my $aumento = $salario * $percentual / 100;

printf "O aumento foi de R\$ %.2f ", $aumento;
say "";

my $novo_salario = $salario + $aumento;

printf "O novo salário é R\$ %.2f ", $novo_salario;
say "";
