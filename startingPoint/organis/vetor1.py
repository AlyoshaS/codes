#!/usr/bin/python3
# -*- coding: utf-8 -*-

# porra de codíng do caralho

"""
def getElementsVector( message ):
  user_input = input(message)
  input_list = user_input.split(',')
  numbers = [ int(x.strip()) for x in input_list ]
  return numbers

myVect = getElementsVector("Entre com numeros separados por virgula")

print(myVect)
"""

basket = [
  { 'type': 'food', 'product': 'oranges', 'price': 3, 'amount': 2 },
  { 'type': 'food', 'product': 'bleach', 'price': 5, 'amount': 5 },
  { 'type': 'home', 'product': 'pears', 'price': 6, 'amount': 2 }
]

def total(type, result=0):
  for c in basket:
    if(c['type'] == type):
      result += c['price'] * c['amount']
  return result

print(total('food'))
