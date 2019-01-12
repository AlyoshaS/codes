#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro

print "Digite um número maior que 0 > ";
my $numero1 = <>;
chomp $numero1;

print "Digite outro número maior que 0 > ";
my $numero2 = <>;
chomp $numero2;

my $pot1 = $numero1 ** $numero2;
my $pot2 = $numero2 ** $numero1;

printf "O número %d elevado a %d é %d \n", $numero1, $numero2, $pot1;
printf "O número %d elevado a %d é %d \n", $numero2, $numero1, $pot2;

