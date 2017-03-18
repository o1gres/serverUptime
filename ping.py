#!/usr/bin/python
import pymysql.cursors
import os
import time
import traceback
import sys
import sqlite3
from threading import Thread

dir = os.path.dirname(__file__)


serverList = {}
serverList["162.244.29.55"] = 'developer3'
serverList["64.137.210.237"] = 'developer2'
serverList["45.62.239.109"] = 'windows'

uptime = []
downtime = []
isUp = []

crash = 0
i = 0
frequencyChekServerStatus = 50 #in seconds



#DATABASE
	
db = sqlite3.connect('serverstatus')
#db = pymysql.connect(host="localhost",    		# your host, usually localhost
#                     user="root",         		# your username
#                     password="root",  			# your password
#                     db="serevrstatus")        	# name of the data base

cur = db.cursor()

#try:
#INSERT INTO `statistiche` (`ip`, `name`) VALUES ('127.0.0.1', 'pippo') ON DUPLICATE KEY UPDATE ip = '127.0.0.1'

def initializeDB():
	#DATABASE
	filename = os.path.join(dir, 'serverstatus')
	db = sqlite3.connect(filename)
	#db = pymysql.connect(host="localhost",    		# your host, usually localhost
	#                     user="root",         		# your username
	#                     password="root",  			# your password
	#                     db="serevrstatus")        	# name of the data base

	cur = db.cursor()


	for key, value in serverList.items():
			try:
				sqlInsert = 'INSERT INTO `statistiche` (`ip`, `name`) VALUES ("' + str(key) + '","'+ value + '" ) ON DUPLICATE KEY UPDATE ip = "' + str(key) + '"' 
				cur.execute(sqlInsert)
				db.commit()
			except Exception:
				print "IP: "+str(key)+" error initializing table"




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

	filename = os.path.join(dir, 'serverstatus')
	db3 = sqlite3.connect(filename)
	#db3 = pymysql.connect(host="localhost",    	# your host, usually localhost
	#                     user="root",         	# your username
	#                     password="root",  		# your password
	#                     db="serevrstatus")     # name of the data base

	cur3 = db3.cursor()

	
	
	while True:
		for key, value in serverList.items():
			developer3 = str(key)
			
			try:
				response3 = os.system("ping -c 1 " + developer3)

				if response3 == 0:
					isUp.insert(i, 1)
					uptimeTmp = uptime[i]
					uptime.insert(i, uptimeTmp+frequencyChekServerStatus)
					sqlInsert3 = 'UPDATE `statistiche` SET `uptime` = "' + str(uptime[i]) +'" WHERE `statistiche`.`ip` = "' + str(key) + '";'
					cur3.execute(sqlInsert3)
					db3.commit()
					uptimeTmp = 0

				else:
					isUp.insert(i, 0)
					downtimeTmp = downtime[i]
					downtime.insert(i, downtimeTmp+frequencyChekServerStatus)
					sqlInsert2 = 'UPDATE `statistiche` SET `downtime` = "' + str(downtime[i]) +'" WHERE `statistiche`.`ip` = "' + str(key) + '";'
					cur3.execute(sqlInsert2)
					db3.commit()
					downtimeTmp = 0

			
			except Exception:
				print(traceback.format_exc())
    			print(sys.exc_info()[0])

			i = i+1	
			time.sleep(frequencyChekServerStatus)
		i=0	
		time.sleep (5)

initializeDB()		
developer()
developer3loop(uptime, downtime)
