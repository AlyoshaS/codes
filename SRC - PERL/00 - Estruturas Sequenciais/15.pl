#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

#Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e mostre o salário a receber seguindo estas regras:

#a hora trabalhada vale a metade do salário mínimo.
#o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
#o imposto equivale a 3% do salário bruto.
#o salário a receber equivale ao salário bruto menos o impostos

print "Digite as quantidade de horas trabalhadas > ";
my $horas_trabalhadas = <>;
chomp $horas_trabalhadas;

print "Digite o valor do salário mínimo > ";
my $salario_minimo = <>;
chomp $salario_minimo;

my $hora_trabalhada = $salario_minimo / 2;
my $salario_bruto = $horas_trabalhadas * $horas_trabalhadas;
my $imposto = $salario_bruto * 3 / 100;
my $salario_a_receber = $salario_bruto - $imposto;

printf "O salário a receber é R\$ %.2f \n", $salario_a_receber;

