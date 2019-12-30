import random as rm
while 1:
	a=rm.randint(0,999999)
	
	b=int(input("please guess the number\n"))
	if(b==a):
		print("congratlation!! you won")
		
	if(b>a):
		print("you guessed a larger number")
	if(b<a):
		print("you guessed a smaller number")
	if(b==0 or b<0):
		break
