

my_list=["alaa",1.2,True,1,["ITI STUDENT" ,"HTI GRAD"]]
"""
print(my_list[4])
print(my_list[0][0])
print(my_list[4][0])

print(my_list[-1])

print(my_list[1:3])
print(my_list[0:4:2]) #slicing

my_list[0]="yousef" 

print(my_list)

my_list[1:2]=[5,6]   

print(my_list)

my_list[1]=[5,6]   

print(my_list)




#my_list[4][0]=[5,6]   

#print(my_list)




my_list.append("alaa")     #add new list element to the list

print(my_list)

my_list.insert(0,"alaa")     #add new list element to the list

print(my_list)


my_list1=[9,10,11,12]


my_list.extend(my_list1)      #to extend list with new element
print(my_list)

my_list.append(my_list1)      #to extend list with new lis


print(my_list)
my_list=["alaa",1.2,True,1,["ITI STUDENT" ,"HTI GRAD"]]

my_list=my_list+my_list1    #concatinanating two list 

print(my_list)


print(my_list*3)






"""
"""
i=1
for x in my_list:
	my_list.insert(i,x)    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print( my_list)

"""





# delete list  
"""
my_list=["alaa",1.2,True,1,["ITI STUDENT" ,"HTI GRAD"]]

del my_list[0]

print (my_list)

del my_list[0:2]

print (my_list)

del my_list

print (my_list)
"""


#remove   listname.remove(item)    remove by item not index

"""
my_list=["alaa",1.2,True,1,["ITI STUDENT" ,"HTI GRAD"]]

my_list.remove("alaa")

print (my_list)

"""



#remove   listname.pop(index)    remove by index not item  and return the elemetnt that deleted 

"""
my_list=["alaa",1.2,True,1,["ITI STUDENT" ,"HTI GRAD"]]

x=my_list.pop(3)

print (my_list)    

print (x)

"""
"""
#remove   listname.clear()    clear all list but it still exist

my_list=["alaa",1.2,True,1,["ITI STUDENT" ,"HTI GRAD"]]

x=my_list.clear()

print (my_list)

my_list.append("haleeeoia")

print (my_list)

"""

#list copy
"""
my_list3=my_list


print(my_list3)

"""
#list copy
"""
my_list3=my_list.copy()


print(my_list3)
"""


#free list creation 

"""


new_list=list()

print(new_list)

new_list.append("hellow ")


print(new_list)

"""
#list initialization

"""
new_list=list(["HELLOW",1,1,1,2,32,33,431,4531,5]) 


print(new_list)

"""




#lab1

name=input("Enter your name ");
name=name.lower()
employ_name=list(["ahmed","ali","amr"])
employ_sallary=list([2000,3000,400])

x=0;
y=len(employ_name)
for i in employ_name :
	if (i==name):
		print ("wlecome "+i)
		print ("your sallary is ",employ_sallary[x])
		break
	else :
		x=x+1
		

if (x==y):
	print("incorrect user name ")
else :
	pass



































    




















