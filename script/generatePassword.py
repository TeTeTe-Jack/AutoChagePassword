#!/usr/bin/env python3

from random import randint

def checkPassword(str,chars,result):
	if result:
		return result
	else:
		return str in chars

# length of password
num=8

#list of charactors used for password
charsSma = "abcdefghijklmnopqrstuvwxyz"
charsCap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charsNum = "0123456789"
charsSym = "+/!$%&'()=~|@`[]{}*+<>?_;:,.\\"
chars=charsSma+charsCap+charsNum+charsSym

# exit condition of while loop 
result=True

while(result):
	
	# condition checking if each chars is contained 
	resultSma=False
	resultCap=False
	resultNum=False
	resultSym=False
	
	# initialization of password
	password=""	
	
	for i in range(0, num):
		length = len(chars)
		pos = randint(0,length-1)
		password=password + chars[pos]
		
		# check if each chars is contained
		resultSma=checkPassword(chars[pos],charsSma,resultSma)
		resultCap=checkPassword(chars[pos],charsCap,resultCap)
		resultNum=checkPassword(chars[pos],charsNum,resultNum)
		resultSym=checkPassword(chars[pos],charsSym,resultSym)
	
	# check exit condition
	if resultSma and resultCap and resultNum and resultSym:
		result=False

print (password)