
import tkinter


window_name=tkinter.Tk()   #creat object from the window 

window_name.geometry("400x250+100+150")
'''
Button1=tkinter.Button(window_name,width=30,height=5,text='B1')
Button1.place(x=10,y=30)
Button1=tkinter.Button(window_name,width=30,height=5,text='B2')
Button1.place(x=100,y=60)
Button1=tkinter.Button(window_name,width=30,height=5,text='B3')
Button1.place(x=70,y=90)

window_name.mainloop()
'''
'''
Button1=tkinter.Button(window_name,width=30,height=5,text='B1')

Button1.grid(row=0,column=1)
Button2=tkinter.Button(window_name,width=30,height=5,text='B2')

Button2.grid(row=1,column=2)
Button2=tkinter.Button(window_name,width=30,height=5,text='B2')

Button2.grid(row=1,column=2)

window_name.mainloop()
'''
'''
def CommandB():

	print("Hellow from the other side")
def CommandB1():
	exit()

window_name.geometry("300x300+100+150")

i=0;
while(i<3):
	window_name.grid_rowconfigure(i,minsize=100)            #concerned with row number
	window_name.grid_columnconfigure(i,minsize=100)

	i+=1


Button1=tkinter.Button(window_name,width=30,height=5,text='Print name',bg="black",fg="silver",command=CommandB)

Button1.grid(row=1,column=0)
Button2=tkinter.Button(window_name,width=30,height=5,text='Exit',bg="blue",fg="yellow",command=CommandB1)

Button2.grid(row=1,column=2)
Button3=tkinter.Button(window_name,width=30,height=5,text='B3')
Button3.grid(row=0,column=1)
Button4=tkinter.Button(window_name,width=30,height=5,text='B4')
Button4.grid(row=2,column=1)


'''
'''
def print_Myname():
	global Entry1
	user=x=Entry1.get()
	Pass=x=Entry2.get()

	if user=="ahmed":
		if Pass=="1234":
			print(f'welcome {user}')
		else:
		print(f'dear {user} incorrect password')
	

else :
		
	print(f'incorrect user name {user}')
	

Button1=tkinter.Button(window_name,width=20,height=5,text='sumbit',bg="red",fg="silver",command=print_Myname)
Button1.grid(row=3,column=1)


Label1=tkinter.Label(window_name,width=20,text="user name")
Label1.grid(row=1,column=2)

Label2=tkinter.Label(window_name,width=20,text="password")
Label2.grid(row=2,column=2)

Entry1=tkinter.Entry(window_name,width=20)
Entry1.grid(row=1,column=1)

Entry2=tkinter.Entry(window_name,width=20,show="*")


Entry2.grid(row=2,column=1)
	
user=x=Entry1.get()
Pass=x=Entry2.get()

if user=="ahmed":
	if Pass=="1234":
		print(f'welcome {user}')
	else:
		print(f'dear {user} incorrect password')
	

else :
		
	print(f'incorrect user name {user}')


window_name.mainloop()

'''
"""

#tkinter.Radiobutton()

var=100
var=tkinter.IntVar()  #WE CANT ACCESS THE VAR WHICH HAVE THE VARIABLE  IN TK
var1=tkinter.IntVar()
def fun():
	global var
	if var.get()==0:
		print("led on")
	elif var.get()==1:
		print("led off")

def fun1():
	global var1
	if var1.get()==0:
		print("motor on")
	elif var1.get()==1:
		print("motor off")



RB1=tkinter.Radiobutton(window_name,value=0,variable=var,text="input1",command=fun)
RB1.grid(row=0,column=1)
RB2=tkinter.Radiobutton(window_name,value=1,variable=var,text="input2",command=fun)
RB2.grid(row=0,column=2)

#------------------------------------
RB3=tkinter.Radiobutton(window_name,value=0,variable=var1,text="input3",command =fun1)
RB3.grid(row=1,column=1)
RB4=tkinter.Radiobutton(window_name,value=1,variable=var1,text="input4",command =fun1)
RB4.grid(row=1,column=2)
#------------------------------------
RB5=tkinter.Radiobutton(window_name,value=0,variable=var,text="input5",command=fun)
RB5.grid(row=2,column=1)
RB6=tkinter.Radiobutton(window_name,value=1,variable=var,text="input6",command=fun)
RB6.grid(row=2,column=2)
#------------------------------------
RB7=tkinter.Radiobutton(window_name,value=0,variable=var,text="input7",command=fun)
RB7.grid(row=3,column=1)
RB8=tkinter.Radiobutton(window_name,value=1,variable=var,text="input8",command=fun)
RB8.grid(row=3,column=2)
#------------------------------------
RB9=tkinter.Radiobutton(window_name,value=0,variable=var,text="input9",command=fun)
RB9.grid(row=4,column=1)
RB10=tkinter.Radiobutton(window_name,value=1,variable=var,text="input9",command=fun)
RB10.grid(row=4,column=2)

#------------------------------------



window_name.mainloop()


"""

