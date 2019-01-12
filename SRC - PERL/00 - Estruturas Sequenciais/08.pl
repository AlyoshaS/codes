#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que calcule e mostre a área de um triangulo. Sabe-se que: Área = (base * altura) / 2

print "Digite a base > ";
my $base = <>;
chomp $base;

print "Digite a altura > ";
my $altura = <>;
chomp $altura;

my $area = ($base * $altura) / 2;

printf "A área do truângulo é %.2f ", $area;
say "";
