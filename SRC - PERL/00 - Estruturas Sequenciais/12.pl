#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Sabe-se que: 
#1 pé = 12 polegadas; 
#1 jarda = 3 pés; 
#1 milha = 1.760 jardas.

# Faça um programa que receba a medida em pés, # faça as conversões a seguir e mostre os resultados.
# polegadas	jardas	milhas

print "Digite uma medida em pés > ";
my $pes = <>;
chomp $pes;

my $polegadas = $pes * 12;
my $jardas = $pes / 3;
my $milhas = $jardas / 1760;

printf "Polegadas: %d; Jardas: %.2f; Milhas: %.2f \n", $polegadas, $jardas, $milhas;



