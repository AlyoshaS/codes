#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

#O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:

#o valor correspondente ao lucro do distribuidor;
#o valor correspondente aos impostos;
#o preço final do veículo.

print "Digite o preço de fábrica > ";
my $preco_fabrica = <>;
chomp $preco_fabrica;

print "Digite o percentual de lucro do distribuidor > ";
my $percentual_distribuidor = <>;
chomp $percentual_distribuidor;

print "Digite o valor dos impostos > ";
my $impostos = <>;
chomp $impostos;

my $valor_distribuidor = $preco_fabrica * $percentual_distribuidor / 100;
my $valor_imposto = $preco_fabrica * $impostos / 100;
my $total = $preco_fabrica + $valor_distribuidor + $valor_imposto;

printf "O lucro do distribuidor é %.2f \n", $valor_distribuidor;
printf "O valor do imposto é %.2f \n", $valor_imposto;
printf "O valor total do carro é %.2f \n", $total;
