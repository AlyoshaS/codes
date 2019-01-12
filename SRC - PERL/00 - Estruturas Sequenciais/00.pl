#!/usr/bin/env perl
use v5.10;

use strict;
use warnings;

use utf8;
use open qw(:std :utf8);

print "Digite o primeiro número -> ";
my $n1 = <>;

print "Digite o segundo número -> ";
my $n2 = <>;

print "Digite o terceiro número -> ";
my $n3 = <>;

print "Digite o quarto número -> ";
my $n4 = <>;

my $soma = $n1 + $n2 + $n3 + $n4;

say "A soma dos números é ", $soma;
