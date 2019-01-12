#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba três núemros, calcule e mostre a multiplicação desses números.

print "Digite o primeiro número >> ";
my $numero1 = <>;
chomp $numero1;

print "Digite o segundo número >> ";
my $numero2 = <>;
chomp $numero2;

print "Digite o terceiro número >> ";
my $numero3 = <>;
chomp $numero3;

my $multiplicacao = $numero1 * $numero2 * $numero3;

printf "%d * %d * %d = %d \n", $numero1, $numero2, $numero3, $multiplicacao;
