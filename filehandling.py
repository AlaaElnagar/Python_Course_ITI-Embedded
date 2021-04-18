#file handling :
#file handling is very easy in python 
#file handling is very important part 
#and have built in functions to creat read write files 
#file handling requirements
	#1-files :are named locations on hard disk >>non voltile memory to store data 
"""
#steps to handle file :
	
	1-open a file or creat file and open it 
	
	2-achive metion (read,write,append,.....)
	
	3-close the file 


1-OPENING FILE 
	-CREATED VARIABLE(X)=OPEN("FILE PATH","MODE") 
	
		-MODE :BY DIFAULT ITS >>READ FILE 
			- r >>>>>>>>>read from file   lazem ykon el file mowgoood 
			-w >>>>>>>>>>write to afile on the first line and over write
			-a >>>>>>>>>>append to a file start at the end of file
			-(r+) or rw >>>>>>>>>read then write 
			-w+   or wr >>>>>>>>>write then read
			-a+   or ar >>>>>>>>>append then read 
			-B>>>>>>>>>>>Binary
			-T>>>>>>>>>>>text
			-x>>>>>>>>>>>creat file
			
x=File.read()  read all file
 
x=File.readline()  read only one line 

x=File.readlines() read all file and return list

file=open("c.text",'w')  creat new file and over write 

file=open("c.text",'a')  add elements to the file and contiue to the old things 
file=open("c.text",'r+')  allow you to read and write to a file 

file=open("c.text",'w+') start new file allow you to delete the file and then write  to it  

file=open("c.text",'w') 

file=open("c.text",'r+') 

File=open("alaa.txt",'a',encoding='utf-8')    allow you to change the language 

File.close() stop writing to a file 

"""
File=open("alaa.txt",'a+',encoding='utf-8')

File.write("\nبكُل فخْر صُنِعَ فيْ مصّر. ")
x=File.read()
print(x)
File.close()






















"""
File=open("alaa.text",'w') #to open a new file and read from it 

File.write("MMMMMMMMMyM firs time tosdfsljkgfdsfdsfdsgfgfdsgdssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssd write in file \n")
File.write("My second time to write in file\n ")
File.write("My sthird time to write in file\n ")

 # allow you to read the fileobject
File=open("alaa.text",'r')
'''line=File.read()  #return all the file elements
'''
'''print(line)
'''
#object [:object file.rfind()]
'''line=File.read()
print(line)
'''
'''
line=File.readlines(5)  
print(line[0])
'''
"""

"""x=line [:line.rfind('M')]

print(x)
"""

"""
x=File.readlines() #return all the file elements in one list
 

print(x)

line = File.readlines()
print(line)

"""
"""
File=open("alaa.text",'w+')

File.write("helwoshdflhdfldhfnhflfhsldlhfdlhlhdghd;lgh,nhjg.,dhgflclnmdfnfdsjsfd.hflkdskldnhfvfjfhfnskfdshfds")

#File=open("alaa.text",'r')


line=File.read()

print(line)

File=open("alaa.text",'w')      #if 'w' over write in every  thing 
"""

















 


	
	
