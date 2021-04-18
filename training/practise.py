#https://www.w3resource.com/python-exercises/

import sys
import datetime
"""
print ("here is your sys "+ str(sys.version))

print ("here is your sys "+ str(sys.version_info))
now =datetime.datetime.now()

print(now)
"""

# Write a Python program which accepts the radius of a circle from the user and compute the area
"""
fixed_inf_tup=(3.14,5,6)


def circuit_data(radious):
	area=(fixed_inf_tup[0]*(radious**2))
	circumstance=2*fixed_inf_tup[0]*radious
	return(area,circumstance)

r=int(input ("enter the circule radious"))

area,circum=circuit_data(r)

print(f'the area of your circle is {area}\nand the circumstancs is {circum}')
"""




"""
# Python3 code to demonstrate working of 
# Convert tuple to float 
# using join() + float() + str() + generator expression 
  
# initialize tuple 
test_tup = (4, 56,1,2,3,4,5) 
  
# printing original tuple  
print("The original tuple : " + str(test_tup)) 
  
# Convert tuple to float 
# using join() + float() + str() + generator expression 
res = float('&&&&'.join(str(ele) for ele in test_tup)) 
  
# printing result 
print("The float after conversion from tuple is : " + str(res)) 

"""
"""
new_tup=(1,2,3,4,5,6)


x=str("@%&*".join(str (elements) for elements in new_tup))

print(x)

"""

#5. Write a Python program which accepts the user's first and 
#last name and print them in reverse order with a space between them

""""

x= str(input ("please enter your first name "))

x=x.lower()

x=x.strip()

y= str(input ("please enter your first name "))

l1=len(x)
l2=len(y)

for i in x :
	print(x[l1-1], end='	',flush=True)

	l1=l1-1

for i in y :
	print(y[l2-1], end='	',flush=True)

	l2=l2-1

print("")

"""


#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the #editor
#Sample data : 3, 5, 7, 23
#Output :
#List : ['3', ' 5', ' 7', ' 23']
#Tuple : ('3', ' 5', ' 7', ' 23')
"""
recive=str(input ("please enter your number followed by ,"))

print(recive)
my_list=list()
my_tup=tuple()
total=''
for i in recive:
	if i==',':
		my_list.append(total)
		my_tup=my_tup+(total,)	
		total=''
	else:
		total=str(total)+str(i)


	
print(my_list)	
print(my_tup)	

"""
#7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
#Sample filename : abc.java
#Output : java
"""
file_reciver=input ("enter your filename")
extension=''
flag=0
for i in file_reciver:

	if flag==1:
		extension=extension+i
	if (i=='.'):
		flag=1

print(f' your file extension is {extension}')
		
"""

#8. Write a Python program to display the first and last colors from the following list.
#color_list = ["Red","Green","White" ,"Black"]
#Click me to see the sample solution
"""
color_list = ["Red","Green","White" ,"Black"]
first_colour=color_list[0]
last_colour=0
for i in color_list:
	last_colour=last_colour+1


print(f'your first colour is {color_list[0]}\nyour last colour is {color_list[last_colour-1]}')
	
"""

#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014
"""
exam_st_date = (11, 12, 2014)

res=int(input ("if you want to get exam date press 1"))
if res==1:
	print(f"your exam will be {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")
"""
#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
#Sample value of n is 5
#Expected Result : 615

"""
x=input ("please enter the number")
count=int(input("enter number of itrations "))
c=''       # i have trouple with it >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>how to intialize char value give error
total=0
for i in range(count):
	for y in range(i):
		c=str(x)+str(c)
		print (c)
	total=int(c)+total
	
	

print (total)

"""


#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
#Sample function : abs()
#Expected Result :
#abs(number) -> number
#Return the absolute value of the argument.


#print(abs.__doc__)

#12. Write a Python program to print the calendar of a given month and year.
#Note : Use 'calendar' module.


"""
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
"""

"""
my_list=list()
my_dict=dict()

count=int(input ("enter nuber of loops"))
while (count>0):

	list_fed=int (input ("enter the list elements"))
	key=input ("dict the list key")
	my_dict[key]=list_fed
	my_list.append(list_fed)
	count=count-1

print(my_list)
print(my_dict)

total=0
for i in my_list:
	total+=i
dict_total=0
for i in my_dict:
	dict_total+=my_dict[i]

print(f'the sumtion of your list is {total}')

print(f'the sumtion of your dict is {dict_total}')

"""



#dict_concatinating

#Sample Dictionary :
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

my_dict=dict()

my_dict=dic1.copy()

my_dict.update(dic2)
my_dict.update(dic3)
print (my_dict)

for i in dic1:
	my_dict[i]=dic1[i]

for i in dic2:
	my_dict[i]=dic2[i]

for i in dic3:
	my_dict[i]=dic3[i]

print(my_dict)

"""

#13. Write a Python program to map two lists into a dictionary


list1=['a','b','c']
list2=['d','e','f']
my_dict=dict()
my_dict2=dict()

my_dict['list1']=list1

my_dict['list2']=list2

print (my_dict)

for i in range (2):
	my_dict2[i]=list1[i]

print(my_dict2)

	















































































	























































