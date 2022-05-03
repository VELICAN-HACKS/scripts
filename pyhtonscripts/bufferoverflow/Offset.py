#!/usr/bin/python3
import sys, socket

offset = "Change  this to your value"
 
try: 
   		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('127.0.0.1, 9999'))
		s.send((' TRUN /.:/' + offset))
		s.close()

except:
		print " Error connecting to server"
		sys.exit()