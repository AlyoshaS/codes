#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Primeira alternativa:
Devolve o elemento dentro do array caso o encontre:
[5]  == True
[] == Vazio
"""

contains = lambda V, e: [True for x in V if x == e]

print(contains([1,2,3,4,5], 5))
print(contains([1,2,3,4,5], 6))

"""
Segunda alternativa:
Devolve o elemento dentro do array caso o encontre:
[5]  == True
[] == False
Observar a forma como o True e False foram utilizados.
"""
contains = lambda V, e: True if [ x for x in V if x == e ] else False

print(contains( [1,2,3,4,5], 5))
print(contains( [1,2,3,4,5], 6))
