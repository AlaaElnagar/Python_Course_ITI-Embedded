# touple like list but it is constant we cant change its value 

"""
Syntax

tublename=(member1,member2)
"""

"""

my_tuple=("alaa",1,2,3)

print (my_tuple)
print (my_tuple[0:3:2])
"""
#dosent suppert any adding functions
"""
my_tuple.insert("hi")
print (my_tuple)

for delete you can only delete the whole tuple 

"""
"""

print (my_tuple)
print (del my_tuple)

"""
"""
#tuple.index()
print (my_tuple.index("alaa"))


#tuple.count
print (my_tuple.count(10))

"""
# you can insert a list in tuple and then u can modify the lis 
"""
my_tuple=("alaa",1,2,3,['a','b','c'])


print (my_tuple)
my_tuple[4][0]=7
print (my_tuple)

"""


order_tuple=list(["apple",10,"banana",7,"watermelon",5])
customer_list=list([])

x=int(input ("to creat your order--> press 1 \nto print your order--> press 2 \nto exit from the system--> press 3 \n"))


if x==1:
	y=int(input ("TO ADD ELEMENT--> press 1 \nTO EXIT --> press 0 \n"))
	while (y==1):
		z=(input ("please enter the fruit"))
		y=int(input ("please enter the quantity"))
		for i in order_tuple:
			if i==z :
				customer_list.append(z)
				h=order_tuple.index(z)+1
				customer_list.append(y*order_tuple.select(h))
		y=int(input ("TO ADD ELEMENT--> press 1 \nTO EXIT --> press 0 \n"))
		
		


				
				
print(customer_list)
				
				
	

	
	

	







