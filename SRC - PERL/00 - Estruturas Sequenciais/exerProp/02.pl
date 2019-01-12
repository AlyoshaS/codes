#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar com validações.

print "Digite o primeiro número >> ";
my $numero1 = <>;
chomp $numero1;

print "Digite o segundo número(não pode ser zero) >> ";
my $numero2 = <>;
chomp $numero2;


my $divisao = $numero1 / $numero2;

printf "%.2f / %.2f = %.2f \n", $numero1, $numero2, $divisao;
