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
			
		
