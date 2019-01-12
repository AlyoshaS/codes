#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o raio, calcule e mostre:

# o comprimento de uma esfera; sabe-se que C = 2 PI R;
# a área de uma esfera; sabe-se que A = PI * R²;
# o volume de uma esfera; sabe-se que V = 3/4 PI R³.

print "Digite um raio para obter alguns calculos sofre a esfera >> ";
my $raio = <>;
chomp $raio;

my $PI = 3.1415;

my $comprimento_esfera = 2 * $PI * $raio;
my $area_esfera = $PI * $raio ** 2;
my $volume_esfera = (3 / 4 * $PI * $raio ** 3);

printf "O comprimento da esfera é: %.2f \n", $comprimento_esfera;
printf "A área da esfera é: %.2f \n", $area_esfera;
printf "O volume da esfera é: %.2f \n", $volume_esfera;
