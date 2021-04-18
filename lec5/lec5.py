my_list=['alaa',1,2,32,43,4]

my_dict={1:"alaa",2:"ahmed"}
"""
print(my_list)
print(my_dict)

print(f'my_dict key element of {1} id {my_dict[1]}')
print(f'my_list of {0} id {my_list[0]}')
print(my_dict[1])
my_list[0]='ahmed'

print(my_list)

my_dict['List']=my_list


print(my_dict['List'][4])

print(f'my_dict after adding the list is {my_dict}')

print(f"my_dict first list element is {my_dict['List'][4]}")


"""
#........................................ask2 is there difference between " and  ''
#........................................ask1

"""
dict1 = {'a':[1], 'b':[2]}
dict2 = {'b':[3], 'c':[4]}

dict3=dict()
                          #dict3 = {'a':[1], 'b':[2,3], 'c':[4]}  #i need this output 
temp_list=list()
for i in dict1 :
	print(i)

	if i  not in  dict2:
		dict3[i]=dict1[i]
	elif i in dict2:
		temp_list=[dict1[i],dict2[i]]
		dict3[i]=temp_list
	for i in dict2:
		if i not in dict1:
			dict3[i]=dict2[i]
		
my_list1=list()
my_list1.extend("abcdefghijklmonpqrstuvwxyz")
my_list2=list()
my_list2=my_list1.copy()
my_list2.insert(0,"abcdefghijklmonpqrstuvwxyz")
print(my_list2)
print(dict3)
dict3["alphabetic"]=my_list1
x=dict3['b'][0].pop(0)
dict3['b'].clear()
print(x)
print(dict3)



"""

#.................................................



"""

my_list.extend("12345678")

print(f"by_list after extend :{my_list}")

"""

my_tuple=tuple()


my_tuple=(1,1,1,4,5,6,"ebrahim","ahmed")



print(f"the tuple u hav entered is {my_tuple}")


x= my_tuple.index("ahmed")

print(x)

print (my_tuple.count(1))





























