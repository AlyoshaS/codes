#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

print "Digite o preço do produto >> R\$ ";
my $preco_produto = <>;
chomp $preco_produto;

my $desconto = ($preco_produto * 10) / 100;
my $preco_produto_com_desconto = $preco_produto - $desconto;

printf "O preço do produto com desconto é: R\$ %.2f \n", $preco_produto_com_desconto;
