#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deverá calcular e mostar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado

print "Digite o custo do espetáculo > ";
my $custo_espetaculo = <>;
chomp $custo_espetaculo;

print "Digite o preço do convite > ";
my $preco_convite = <>;
chomp $preco_convite;

my $quantidade = $custo_espetaculo / $preco_convite;

printf "A quantidade que deve ser vendida é %d \n", $quantidade;
