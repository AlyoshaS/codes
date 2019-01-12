#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e seu salário final

print "Digite o valor do salário do funcionário >> ";
my $salario = <>;
chomp $salario;

print "Digite o valor de suas vendas >> ";
my $valor_vendas = <>;
chomp $valor_vendas;

my $comissao = ($valor_vendas * 4) / 100;
my $salario_final = $salario + $comissao;

printf "O funcionário tem R\$ %.2f de comissão e o seu salário final será de R\$ %.2f \n", $comissao, $salario_final;
