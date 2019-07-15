# importing csv module 
import csv 
import os

# csv file name 
filename = "list.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 	
	# extracting field names through first row 
	fields = csvreader.next() 
	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 
	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

print('\nFirst 5 rows are:\n') 
for row in rows[:5]:
	if(row[1]=='y'):
		#executing commands
		os.system(row[0])
	print('\n') 

print("end of script")
