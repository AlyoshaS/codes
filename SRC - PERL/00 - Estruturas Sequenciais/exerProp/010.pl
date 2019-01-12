#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

# Faça um programa que calcule e mostre a tabuada de um número digitado pelo usuário.

print "Digite um número e veja sua tabuada >> ";
my $numero = <>;
chomp $numero;

my $m1 = $numero ** 1;
my $m2 = $numero ** 2;
my $m3 = $numero ** 3;
my $m4 = $numero ** 4;
my $m5 = $numero ** 5;
my $m6 = $numero ** 6;
my $m7 = $numero ** 7;
my $m8 = $numero ** 8;
my $m9 = $numero ** 9;
my $m10 = $numero ** 10;

printf " $numero ** 1 = $m1\n $numero ** 2 = $m2\n $numero ** 3 = $m3\n $numero ** 4 = $m4\n $numero ** 5 = $m5\n $numero ** 6 = $m6\n $numero ** 7 = $m7\n $numero ** 8 = $m8\n $numero ** 9 = $m9\n $numero ** 10 = $m10\n", $m1, $m2, $m3, $m4, $m5, $m6, $m7, $m8, $m9, $m10;

