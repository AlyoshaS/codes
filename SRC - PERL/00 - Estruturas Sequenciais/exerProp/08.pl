#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * diagonal menor) / 2

say "+==============================+";
say "| Calcula a área de um losango |";
say "+==============================+\n";

print "Digite o valor da diagonal maior >> ";
my $diagonal_maior = <>;
chomp $diagonal_maior;

print "Digite o valor da diagonal menor >> ";
my $diagonal_menor = <>;
chomp $diagonal_menor;

my $area = ($diagonal_maior * $diagonal_menor) / 2;

printf "A área do losango é: %.2f \n", $area;
