#print ("hellow from python")

#python code to print short bography;
"""
print ("i'm alaa elnagar")
print ("my birth day 10 april 1995")
print ("graduated from facualty of engineering HTI")
"""

#VARIABLES IN PYTHON
"""
PYTHON HAS NO COMMAND TO DECLARE A VARIABLE 
we can change variavble type by re defenition
"""

#ex
"""
x=5
y=6
print("x & y value equal ",x,y)
x="alaa"
print(x)
"""



#variables comma operator 
"""
x,y,z=5,6,7

print(x , y, z)
#swapping easy
x,y,z=7,5,6
print(x , y, z)

x=y=z=7
print(x , y, z)
"""
#casting formates

#input internal function  to recive int
"""

x=int (input("enter your first number"))

y=int (input("enter your second number"))


print("your sum result equal",x+y)



"""

#input internal function  to recive string



"""
v=input ("enter your name :")

print("welcome " +v)
x=int (input("enter your first number"))

y=int (input("enter your second number"))


print("your sum result equal",x+y)

"""

#input internal function  to recive a float


"""
a= float (input ("enter your float number"))

print("the floated number u have entered is " ,a)

"""

#  exampel to return your age from birth day
"""
c=int (input ("enter your birth day"))

print("you are ",2020-c,"years old")

"""



#if statement 
""" 
---------------construction
if condition:
<Spaces> Action_1
elif condition:
<Spaces> Action_2
else:
<Spaces> Action_3

"""

#making login system using f statement 

"""
User Name Password
Ahmed 1394
Ali 6078
Amr 9345

"""
"""
name=input("enter your user name:")

password=int(input("enter your user password:"))

if (name==ahmed and password==1394):
	print ("welcome "+name)



"""


my_fruit_tuple=("apple","banana","watermelon")

my_cost_tuple=(10,7,20)
consumer_number=[]
consumer_list=[]
consumer_cost=[]
selector=int(input("to creat order press 1: \nto print order press 2:\nto exit press 3:"))
y=1
z=1;
z=0
while(selector>0):
	while(y>0):
		consumer_number.append(z)
		selected_fruit=input("enter your fruit:")
		selected_fruit_quantity=input("enter your quantity:")
		my_cost_tuple_counter =0

		for i in my_fruit_tuple:
			if (i==selected_fruit) :
				consumer_list.append(i)
				consumer_cost.append( my_cost_tuple[my_cost_tuple_counter] *(int(selected_fruit_quantity)))
				my_cost_tuple_counter+=1
				break
		else :
			print(f"sorry your {selected_fruit} fruit dosent exist")
			z=z-1				
		z+=1			
		my_cost_tuple_counter=0
		y=int(input ("TO ADD ELEMENT--> press 1 \nTO EXIT --> press 0 \n"))
	
			#x=my_fruit_tuple.index("apple")
			
			#consumer_cost.append(my_cost_tuple(my_fruit_tuple.index(i))*selected_fruit_quantity)
	selector=int(input("to creat order press 1: \nto print order press 2:\nto exit press 3:"))

	if (selector==2):
		print ("_______THANK U_____")
		print ("_______You bought_____")
		print (consumer_list)
		print ("_______respectively cost_____")
		print (consumer_cost)
		total_cost=0
		for j in range (z):
			total_cost+=consumer_cost[j]
		print ("_______TOtal cost_____")
		print (f"total cost ={total_cost}")
		print ("__Let we see u again!__")
	total_cost=0
			
		

	
	







































