#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

#Faça um programa que receba um número real, calcule e mostre:

#a parte inteira desse número;	   #a parte fracionária desse número;	  #o arredondamento desse número


print "Digite um número real > ";
my $numero = <>;
chomp $numero;

my $inteiro = int($numero);
my $fracao = $numero - $inteiro;
my $arredondado = abs($numero);

printf "A parte inteira é %d \n", $inteiro;
printf "A parte fracionária é %f \n", $fracao;
printf "O número arredondado é %d \n", $arredondado;
