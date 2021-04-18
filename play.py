
from module import *
"""
print("hello world ")


print("here we are ")



x = input("ENTER YOUR NAME ")

print ("wlcome " +x)


if x=="alaa" :
	print("ACCESS ")



for z in x :

	print(z)


Resolution  = input("Please enter the timer resolution: ")
Frequency   = input("Please enter the system frequency in MHz: ")
Prescaller  = input("Please enter the Prescaller value: ")

Resolution  = int(Resolution)
Frequency   = int(Frequency )
Prescaller  = int(Prescaller)

Overflow = ((2**Resolution) * Prescaller) / (Frequency * (10**3))

Message = "The timer would overflow after " + str(Overflow) + " milliseconds"
print(Message)

Sentence  = input("Please enter a sentence: ")
mirror = ""
for x in Sentence:
	mirror = x+ mirror 
	print("The sentence after mirrorring is " + mirror)	
print("The sentence after mirrorring is " + mirror)

"""

"""

height = input("Please enter pyramid Hieght: ")
height = int(height)

row = 0
while row < height:
	NumOfSpace  = height - row - 1
	NumOfStars  = ((row + 1) * 2) - 1
	string = ""
	#Step 1: Get the spaces
	i = 0
	while i < NumOfSpace:
		string = string + " "
		i += 1
	
	#step 2: Get the stars
	i = 0
	while i < NumOfStars:
		string = string + "*"
		i +=1
		
	print(string)
	row += 1


"""

"""
string = "luka elnagar"

print(string[0:6])

print(string[7])

print(string[-1:-2])

print(string.upper())
print(string.lower())
print(len(string))


def print_myname ():
	x=("my name is alaa elnagar")
	print(x.lower())
	print(x.upper())
	print(len(x))
	print(x[1:20])



print_myname ();



def func_arg (x,y) :
	print(x+y)
	global b
	b=33






module.funcInmodule("alaa","yousef")
from module import funcInmodule





from module import Set_bit  
from module import Clr_bit 
from module import Tog_bit 
from module import get_bit 

number=int (input ("Enter your  number "))
number=int (input ("Enter your  bit number  "))
bit_num=2


x=Set_bit(number,bit_num) 

print(x)

x=Clr_bit (number,bit_num) 

print(x)

x=Tog_bit (number,bit_num)

print(x)

x=get_bit (number,bit_num)

print(x)



""" 



"""
Set_bit(4,2)

x=str(input ("enter yor elements to capatilize the first name "))
print(x.capitalize())

print(x.upper())

print(x.lower())

print(x.casefold())

print(x.center(20))

print(x.count('a'))

print(x.endswith('a'))

y=input ("a\ta\tl\ta\ta\t")

print(y.expandtabs(5))    # must be user defined


print(x.find('l'))

z="it {cost:.3f} as u {know} "

print(z.format(cost=20,know="see"))


c={ 'h':'alaa' , 'y':'elnagar'}



print("here is mr {h} {y}".format_map(c))



print(x.index('l'))


print(x.index('a',1,3))


txt = "Hello, welcome to my world."

print(txt.find("q"))


"""


x=str(input ("enter yor elements to capatilize the first name "))



print(x.isalnum())

x=(input ("enter yor elements to capatilize the first name "))

print(x.isalpha())











































































