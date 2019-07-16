# importing csv module 
import csv 
import os

# csv file name 
filename = "list.csv"
 
fields = [] 
rows = [] 
success =0;
failed =0;
commandIndex = -1;
runIndex = -1;
resultIndex = -1;
nameIndex = -1;

def saveResult(filecontent):
	f = open('runResult.csv', 'w+')
	f.write(filecontent)
	f.close()

	
def getColIndex(argument):
    for i in range(len(argument)):
		global commandIndex
		global runIndex
		global nameIndex
		if(argument[i]=='command'):
			commandIndex = i
		elif(argument[i]=='run'):
			runIndex = i
		elif(argument[i]=='testName'):
			nameIndex = i

def readCsv(filename):
	global fields
	global rows
	with open(filename, 'r') as csvfile: 
		csvreader = csv.reader(csvfile) 
		fields = csvreader.next() 
		for row in csvreader: 
			rows.append(row) 

# reading csv file 
readCsv(filename)

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
headers = ', '.join(field for field in fields)
headers= headers + ', result\n'
csvLines = ''
print headers

#for field in fields:
getColIndex(fields)

print('executing tests') 
for row in rows[:5]:
	x = ''
	if(row[runIndex]=='y'):
		#executing commands
		x=os.system(row[commandIndex])
		if(x==0):
			success = success + 1
		else:
			failed = failed + 1
	print('\n')
	if(x==''):
		testResult = 'NOT_RUN'
	elif(x==0):
		testResult = 'PASSED'
	else:
		testResult = 'FAILED'
	csvLines = csvLines + ', '.join(row) + ', ' + testResult + '\n'
	print("Test Run status of %s is %s" %(row[nameIndex] , testResult))
	result = headers +csvLines
print('total success =%3d ; total failed =%3d' %(success,failed)) 

print result

saveResult(result)

print("end of script")

