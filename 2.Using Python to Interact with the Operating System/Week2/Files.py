with open("spider.txt") as file:
	lines=file.readlines()
	lines.sort()
	print(lines)
#	print(file.read())
#	for line in file:
#		print(line.strip().upper())



guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()


new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()



checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w+") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

#new directory
import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:#Return True if path is an existing directory. 
    os.makedirs(directory, exist_ok=True)#Recursive directory creation function. 
    
  # Create the new file inside of the new directory
  os.chdir(directory)#Change the current working directory to path.
  with open (filename,"w") as file:
    pass
  os.chdir("..")#Remember that '..' is a relative path alias that means "go up to the parent directory".

  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,"w") as new_file:
    new_file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

# new file
import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
    pass
  timestamp = os.path.getmtime(filename)

  # Convert the timestamp into a readable format, then into a string
  tm=datetime.datetime.fromtimestamp(timestamp).date()
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(tm))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


import os
def parent_directory():

  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), os.pardir)#Return a string representing the current working directory.
  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())