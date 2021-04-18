

from time import sleep
def loading ():
	print("")
	print("LOADING")
	for i in range(1,30):
		print('.', end='',flush=True)
		sleep(.1) 
	print("")		

Hr_members={'alaa':1234,'ahmed':5678,'ebrahim':9101}

new_dict=dict()
count=1
while(count>0):
	print("___________________welcome to the company system_________________________")
	count=select=int(input ("to access Hr system press 1\nto access employ system press 5\nto exit press 0\nYour choise is :"))
	if (count==0):
		print("______________________________Thank u__________________________________\n\n")
		break

	if (select==1):
		
		x=y=3
		while(x>0):
			Hr_name=str(input("please enter your user name:"))
			Hr_name=Hr_name.lower()
			Hr_name=Hr_name.strip()
			y=3
			while(y>0):	
				if Hr_name in Hr_members:
					Hr_Pass=int (input("please enter your password"))
				
					if Hr_Pass ==Hr_members[Hr_name] :
					
						print(f"_____________________welcome mr {Hr_name} to HR system__________________")
						
						count=2
						y=x=0
					else:
						print(f"in correct password try again!!")
						y=y-1
				else:
					print(f"incorrect user name")
					y=0

				
				
				
	while(count==2):
		#print("______________________________________HR System __________________________________\n\n")	
		count=int (input("to enter employ data press 2: \nto clear employ data press 3: \nto see all emp data press 4:\nto back press1\nYour select is : "))
		if (count==2):
			new_dict1= dict()
			ID=int (input("please enter your emp id : "))
			name= (input("please enter your emp  name : "))
			sallary= (input("please enter your emp  sallary : "))
		
			new_dict[ID]=new_dict1
			new_dict1['sallary']=sallary
			new_dict1['name']=name
			loading ()   	
			print("element added succesfuly")		
		


		if (count==3):
			rejected_member=int(input("enter the ID of emp u want to reject"))
			if rejected_member in Hr_members:

				new_dict.pop(rejected_member)
				#Hr_members[id].clear(rejected_member)
				
			else :
				print("Sorry no member match {rejected_member}")
			count=2
		elif count==4:
			
			loading ()
	
			print(new_dict)
			count=2
	if count==5:
		emp_id=int(input ("please enter your id"))
		loading ()
		if emp_id in new_dict:
			loading () 
			print(" ")
			print(f"your data is :{new_dict[emp_id]}")
		else:
			print(f"your ID:{emp_id} don't exist")
			
		
		

		




















































