#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

#Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que o usuário deseja alcançar subindo a escada, calcule e mostre quantos degraus ele deverá subir para atingir seu objetivo, sem se preocupar com a altura do usuário. Todas as medidas fornecidas devem estar em metros.

print "Digite a altura do degrau > ";
my $altura_degrau = <>;
chomp $altura_degrau;

print "Digite a altura que se deseja alcançar > ";
my $altura_usuario = <>;
chomp $altura_usuario;

my $quantidade_degraus = $altura_usuario / $altura_degrau;

printf "Você deverá subir %d degraus \n", $quantidade_degraus;

