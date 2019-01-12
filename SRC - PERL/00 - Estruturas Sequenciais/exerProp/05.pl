#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.

print "Digite seu peso em quilos >> ";
my $peso_quilos = <>;
chomp $peso_quilos;

my $peso_gramas = $peso_quilos * (10 ** 3);

printf "O seu peso em gramas é: %.2f \n", $peso_gramas;
