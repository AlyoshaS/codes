#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de horas extras trabalhadas, calcule e mostre o salário a receber, seguindo as regras abaixo:
    # a hora trabalhada vale 1/8 do salário mínimo;
    # a hora extra vale 1/4 do salário mímino;
    # o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
    # a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra;
    # o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras
    
print "Digite a quantidade de horas trabalhadas(apenas horas) >> ";
my $horas_trabalhadas = <>;
chomp $horas_trabalhadas;

print "Digite o valor do salário mínimo >> ";
my $salario_minimo = <>;
chomp $salario_minimo;

print "Digite as horas extras trabalhadas >> ";
my $horas_extras = <>;
chomp $horas_extras;

my $valor_hora_trabalhada = $salario_minimo / 8;
my $valor_hora_extra = $salario_minimo / 4;
my $salario_bruto = $horas_trabalhadas * $valor_hora_trabalhada;
my $quantia_hora_extra = $horas_extras * $valor_hora_extra;
my $salario_a_receber = $salario_bruto + $quantia_hora_extra;

printf "O salário a receber é R\$ %.2f \n", $salario_a_receber;


