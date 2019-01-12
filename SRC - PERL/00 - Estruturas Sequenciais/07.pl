#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faca um programa que receba o valor de um deposito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento

print "Digite o valor do despósito > ";
my $desposito = <>;
chomp $desposito;

print "Digite o valor da taxa de juros > ";
my $taxa_juros = <>;
chomp $taxa_juros;

my $rendimento = $desposito * $taxa_juros / 100;
my $valor_total = $desposito + $rendimento;

printf "O valor total é R\$ %.2f ", $valor_total;
say "";
