def funcInmodule(a,b):

	print("u have enterd "+a)
	print("u have enterd "+b)


def Set_bit(number,bit_num) :
	print("hellow from other function ")
	x=1<<bit_num

	number=number|x
	return number
	
def Clr_bit (number,bit_num) :

	x=~(1<<bit_num)

	number=number&x
	return number

def Tog_bit (number,bit_num) :

	x=(1<<bit_num)

	number=number^x
	return number

def get_bit (number,bit_num) :

	x=(1<<bit_num)

	number=number&x
	return number





	
































	
