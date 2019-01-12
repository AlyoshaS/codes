#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas

print("Digite a nota 1 > ");
my $nota1 = <>;

print("Digite o peso da nota 1 > ");
my $peso1 = <>;

print("Digite a nota 2 > ");
my $nota2 = <>;

print("Digite o peso da nota 2 > ");
my $peso2 = <>;

print("Digite a nota 3 > ");
my $nota3 = <>;

print("Digite o peso da nota 3 > ");
my $peso3 = <>;

my $soma1 = $nota1 * $peso1;
my $soma2 = $nota2 * $peso2;
my $soma3 = $nota3 * $peso3;

my $total = $peso1 + $peso2 + $peso3;

my $media = ($soma1 + $soma2 + $soma3) / $total;

say "A média ponderada das notas é ", $media;
