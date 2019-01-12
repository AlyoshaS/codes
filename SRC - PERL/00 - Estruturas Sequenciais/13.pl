#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

#Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:

#a idade da pessoa
#quantos anos ela terá em 2050

print "Digite o ano em que você nasceu > ";
my $ano_nascimento = <>;
chomp $ano_nascimento;

print "Digite o ano atual > ";
my $ano_atual = <>;
chomp $ano_atual;

my $idade_pessoa = $ano_atual - $ano_nascimento;
my $idade_em_2050 = 2050 - $ano_nascimento;

printf "Sua idade é %d \n", $idade_pessoa;
printf "Em 2050 você terá %d \n", $idade_em_2050;
