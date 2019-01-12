#!/usr/bin/python3
# encoding: utf-8
# encoding: iso-8859-1 
# encoding: win-1252
# 

from random import randint


num = randint(0,30);

palp = 0


while(palp != num):

	palp = int(input("Digite o seu palpite: "))

	
	if (palp > num):
		print("Você errou... O numero é menor que", palp, "!")
		print(" ")
		
	elif (palp < num): 
		print("Você errou... O numero é maior que", palp, "!")
		print(" ")

	else:
		print("Parabéns! Você acertou!!")
		print(" ")