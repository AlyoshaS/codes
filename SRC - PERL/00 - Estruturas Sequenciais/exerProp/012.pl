#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# João recebeu seu salário e precisa pagar duas contas atrasadas. Por causa do atraso, ele deverá pagar multa de 2% sobre cada conta. Faça um programa que calcule o mostre quanto restará do salário de João.

print "Digite o salário >> ";
my $salario = <>;
chomp $salario;

print "Digite o valor da primeira conta >> ";
my $valor_primeira_conta = <>;
chomp $valor_primeira_conta;

print "Digite o valor da segunda conta >> ";
my $valor_segunda_conta = <>;
chomp $valor_segunda_conta;

# Soma o juros com o valor das contas
my $total_primeira_conta = ($valor_primeira_conta * 2 / 100) + $valor_primeira_conta;
my $total_segunda_conta = ($valor_segunda_conta * 2 / 100) + $valor_segunda_conta;

my $saldo = $salario - ($total_primeira_conta + $total_segunda_conta);

printf "\nO saldo é R\$ %.2f \n", $saldo;
