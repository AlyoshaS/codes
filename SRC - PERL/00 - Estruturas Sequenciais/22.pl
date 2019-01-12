#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba uma hora formada por hora e minutos(um número real), calcule e mostre a hora digitada apenas em minutos. Lembre-se de que:

# para quatro e meia, deve-se digitar 4.30;
# os minutos vão de 0 a 59

print "Digite a hora no formato H.mm > ";
my $horario = <>;
chomp $horario;

my $hora = int($horario);
my $minuto = $horario - $hora;
my $conversao = ($hora * 60) + ($minuto * 100);

printf "A hora convertida em minutos é %d \n", $conversao;

