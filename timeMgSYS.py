my_plan_dict=dict()

my_achived_plan=dict()


#print ("________________________بكُل فخْر صُنِعَ فيْ مصّر ______________________________")



print("to add task >>>>press1")

File=open("TimeMange.txt",'a+',encoding='utf-8')
x= int(input("You select:"))

while(x > 0):
	
	if (x==1):
		hour_key=str(input ("enter the task time:"))

		task=input ("enter the task ")
		my_plan_dict[hour_key]=task
		File.write("\n"+repr(my_plan_dict[task]) )

	print(my_plan_dict)
	
	x= int(input("to add another task >>>1:\nto add achived task>>>>2:"))
	if (x==2):
		achived_task=input("enter the task u achived ")
		for i in my_plan_dict:
			if achived_task in my_plan_dict:
				print("Great Job!!")
				my_achived_plan[i]=my_plan_dict[i]
				print(i)
				
				my_plan_dict.pop(i)
			else :
				pass

		x= int(input("to add another achived hour >>>2:\nto out>>>>1:\nto print the achived tasks press 3:"))
	
	if (x==3):
		print (f"u have achived {my_achived_plan}")
		x= int (input ("to out to enter task >>>>1:\nto print the achived tasks again press 3:\nto print un achived task>>>4:"))
	if (x==4):
		
		print (f"u have not achived {my_plan_dict}")

		


		



