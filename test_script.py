# importing csv module 
import csv 
import os
from datetime import datetime

fields = [] 
rows = [] 
success =0;
failed =0;
noRun =0;
commandIndex = -1;
folderIndex = -1;
runIndex = -1;
resultIndex = -1;
nameIndex = -1;
reportIndex = -1;
now = datetime.now()
current_time = now.strftime("%Y%m%d-%H%M%S")
reportFolder = 'Reports/' + current_time

# csv file name 
filename = "list.csv"
os.system('mkdir "'+reportFolder +'"')
 

def saveResult(filecontent):
	f = open('runResult.csv', 'w+')
	f.write(filecontent)
	f.close()

	
def getColIndex(argument):
	global commandIndex
	global runIndex
	global nameIndex
	global resultIndex
	global folderIndex
	global reportIndex

	for i in range(len(argument)):
		if(argument[i]=='command'):
			commandIndex = i
		elif(argument[i]=='run'):
			runIndex = i
		elif(argument[i]=='testName'):
			nameIndex = i
		elif(argument[i]=='folderName'):
			folderIndex = i
	resultIndex = len(argument)

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
#print('Field names are:' + ', '.join(field for field in fields)) 

headers = ', '.join(field for field in fields)
headers= headers + ', result\n'
csvLines = ''

getColIndex(fields)

print('executing tests') 
for row in rows[:5]:
	x = ''
	if(row[runIndex]=='y'):
		x=os.system(row[commandIndex])
		if(x==0):
			success = success + 1
			testResult = 'PASSED'
		else:
			failed = failed + 1
			testResult = 'FAILED'
		if(row[reportIndex]!=''):
			os.system('mv '+row[reportIndex]+'* ' +reportFolder +'/'+row[nameIndex] )
		else:
			os.system('echo "report file Destination not defined"' +reportFolder +'/'+row[nameIndex] )
	elif(x==''):
		noRun = noRun + 1
		testResult = 'NOT_RUN'
	csvLines = csvLines + ', '.join(row) + ', ' + testResult + '\n'
	print("\nTest Run status of %s is %s" %(row[nameIndex] , testResult))
	result = headers +csvLines
print('\n\n============================================')
print('TEST RUN COMPLETED')
print('Total success runs\t =%3d \nTotal failed runs\t =%3d \nTests marked as no run\t =%3d' %(success,failed,noRun)) 
print('============================================')

saveResult(result)

print("end of script")
