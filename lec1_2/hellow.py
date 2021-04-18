"""
print ("my name is 3LAA ")
print ("my birth day is 10 -4 -1995 ")
print ("facualty of engineering  ")
print ("HTI")

a=b=c=10
a,b,c=1,2,3

print(a)
print(b)
print(c)
clear

"""
"""
# input function always return string 

x=input ("please enter the number ")
x=int (input ())
x=float (x)
x+=5
x="the value of x ="+str( x)
print ("the number u have enterd is :",x)



"""

            # operations 

#x,y=5,2

#z=x**y 

#print (z)

# it is calld flower division 

"""
z=x//y

print (z)



x=int ( input ("plz enter your birth year"))

x=2020-x
print("your age is ",x)

"""
"""
x=int (input ("enter the loan value  :"))
y=int (input("enter the num of years :"))

z=(x+(x*.12*5))/(y*12)

print ("the monthly payment is :",z)


"""


        # bool type x

"""
x=5;
y=6;

z=(x==y)
print (int (z))     #return False 
print (int (z))      # #return 0

print (bool (6))         # any number give bool true except zerro 
print (bool (-8))
print (bool (0))


"""
"""

# logical operators
x,y=3,5
z=not(x<y and x>0)
print(z)
z=not(x<y or x>0)
print(z)
 z=(x<y or x>0)
print(z)
"""
"""
#assigenments operator += *= //= **=

#bitwise operator  & | ^ ~ >> <<


x=3 & 1
print(x)

print (x>>2)



"""


# conditional statement  just contains if statement no switch
"""
x=0

if x==5 :
 print("true")
elif x==1 :
 print("false")
else :
 print ("x not meet your conditions ")

"""
"""
x= input ("ENTER YOUR NAME : ")
Y= input ("ENTER YOUR PASSWARD : ")
if Y=="1394" or Y=="6078" or Y=="9345" :

 if (x=="AHMED" and Y=="1394") or ( x=="Ali" and Y=="6078") or( x=="Amr" and Y=="9345") :
  print("welcome ",x)
 else :
  print("incorect user name ")
else :
 print("incorect user pass ")
"""


             # lab 1  20 09 2020
"""
num1=int( input ("ENTER YOUR num1 : "))
num2=int (input ("ENTER YOUR num2 : "))
z=num1+num2
a=num1-num2
print ('num1={0},num2={1}'.format(num1,num2))  #<<<<<<<<<<<<<<<<<<<outpout format
print (f"num1={num1},num2={num2}")
print("the sum =",z)
print("the sub= ",a)

"""
"""

num1=int( input ("ENTER YOUR num1 : "))
num2=int (input ("ENTER YOUR num2 : "))
print(" ")
z=num1//num2
print ('num1=%d,num2=%d'%(num1,num2))
z=round(float_num, num_of_decimals)

print("the flower division =",z)
print("   ")
print ('num1={0},num2={1}'.format(num1,num2))
print (f"result={z}")


"""
"""
num1=int( input ("ENTER YOUR pow : "))
num2=int (input ("ENTER YOUR base: "))
print("val =",num2**num1)
"""

# LAB 4  A CODE TO GET SQUARE AND CUBIC ROOT OF A NUMBER 
"""
num1=int( input ("ENTER YOUR NUM : "))

print("SQR ROOT =",num1**(1/2))

print("CUB ROOT =",num1**(1/3))

"""

"""
num1=int( input ("ENTER YOUR NUM1 : "))
num2=int( input ("ENTER YOUR NUM2 : "))
num3=int( input ("ENTER YOUR NUM3: "))

if num1>num2 :
 if num1>num3 :
  print (" THE LARGEST NUMBER is 1 ")
if num2>num1 :
 if num2>num3 :
  print (" THE LARGEST NUMBER is 2 ")
if num3>num2 :
 if num3>num1 :
  print (" THE LARGEST NUMBER is 3 ")

"""
  



"""


def swap(n1,n2):        


#swap case1 
 print("case1")
 n1, n2 = n2, n1
 print("n1 =", n1)
 print("n2 =", n2)

 #swap case2 
 print("case2")
 n1=n1+n2
 n2=n1-n2
 n1=n1-n2
 print("n1 =", n1)
 print("n2 =", n2)


 #swap case3
 print("case3") 
 n1=n1*n2
 n2=n1/n2
 n1=n1/n2
 print("n1 =", n1)
 print("n2 =", n2)


 #swap case4 
 print("case4")
 n1=int (n1)
 n2=int (n2)
 n1=n1^n2
 n2=n1^n2
 n1=n1^n2
 print("n1 =", n1)
 print("n2 =", n2)
 return(n1,n2)

x1=int( input ("ENTER YOUR NUM1 : "))
x2=int( input ("ENTER YOUR NUM2 : "))  
 
x1,x2=swap(x1,x2)

print("n1 finally  =", x1)
print("n2 finally =", x2)




"""










          # LEC2 20 09 2020       loops 
"""
I=0

while I<4:
 x= (input ("ENTER YOUR NAME : "))
 Y= int (input ("ENTER YOUR PASSWARD : "))
 if Y==1394 or Y==6078 or Y==9345 :
  if (x=="AHMED" and Y==1394) or ( x=="Ali" and Y==6078) or( x=="Amr" and Y==9345) :
   print("welcome ",x)
   I=4
  else :
   print("incorect user name ")
   I=4
 else :
  print("incorect user pass TRY AGAIN !! ")
 I+=1

"""

 #for loop 

"""

x=10

for i in range(x):
	print(i)




"""


"""
x=10

for i in range(3,10):
	print(i)

"""


num=input ("please enter your number ")
s=0
for i in num :
 s=int (i)+s
print (s)


"""

"""
#sequance type 

# string  x='string'   x="string "    

string ="123456789"
#        123456
#        -6-5>>>>>
print (string[4])
#slicing 
print (string[0:4])
print (string[-6:-1])

#upercase and lower case

x= input("enter any name")

print ("YOUR LOWER case NAME",x.lower())
print (string[0::2])
print ("YOUR LOWER case NAME",x.upper())

"""
"""
#formate 

nm=("yor name is {} and u r originally freom {}")
x= input ("enter your name ")
x=x.replace("a","A")
y= input ("enter your name ")

print (nm.format(x,y))

print (len(y))

"""
#Task1
#Search For All Built In String Function

#functions 


# func without arg
"""
def PrintMyname() :
	print("hellow my name is alaa")

def PrintMynameArg(NAME):
	print("WELCOME"+str(NAME))
	return("thank u ",3122)

x= input ("enter your name ")
PrintMynameArg(x)
x,y=PrintMynameArg(x)
print (x,y)
PrintMyname()

"""

#lab  
"""
def func (n1,n2):
	return n1+n2,n1*n2,n1/n2,n1-n2

n1=int (input("enter n1 :"))
n2=int (input("enter n2 :"))

sm,mul,div,sub=func(n1,n2)

print ("sum=",sm)
print ("mul",mul)
print ("div",div)
print ("sub",sub)


print ("sum="+str(sm))
print ("mul"+str(mul))
print ("div"+str(div))
print ("sub"+str(sub))

print ("sum={},mul={},div={},sub{}".format(str(sm)),mul,div,sub)


"""


































































