


"""

def Gcc (num1 ,num2) :
	x;
	if (num1>num2) :
		x=num1

"""

 
n=int(input("plz Enter your number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    print(dig)
    rev=rev*10+dig
    print(rev)    
    n=n//10
    print(n)  
if(temp==rev):
    print("The number is a palindrome")
else:
    print("The number isn't a palindrome")



def evenorodd(c):
	z=c
	while (z<(3*c)) :
		if (z%2==0):
			print("even number ")
			z=z-1
		else :  
			print("odd number ")
			z=z-1
		
	else:
		printf("number overr than 3n")


c= int (input("enter a number to chek even or odd"))




evenorodd(c)































