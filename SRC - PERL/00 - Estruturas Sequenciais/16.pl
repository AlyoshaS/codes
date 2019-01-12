#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

#Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% e o saldo inicial da conta está zerado.

print "Digite o valor do salário > ";
my $valor_salario = <>;
chomp $valor_salario;

print "Digite o valor do primeiro cheque > ";
my $cheque_1 = <>;
chomp $cheque_1;

print "Digite o valor do segundo cheque > ";
my $cheque_2 = <>;
chomp $cheque_2;

my $cpmf_1 = $cheque_1 * 0.38 / 100;
my $cpmf_2 = $cheque_2 * 0.38 / 100;

my $saldo = $valor_salario - $cheque_1 - $cheque_2 - $cpmf_1 - $cpmf_2;

printf "Seu saldo atual é R\$ %.2f \n", $saldo;
