#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba uma temperatura em Celcius, calcule e mostre essa temperatura em Fahrenheit. Sabe-se que F = 180 * (C + 32) / 100.

print "Digite uma temperatura em Celcius >> ";
my $celcius = <>;
chomp $celcius;

my $F = 180 * ($celcius + 32) / 100;

printf "F° %.2f \n", $F;
