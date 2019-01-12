#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m² deve-se usar 18 W de potência. Faça um programa que receba as duas dimensões de um cômodo(em metros), calcule e mostre a sua área(em m²) e a potência de iluminação que deverá ser utilizada.

print "Digite o primeiro lado >> ";
my $lado1 = <>;
chomp $lado1;

print "Digite o segundo lado >> ";
my $lado2 = <>;
chomp $lado2;

my $area = $lado1 * $lado2;
my $potencia = $area * 18;

printf "A área é %d e a potencia deve ser %d W\n", $area, $potencia;
