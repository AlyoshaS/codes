#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = PI * R²

print "Digite o raio para encontrar a área do círculo > ";
my $raio = <>;
chomp $raio;

my $PI = 3.1416;

my $area = $PI * ($raio * $raio);

printf "A área do círculo é %.2f ", $area;
say "";
