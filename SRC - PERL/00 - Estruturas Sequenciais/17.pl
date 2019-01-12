#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.

print "Digite o peso do saco de ração em quilos > ";
my $peso_do_saco = <>;
chomp $peso_do_saco;

print "Digite a quantidade de ração do primeiro gato > ";
my $racao_primeiro_gato = <>;
chomp $racao_primeiro_gato;

print "Digite a quantidade de ração do segundo gato > ";
my $racao_segundo_gato = <>;
chomp $racao_segundo_gato;

$racao_primeiro_gato = $racao_primeiro_gato / 1000;
$racao_segundo_gato = $racao_segundo_gato / 1000;

my $total_final = $peso_do_saco - 5 * ($racao_primeiro_gato + $racao_segundo_gato);

printf "O restante da ração daqui 5 dias será %.2f \n", $total_final;
