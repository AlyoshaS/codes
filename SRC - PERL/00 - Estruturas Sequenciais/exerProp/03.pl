#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira e peso 3 para a segunda.

print "Digite o valor da primeira nota >> ";
my $nota1 = <>;
chomp $nota1;

print "Digite o valor da segunda nota >> ";
my $nota2 = <>;
chomp $nota2;

my ($peso_nota1, $peso_nota2) = qw< 2 3 >;

my $soma1 = $nota1 * $peso_nota1;
my $soma2 = $nota2 * $peso_nota2;

my $total = $peso_nota1 + $peso_nota2;
my $media = ($soma1 + $soma2) / $total;

printf "A média ponderada das notas %.2f & %.2f é %.2f \n", $nota1, $nota2, $media;


