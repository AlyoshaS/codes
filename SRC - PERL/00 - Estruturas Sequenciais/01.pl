#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);


# Faça um programa que receba três notas, calcule e mostre a média aritimética entre elas

print("Digita a 1 nota > ");
my $nota1 = <>;
chomp $nota1;

print("Digita a 2 nota > ");
my $nota2 = <>;
chomp $nota2;

print("Digita a 3 nota > ");
my $nota3 = <>;
chomp $nota3;

my $media = ($nota1 + $nota2 + $nota3) / 3.0;

say "A média das notas é ", $media;
