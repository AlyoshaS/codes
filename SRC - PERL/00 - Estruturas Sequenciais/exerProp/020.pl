#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o número de lados de um polígono convexo, calcule e mostre o número de diagonais desse polígono. Sabe-se que ND = N * (N - 3) / 2, onde N é o número de lados do polígono.

print "Digite a quantidade de lados do polígono >> ";
my $lados_do_poligono = <>;
chomp $lados_do_poligono;

my $diagonais_do_poligno = $lados_do_poligono * ($lados_do_poligono - 3) / 2;

printf "O polígono possui %d diagonais \n", $diagonais_do_poligno;
