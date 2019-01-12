#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que calcule e mostre a área de um quadrado. Sabe-se que: A = lado * lado

say "+===============================+";
say "| Calcula a área de um quadrado |";
say "+===============================+\n";

print "Digite o valor de um lado do quadrado >> ";
my $lado = <>;
chomp($lado);

my $area = $lado ** 2;

printf "A área do quadrado é: %d \n", $area;


