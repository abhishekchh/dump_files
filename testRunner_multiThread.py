import sys
import csv 
import os
import array
import time
import threading
import random
from datetime import datetime

startTime = datetime.now().replace(microsecond=0)

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
envSetupIndex = -1;
criticalIndex = -1;
now = datetime.now()
current_time = now.strftime("%Y%m%d-%H%M%S")
reportFolder = 'Reports/' + current_time
result =[]
csvLines = []
rowsCopy = []
threadCount = 3
headers=''
f=''
criticalTag =''

def saveResult(line):
	global f
	csvWriter = csv.writer(f,delimiter=',',quotechar='"')
	csvWriter.writerow(line)
	
	
def getCriticalValue(key):
	if(key == 'high'):
		value=5
	elif(key == 'medium'):
		value=3
	elif(key == 'low'):
		value=0
	else:
		value=0;
	return value;
	
def getColIndex(argument):
	global commandIndex
	global runIndex
	global nameIndex
	global resultIndex
	global folderIndex
	global reportIndex
	global criticalIndex

	for i in range(len(argument)):
		if(argument[i]=='command'):
			commandIndex = i
		elif(argument[i]=='run'):
			runIndex = i
		elif(argument[i]=='testName'):
			nameIndex = i
		elif(argument[i]=='folderName'):
			folderIndex = i
		elif(argument[i]=='envSetup'):
			envSetupIndex = i
		elif(argument[i]=='reportFolder'):
			reportIndex = i
		elif(argument[i]=='critical'):
			criticalIndex = i
	resultIndex = len(argument)

def readCsv(filename):
	global fields
	global rows
	with open(filename, 'r') as csvfile: 
		csvreader = csv.reader(csvfile,quotechar='"') 
		fields = csvreader.next() 
		for row in csvreader: 
			rows.append(row) 

def execute(row):
	global failed
	global csvLines
	global result
	global noRun
	global success
	global commandIndex
	global runIndex
	global nameIndex
	global resultIndex
	global folderIndex
	global reportIndex
	global criticalIndex
	x = ''
	testScriptCritical = getCriticalValue(row[criticalIndex])
	if(row[runIndex]=='y' and testScriptCritical >= criticalTag):
		print("Setting up environment for "+ row[nameIndex])
		os.system(row[envSetupIndex])		
		print ("runnng test: " + row[nameIndex])
		print ("Executing command: "+row[commandIndex])
		x=os.system(row[commandIndex] + " 1> logs/" + row[nameIndex]+".log 2>logs/"+row[nameIndex]+".err")
		if(x==0):
			success = success + 1
			testResult = 'PASSED'
		else:
			failed = failed + 1
			testResult = 'FAILED'
		if(row[reportIndex]!=''):
			print ("moving report file "+row[reportIndex])
			os.system('mv '+row[reportIndex]+'* ' +reportFolder +'/'+row[nameIndex] )
		else:
			os.system('echo "report file Destination not defined; This is a place holder"> ' +reportFolder +'/'+row[nameIndex] +'-report.txt' )
	elif(x==''):
		noRun = noRun + 1
		testResult = 'NOT_RUN'
	row.append(testResult)
	csvLines.append(row)
	print("\nTest Run status of %s is %s" %(row[nameIndex] , testResult))
	


	
def worker():
	print(threading.current_thread().name)
	global rowsCopy
	while(len(rowsCopy)>0):
		#print("\n\n========================================")
		#print("worker thread "+threading.current_thread().name)
		#print("========================================\n\n")
		r = rowsCopy.pop()
		print(threading.current_thread().name , r)
		execute(r)
	print ("")

def main():
	global rowsCopy;
	global headers
	global f
	global criticalTag
	
	if (len(sys.argv) < 2):
		print ("no args")
		criticalTag =0
	else:
		criticalTag = getCriticalValue(sys.argv[1])
	
	# csv file name 
	filename = "list.csv"
	os.system('mkdir "'+reportFolder +'"')
	os.system("mkdir logs")
	
	# reading csv file 
	readCsv(filename)

	headers = fields
	headers.append('result')

	getColIndex(fields)

	print('executing tests') 

	rowsCopy = list(rows)
	testcaseCount = len(rows)

	threads = []
	for x in range(threadCount):
		print ("adding thread")
		threads.append(threading.Thread(target=worker, name=('thread'+str(x+1))))
		
	for x in range(threadCount):
		#print("starting thread " + str(x))
		time.sleep(0.5)	
		threads[x].start()

	for x in range(threadCount):
		#print("starting thread " + str(x))
		threads[x].join()

	print('\n\n============================================')
	print('TEST RUN COMPLETED')
	print('Total success runs\t =%3d \nTotal failed runs\t =%3d \nTests marked as no run\t =%3d' %(success,failed,noRun)) 
	print('============================================')

	f = open('runResult.csv', 'wb+')

	#result = headers +csvLines
	saveResult(headers)
	csvLines.reverse()
	for line in csvLines:
		saveResult(line)
	f.close()

	print("Script execution time is ")
	print(datetime.now().replace(microsecond=0) - startTime)
	print("end of script")


if __name__ == '__main__':
	main()
	