password=''

def Get_user():

	global Entry1
	global Entry1	
	user=Entry1.get()
	#Pass=x=Entry2.get()

def Num0():
	global password
	password=password+'0'
	display.insert(END,'0')

def Num1():
	global password
	password=password+'1'
	display.insert(END,'0')
def Num2():
	global password
	password=password+'2'
	display.insert(END,'0')
def Num3():
	global password
	password=password+'3'
	display.insert(END,'0')
def Num4():
	global password
	password=password+'4'
	display.insert(END,'0')
def Num5():
	global password
	display.insert(END,'0')
	password=password+'5'
def Num6():
	global password
	display.insert(END,'0')

	password=password+'6'

def Num7():
	global password
	password=password+'7'
	display.insert(END,'0')
def Num8():
	global password
	password=password+'8'
	display.insert(END,'0')
def Num9():
	global password
	password=password+'9'
	display.insert(END,'0')
def Enter():
	global Entry1
	user=Entry1.get()
	

	if password=="1234" and user=="ALAA":
		print("welcome")
		display.insert(END,'0\nok')

	else :
		print ("wrong password")
	display.insert(END,'0\n')



Button1=tkinter.Button(window_name,text='1',bg="black",fg="silver",command=Num1)
Button1.grid(row=3,column=0)


Button2=tkinter.Button(window_name,text='2',bg="black",fg="silver",command=Num2)
Button2.grid(row=3,column=1)


Button3=tkinter.Button(window_name,text='3',bg="black",fg="silver",command=Num3)
Button3.grid(row=3,column=2)


Button4=tkinter.Button(window_name,text='4',bg="black",fg="silver",command=Num4)
Button4.grid(row=4,column=0)


Button5=tkinter.Button(window_name,text='5',bg="black",fg="silver",command=Num5)
Button5.grid(row=4,column=1)


Button6=tkinter.Button(window_name,text='6',bg="black",fg="silver",command=Num6)
Button6.grid(row=4,column=2)


Button7=tkinter.Button(window_name,text='7',bg="black",fg="silver",command=Num7)
Button7.grid(row=5,column=0)


Button8=tkinter.Button(window_name,text='8',bg="black",fg="silver",command=Num8)
Button8.grid(row=5,column=1)


Button9=tkinter.Button(window_name,text='9',bg="black",fg="silver",command=Num9)
Button9.grid(row=5,column=2)

Button0=tkinter.Button(window_name,text='0',bg="black",fg="silver",command=Num0)
Button0.grid(row=6,column=0)

ButtonEnter=tkinter.Button(window_name,width=10,text="ENTER",bg="black",fg="silver",command=Enter)
ButtonEnter.grid(row=6,column=1)




Label1=tkinter.Label(window_name,width=20,text="user name")
Label1.grid(row=1,column=3)

Label2=tkinter.Label(window_name,width=20,text="password")
Label2.grid(row=2,column=3)

Entry1=tkinter.Entry(window_name,width=20)
Entry1.grid(row=1,column=1)

Entry2=tkinter.Entry(window_name,width=20,show="*")


Entry2.grid(row=2,column=1)

display



window_name.mainloop()


















 















