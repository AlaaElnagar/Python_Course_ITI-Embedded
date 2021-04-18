
"""
set : it is an un order collection of itimes  i can't access it by index

-Every set is unique not duplicated 

we can add and removeitems 
my_set={10,10,2,3,4,5,6}
print(my_set)

-set dosent support list

set can be used to perform mathimatically set operation such as 
			ex:
				union              
				intersection
				symetric difference 
				

SYNTAX:
  set_name={items}

ex 
	my_set={1,2,3,4,5,6}
	print(my_set)


"""

"""		
my_set={10,10,2,3,4,5,6}
print(my_set)	

my_set={10,10,2,3,4,5,6,(1,2,3,4)}

print(my_set)	


"""

#free set creation
"""
my_set={}    #it will be dict not set so dont do this format for set

my_se1=()    #it will be createdas tuple


my_se1=set()    #it will be createdas set

#  type()   it return parameter type

 
print(type(my_set))

print(type(my_set1))
"""

#add&update >>  set_name.add(value)   to insert new valueo it recive only one element 

#add&update >>  set_name.aupdate(value)  value may be   can recive list 

"""
my_set={1,"alaa",2,4,5}

print(my_set)


my_set.add(10) 


print(my_set)

my_set.update((6,7,8,9,12))

print(my_set)

"""

#removing set element 
"""
SYNTAX
set_name.discard(value)   remove the selected element and if it dosent exisit return nothing

set_name.remove(value)	remove the selected element and if it dosent exisit return error

set_name.pop()     	dont take any argument and delete the laste element :note it differe from the another pop with list

set_name.(value)

"""

#EXAMPEL
"""
my_set={1,"alaa",2,4,5}
my_set2={3,"alaa",77,4,5}

print(my_set)
my_set.discard(5)
print(my_set)

my_set.pop()

print(my_set)


"""

#my_srt1.union(my_set2)   >>>add two set and get only one element of  the same elements 
"""
my_set={1,"alaa",2,4,5}
my_set2={3,"alaa",77,4,5}
print(my_set.union(my_set2))


"""
#myset.intersection(my_set2)   return the same elements 
"""
my_set1={1,"alaa",2,4,5}
my_set2={3,"alaa",77,4,5}

my_set1.intersection(my_set2)

print(my_set1.intersection(my_set2))

"""


#my_srt1.difference(my_set2)   >>>return the elements that dont exist in the myset 

"""
my_set={1,"alaa",2,4,5}
my_set2={3,"alaa",77,4,5}
print(my_set.difference(my_set2))  
"""
#my_set1.symmetric_difference(my_set2)   >>>return the elements that dont exist in the two sets
"""
my_set1={1,"alaa",2,4,5}
my_set2={3,"alaa",77,4,5}

my_set1.symmetric_difference(my_set2)

print(my_set1.symmetric_difference(my_set2))

"""




#_____________________________________________DICTIONARY IT IS VERY IMPORTANT TOPIC__________________________________________________

"""
dict it is un orderd collection of date 
advantages :
	each vlaue have its unique key 
	no duoblicated key 
	value can be doublicated


__________syntax_________________

dict_name={key1:value1,key2:value:2}


"""
#exampel
"""
my_Dict={1:'alaa',2:27,3:'cairo'}

print(my_Dict)

#dictionary access  my_Dict[key] 
#my_Dict[key]  give error incase of given invalid key
print(my_Dict[1])

print(my_Dict[2])

"""
#dictionary access  my_Dict.get(key)  return None
"""
my_Dict={1:'alaa',2:27,3:'cairo'}

print(my_Dict.get(3))

print(my_Dict.get('H'))

"""

#DIFFERDENCE BETWEEN LIST AND DICT 

""" 
KEY IS USED ICASE OF EXISTANCE OF UNIQUE ID WITH VALUE 
THE KEY UNIQUE CANT BE CHANGED 
THE KEY VALUE CAN BE CHANGED 
LIST IS USED INCASE OF EXISTANCE OF MULTIPLE VALUES WHICH ARE EQUAL OR DIFFERENCE 


"""

#ADDING KEY TwO DICT 
#NOTE if the given key is exised the value will be upploaded else the value will be generated

#ex







#removig elements 

#pop   dict_name.pop(key)  >>this case will returnthe value 


#popitem()  dict_name.popitem() dont recive argument and delete last key with its vaueo


#clear()   dict_name.clear()

#del       del dict.name()

#del       del my_dict[key]
#exampels
"""
my_Dict={1:'alaa',2:27,3:'cairo'}

x=my_Dict.pop(1)
	
print(my_Dict)
print(x)

"""

"""
my_Dict={1:'alaa',2:27,3:'cairo'}

x=my_Dict.popitem()

print(my_Dict)
print(x)

"""

"""
my_Dict={1:'alaa',2:27,3:'cairo'}

my_Dict.clear()

print(my_Dict)
"""
"""

my_Dict={1:'alaa',2:27,3:'cairo'}

del my_Dict

print(my_Dict)   


"""

#dictionary constructor to creat a free dict
"""
my_Dict=dict()  

print(my_Dict)   
"""

#my_Dict=dict({a='alaa',i='ITI'})  >>>>>>>>>>>>>

#print(my_Dict)                    >>>>>>>>>>>>>>>

"""
my_Dict={1:'alaa',2:27,3:'cairo'}

if 3 in my_Dict:
	print("hi from if statememnt")


if 27 in my_Dict.values():               #my_dict.values return the values o f dict
	print("hi from if statememnt2")


if 1  in my_Dict.keys():              
	print("hi from if statememnt3")

print (my_Dict.values())

print (my_Dict.keys())

"""
#dict with for loop
"""
my_Dict={1:'alaa',2:27,3:'cairo'}


for i in my_Dict:
	print(i)
	my_Dict[i]='ITI'
print(my_Dict)

for i in my_Dict.values():
	print(i)

"""
#dict id creation>>>>>>>>>>   my_Dict[ID]='value'
"""
my_Dict={1:'alaa',2:27,3:'cairo'}

ID=input("enter any value to insert inside the dictionary")

my_Dict[ID]="NEW VALUE"

#print(my_Dict)
print(my_Dict[ID])


"""

""""
my_Dict={1:'alaa',2:27,3:'cairo'}

for i in my_Dict:
	print(i)
	my_Dict[i]='ITI'
print(my_Dict)

for i in my_Dict.values():
	print(i)
"""


#nested dictionaries
"""
my_Dict={1:'python',2:'course',3:{'a':"welcome",'b':"to",'c':"ITI"}}

print(my_Dict[1])

print(my_Dict[3]['a'])


"""


emp_Dict=dict()

selector=int(input ("chose >>1 to add emp\nchose >>2 to print emp\nchose >>3 to remove emp\n"))


while(selector>0):
	if selector==1:
		id_key=int(input("enter emp id"))
		name_key=input("enter emp name")
		sallary_key=int (input("enter emp sallary"))
		x=dict()
		x['sallary']=sallary_key
		x['name']=name_key
		emp_Dict[id_key]=x
		
	elif (selector==2):
			print (emp_Dict)
	elif (selector==3):
		"""reject_emp=emp_Dict()
		"""emp_Dic
		
	
	selector=int(input ("chose >>1 to add emp\nchose >>2 to print emp\nchose >>3 to remove emp\n"))

		

		



































