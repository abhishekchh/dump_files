# importing csv module 
import csv 
import os

# csv file name 
filename = "list.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 
success =0;
failed =0;

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

print('executing tests') 
for row in rows[:5]:
	if(row[1]=='y'):
		#executing commands
		x=os.system(row[0])
		if(x==0):
			success = success + 1
		else:
			failed = failed + 1
		print("status of print is %d", x)
	print('\n') 
	print('total success = %d ; total failed = %d',success,failed) 

print("end of script")
