#!/usr/bin/python
import pymysql.cursors
import os
import time

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
		uptimed3 =  int(result[0])

		cur.execute("SELECT downtime FROM statistiche WHERE ip='64.137.210.237'")
		result  = cur.fetchone()
		downtimed3 =  int(result[0])

except Exception, e:
	print "Error with db: "+e.value


# UPDATE `statistiche` SET `uptime` = '10' WHERE `statistiche`.`ip` = '162.244.29.55';


#PING
developer3 = "162.244.29.55"
developer2git = "64.137.210.237"

#developer3
while True:
	response = os.system("ping -c 1 " + developer3)

	#and then check the response...
	if response == 0:
		isUp = 1
		uptimed3 = uptimed3 + 10
		sqlInsert = "UPDATE `statistiche` SET `uptime` =" + str(uptimed3) +" WHERE `statistiche`.`ip` = '162.244.29.55';"
		cur.execute(sqlInsert)
		db.commit()
	  	print developer3, 'is up!'
	else:
		isUp = 0
		downtimed3 = downtimed3 + 10
		sqlInsert = "UPDATE `statistiche` SET `downtime` =" + str(downtimed3) +" WHERE `statistiche`.`ip` = '162.244.29.55';"
		cur.execute(sqlInsert)
		db.commit()
	  	print developer3, 'is down!'
	time.sleep (10)	


sleep(2)

#developer2
while True:
	response = os.system("ping -c 1 " + developer2git)

	#and then check the response...
	if response == 0:
		isUp = 1
		uptime2 = uptime2 + 10
		sqlInsert = "UPDATE `statistiche` SET `uptime` =" + str(uptime2) +" WHERE `statistiche`.`ip` = '64.137.210.237';"
		cur.execute(sqlInsert)
		db.commit()
	  	print developer2git, 'is up!'
	else:
		isUp = 0
		downtime2 = downtime2 + 10
		sqlInsert = "UPDATE `statistiche` SET `downtime` =" + str(downtime2) +" WHERE `statistiche`.`ip` = '64.137.210.237';"
		cur.execute(sqlInsert)
		db.commit()
	  	print developer2git, 'is down!'
	time.sleep (10)	