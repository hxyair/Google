'''
import csv

with open('software_sample.csv') as software:
	reader=csv.DictReader(software)
# writer=csv.DictWriter(by_department, fieldnames=keys)
# writer.writeheader()
# writer.writerrows()
	for row in reader:
		print(("{} used {} keys").format(row["Name"],row["Used"]))

'''
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader=csv.DictReader(file)
    # row is now a dictionary, e.g. {'color': 'pink', 'type': 'annual', 'name': 'carnation'}
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

'''
# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as f:
    # Read the rows of the file
    rows = csv.reader(f)
    # Process each row
    line_count = 0
    for row in rows:
      name,color,typ = row
      # Format the return string for data rows only
      if line_count != 0:
        return_string += "a {} {} is {}\n".format(name,color,typ)
      line_count += 1
    
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
'''




#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
#The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#You now need to iterate over the CSV file that you opened, i.e., employee_file. When you iterate over a CSV file, each iteration of the loop produces a dictionary from strings (key) to strings (value).
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list
employee_list = read_employees('/home/student-04-3a9de588b8f8/data/employees.csv')
#print(employee_list)
def process_data(employee_list):
#Now, initialize a new list called department_list, iterate over employee_list, and add only the departments into the department_list.
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
#The department_list should now have a redundant list of all the department names. We now have to remove the redundancy and return a dictionary. We will return this dicationary in the format department:amount, where amount is the number of employees in that particular department.
  department_data = {}
#This uses the set() method, which converts iterable elements to distinct elements.
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
#The count() method returns the number of times element appears in the list.
  return department_data
dictionary = process_data(employee_list)
#print(dictionary)
def write_report(dictionary, report_file):
#Once you open the file for writing, iterate through the dictionary and use write() on the file to store the data.
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()
write_report(dictionary, '/home/student-04-3a9de588b8f8/test_report.txt')
