#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão e econstada na parede e a altura da parede onde está a ponta da escada, calcule e mostre a medida desta escada.

print "Digite o ângulo > ";
my $angulo = <>;
chomp $angulo;

print "Digite a altura da parede > ";
my $altura_parede = <>;
chomp $altura_parede;

my $PI = 3.1415;

my $radiano = $angulo * $PI / 180;
my $altura_escada = $altura_parede / sin($radiano);

printf "A escada mede %.2f m\n", $altura_escada;
