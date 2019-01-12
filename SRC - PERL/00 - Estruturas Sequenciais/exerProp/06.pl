#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = ((base maior + base menor) * altura) / 2

say "---------------------------------";
say "| Calcula a área de um trapézio |";
say "---------------------------------\n";

print "Digite o valor da base maior >> ";
my $base_maior = <>;
chomp $base_maior;

print "Digite o valor da base menor >> ";
my $base_menor = <>;
chomp $base_menor;

print "Digite a altura >> ";
my $altura = <>;
chomp $altura;

my $area = (($base_maior + $base_menor) * $altura) / 2;

printf "A área do trapézio é: %.2f\n", $area;
