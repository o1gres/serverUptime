#!/usr/bin/python
import pymysql.cursors
import os
import time
import traceback
import sys
from threading import Thread


serverList = {}
serverList["162.244.29.55"] = 'developer3'
serverList["64.137.210.237"] = 'developer2'
serverList["64.137.233.195"] = 'windows'

uptime = []
downtime = []
isUp = []

crash = 0
i = 0
frequencyChekServerStatus = 50 #in seconds



#DATABASE
db = pymysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     password="root",  # your password
                     db="serevrstatus")        # name of the data base

cur = db.cursor()

#try:

def developer():
	
	global serverList
	global uptime
	global downtime
	global isUp
	global crash
	

	if crash == 0: 
		for key, value in serverList.items():
			try:
				crash = 1
				cur.execute('SELECT uptime FROM statistiche WHERE ip= "' + key + '";')
				result  = cur.fetchone()
				uptime.append(int(result[0]))

				cur.execute('SELECT downtime FROM statistiche WHERE ip="' + key + '";')
				result  = cur.fetchone()
				downtime.append(int(result[0]))
			except Exception:
				print "IP: "+str(key)+" not found in table statistics"




def developer3loop(uptime, downtime):
	
	global serverList
	global isUp
	global crash
	global i
	global frequencyChekServerStatus

	db3 = pymysql.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     password="root",  # your password
	                     db="serevrstatus")        # name of the data base

	cur3 = db3.cursor()

	
	
	while True:
		for key, value in serverList.items():
			print "for"+str(i)	
			developer3 = str(key)
			print "developer3: "+str(developer3)
			
			try:
				response3 = os.system("ping -c 1 " + developer3)

				#and then check the response...
				if response3 == 0:
					isUp.insert(i, 1)
					#isUp[i] = 1
					uptimeTmp = uptime[i]
					uptime.insert(i, uptimeTmp+frequencyChekServerStatus)
					#uptime[i] = uptime[i] + 60
					sqlInsert3 = 'UPDATE `statistiche` SET `uptime` = "' + str(uptime[i]) +'" WHERE `statistiche`.`ip` = "' + str(key) + '";'
					cur3.execute(sqlInsert3)
					db3.commit()
				  	#print developer3, 'is up!'
				else:
					isUp.insert(i, 0)
					#isUp[i] = 1
					downtimeTmp = downtime[i]
					downtime.insert(i, downtimeTmp+frequencyChekServerStatus)
					sqlInsert2 = 'UPDATE `statistiche` SET `downtime` = "' + str(downtime[i]) +'" WHERE `statistiche`.`ip` = "' + str(key) + '";'
					cur3.execute(sqlInsert2)
					db3.commit()
				  	#print developer3, 'is down!'
			
			
			except Exception:
				print(traceback.format_exc())
    			print(sys.exc_info()[0])

			i = i+1	
			time.sleep(frequencyChekServerStatus)
		print "while"
		i=0	
		time.sleep (5)
		print "lol"
			
			

developer()
developer3loop(uptime, downtime)