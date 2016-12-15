#!/usr/bin/python
import pymysql.cursors
import os
import time
from threading import Thread

crash = 0;
uptimed2 = 0;
downtimed2 = 0;
uptimed3 = 0;
downtimed3 = 0;
isUp2 = 0;
isUp3 = 0;

#DATABASE
db = pymysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     password="root",  # your password
                     db="serevrstatus")        # name of the data base

cur = db.cursor()

try:
	if crash == 0:
		crash = 1
		#developer3
		cur.execute("SELECT uptime FROM statistiche WHERE ip='162.244.29.55'")
		result  = cur.fetchone()
		uptimed3 =  int(result[0])

		cur.execute("SELECT downtime FROM statistiche WHERE ip='162.244.29.55'")
		result  = cur.fetchone()
		downtimed3 =  int(result[0])
		

		#developer2
		cur.execute("SELECT uptime FROM statistiche WHERE ip='64.137.210.237'")
		result  = cur.fetchone()
		uptimed2 =  int(result[0])

		cur.execute("SELECT downtime FROM statistiche WHERE ip='64.137.210.237'")
		result  = cur.fetchone()
		downtimed2 =  int(result[0])

		db.close()

except Exception, e:
	print "Error with db: "+e.value


# UPDATE `statistiche` SET `uptime` = '10' WHERE `statistiche`.`ip` = '162.244.29.55';


#PING



#developer3
def developer3loop(uptimed3, downtimed3):
	db3 = pymysql.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     password="root",  # your password
	                     db="serevrstatus")        # name of the data base

	cur3 = db3.cursor()

	developer3 = "162.244.29.55"
	
	while True:
		try:
			response3 = os.system("ping -c 1 " + developer3)

			#and then check the response...
			if response3 == 0:
				isUp = 1
				uptimed3 = uptimed3 + 60
				sqlInsert3 = "UPDATE `statistiche` SET `uptime` =" + str(uptimed3) +" WHERE `statistiche`.`ip` = '162.244.29.55';"
				cur3.execute(sqlInsert3)
				db3.commit()
			  	#print developer3, 'is up!'
			else:
				isUp = 0
				downtimed3 = downtimed3 + 60
				sqlInsert2 = "UPDATE `statistiche` SET `downtime` =" + str(downtimed3) +" WHERE `statistiche`.`ip` = '162.244.29.55';"
				cur3.execute(sqlInsert2)
				db3.commit()
			  	#print developer3, 'is down!'
			time.sleep (60)	
		except Exception, e:
			print "Error with db: "+e.value



#developer2
def developer2loop(uptimed2, downtimed2):

	db2 = pymysql.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     password="root",  # your password
	                     db="serevrstatus")        # name of the data base

	cur2 = db2.cursor()

	developer2git = "64.137.210.238"
	while True:
		response2 = os.system("ping -c 1 " + developer2git)
		print response2
		#and then check the response...
		if response2 == 0:
			isUp = 1
			uptimed2 = uptimed2 + 60
			sqlInsert = "UPDATE `statistiche` SET `uptime` =" + str(uptimed2) +" WHERE `statistiche`.`ip` = '64.137.210.237';"
			cur2.execute(sqlInsert)
			db2.commit()
		  	#print developer2git, 'is up!'
		else:
			isUp = 0
			downtimed2 = downtimed2 + 60
			sqlInsert = "UPDATE `statistiche` SET `downtime` =" + str(downtimed2) +" WHERE `statistiche`.`ip` = '64.137.210.237';"
			cur2.execute(sqlInsert)
			db2.commit()
		  	#print developer2git, 'is down!'
		time.sleep (60)	


threadDeveloper2 = Thread(target=developer2loop, args=(uptimed2, downtimed2))
threadDeveloper2.deamon = True
#time.sleep(2)
threadDeveloper3 = Thread(target=developer3loop, args=(uptimed3, downtimed3))
threadDeveloper3.deamon = True

threadDeveloper2.start()
threadDeveloper3.start()