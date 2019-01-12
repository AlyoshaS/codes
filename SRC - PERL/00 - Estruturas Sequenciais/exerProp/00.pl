#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba dois números, calcule e mostre a subtração do primeiro número pelo segundo.

print "Digite o primeiro número >> ";
my $numero1 = <>;
chomp $numero1;

print "Digite o segundo número >> ";
my $numero2 = <>;
chomp $numero2;

my $subtracao = $numero1 - $numero2;

printf "%d - %d = %d \n" , $numero1, $numero2, $subtracao;
