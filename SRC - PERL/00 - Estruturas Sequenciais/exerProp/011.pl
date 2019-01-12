#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# a idade dessa pessoa em anos;
# a idade dessa pessoa em meses;
# a idade dessa pessoa em dias;
# a idade dessa pessoa em semanas.

print "Digite o ano de nascimento >> ";
my $ano_nascimento = <>;
chomp $ano_nascimento;

print "Digite o ano atual >> ";
my $ano_atual = <>;
chomp $ano_atual;

my $idade_em_anos = $ano_atual - $ano_nascimento;
my $idade_em_meses = $idade_em_anos * 12;
my $idade_em_dias = $idade_em_meses * 30;
my $idade_em_semanas = $idade_em_dias / 7;

printf "\nIdade em anos: %d \n", $idade_em_anos;
printf "Idade em meses: %d \n", $idade_em_meses;
printf "Idade em dias: %d \n", $idade_em_dias;
printf "Idade em semanas: %d \n", $idade_em_semanas;
