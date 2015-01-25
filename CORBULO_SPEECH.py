#=-=JNewbury=-=
#=-=-=-=-=-=-=-
#=-=Corbulo=-=-
#=-=-=-=-=-=-=-
#
# Import Modules
import webbrowser
import time
import sys
import speech_recognition as sr
import socket as so
import random
import platform
from socket import *
import urllib
import urllib2
from urllib2 import Request, urlopen
from Crypto.Cipher import AES
import string
import base64
import termios
import json
import time
import datetime
import os
import binascii
import subprocess
import pywapi
import string
import fnmatch
import platform
from time import sleep
from datetime import date
# Defining While Loop Variables
i = 0
# Defining Base Variables
pathcd = "/Users/JacobN"
path = ""
speak = 0
linef1 = ("")
linef2 = ("")
linef3 = ("")
linef4 = ("")
linef5 = ("")
localtime = time.asctime( time.localtime(time.time()) )
file = open("temp.txt", "a")
rootPath = "/Users/JacobN/Desktop/AI/Music"
# Defining Help Variables
youtubeh = "> search youtube for <query> : search query on youtube"
helph = "> help : shows list of commands available"
conversionh1 = "> conversion : conversion group (Temperature/Length)"
conversionh2 = "; asks for original units"
conversionh3 = "; asks for measurement of original units"
conversionh4 = "; asks for units to be converted to"
iph = "> ip : shows user's internal IP address and network's external IP address"
computeraliash = "> computer_alias : shows name of device that this script is being run on"
validateurlh = "> validate_url : tests validity of URL"
validateurlh1 = "; asks for URL"
searchamazonh = "> search amazon for <query> : search query on amazon"
searchgoogleh = "> search google for <query> : search query on google"
searchimagesh = "> search images for <query> : search query on google images"
encryptionh = "> encryption : opens menu for encryption"
encryptionh1 = "; asks user if encryption or decryption is wanted"
encryptionh2 = "; encryption ; asks for 16 character encryption key"
encryptionh3 = "; encrpytion ; asks for text to be encrypted"
encryptionh4 = "; decryption ; asks for pre-encrypted text"
encryptionh5 = "; decryption ; asks for 16 character encryption key"
musich = "> play <song name> : plays entered song"
musich1= "; !NOTE: MUSIC FILES MUST BE PLACED IN \"Music\" FOLDER"
exith = "> exit() : exits script"
cdandlsh = "> cd <directoryname> : virtually enters the entered directory"
cdandlsh1 = "> ls : outputs the available directories that can be used in corrolation with command \"cd\""
cdandlsh2 = "> cd : goes back a directory"
weatherh = "> weather : outputs weather in user's country"
togglespeechh = "> toggle_speech : toggles speech output"
mynameish = "> my name is <yourname> : tells Corbulo your name"
reminderh = "> make a reminder : asks user for reminder details"
reminderh1 = "; asks user for day (eg.Mon,Tues,Wed,Thu,Fri,Sat,Sun)"
reminderh2 = "; asks user for date (eg.1 - 30/31)"
reminderh3 = "; asks user for month (eg. Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec)"
reminderh4 = "; asks user for time (eg. 13:11:00) = 1:11pm)"
whoareyouh = "who are you? : asks Corbulo for it's name"
computerinfoh = "computer info : outputs computer info"
weighth = "calculate weight : asks for further needed calculation details"
weighth1 = "; asks user for preferred units of entered measurements, kg or lb (kg/lb)"
weighth2 = "; asks user for data depending or previously set preferred units of measurements"
weighth3 = "; asks user for planet for calculation simulation (eg. mecury, venus, earth, mars, jupiter, saturn, uranus, neptune)"
bmih = "calculate bmi : asks for further needed calculation details"
bmih1 = "; asks user if they prefer to input measurements in imperial or metric"
dbh = "create database : initiates database.csv and database.csv management python file creating phase"
dffurlh = "wget <URL> : asks user to enter url with file to download"
dffurlh1 = "; !NOTE: URLs MUST INCLUDE A '.' THEN A FILE FORMAT (eg. http://i.imgur.com/5MKOvMR.jpg)"
dbh1 = "; asks user for how many fields in user's database.csv"
dbh2 = "; asks user to input alias for each field user intends to have (not including primary key which will be put it automatically)"
dbh3 = "; asks user if they would like to make a python database managment file which allows user to input a new record into the previously created database and also search user entered query by searching specfic field then prints all lines which include query"
lolh = "lol : hahahahaha"
dawnmh = "dawn messenger : initiates dawn messenger program"
dawnmh1 = "; asks user for IP address which will be set to be the designated address for sending messages"
dawnmh2 = "; user will then have to wait until both computers are connected with the same command"
dawnmh3 = "; !NOTE: PROGRAM OPERATES SO THAT USERs WILL ONLY BE ALLOWED TO SEND ONE MESSAGE AT A TIME, USERs WILL HAVE TO WAIT FOR A REPLY TO SEND AGAIN"
matrixrh = "matrix rain : initiates matrix rain script"
matrixrh1 = "; script can be stopped by pressing 'Ctrl'+'C'"
newcustomcommand = "add new custom command : Adds additional custom inputted command"
newcustomcommand1 = "; !NOTE: MAKE SURE CUSTOM COMMAND IS LOWER CASE"
newcustomcommand2 = "; python script syntax : new line = '\\n'"
newcustomcommand3 = "; python script syntax : indents needed in code must be entered by using tab"
# Welcoming Message
if "25" in localtime and "Dec" in localtime:
	print ("Welcome, I Am Corbulo, Merry Christmas and What Would You Like To Do Today?")
else:
	print ("Welcome, I Am Corbulo, What Would You Like To Do Today?")
# While Loop Begins
while i != 10:
# Reminder Checking Process
	file = open('temp.txt','r')
	lines=file.readlines()
	num = sum(1 for line in open('temp.txt'))
	if num == 1:
		sptext = line1.split(" ") 
		linen11= " ".join(sptext[3:len(sptext)])
		linef11 = line1.rpartition(',')[0]
	elif num == 2:
		line1 = lines[0]
		line2 = lines[1]
		sptext = line1.split(" ") 
		linen11= " ".join(sptext[3:len(sptext)])
		linef11 = line1.rpartition(',')[0]
		sptext = line2.split(" ") 
		linen22= " ".join(sptext[3:len(sptext)])
		linef22 = line2.rpartition(',')[0]
	elif num == 3:
		line1 = lines[0]
		line2 = lines[1]
		line3 = lines[2]
		sptext = line1.split(" ") 
		linen11= " ".join(sptext[3:len(sptext)])
		linef11 = line1.rpartition(',')[0]
		sptext = line2.split(" ") 
		linen22= " ".join(sptext[3:len(sptext)])
		linef22 = line2.rpartition(',')[0]
		sptext = line3.split(" ") 
		linen33= " ".join(sptext[3:len(sptext)])
		linef33 = line3.rpartition(',')[0]
	elif num == 4:
		line1 = lines[0]
		line2 = lines[1]
		line3 = lines[2]
		line4 = lines[3]
		sptext = line1.split(" ") 
		linen11 = " ".join(sptext[3:len(sptext)])
		linef11 = line1.rpartition(',')[0]
		sptext = line2.split(" ") 
		linen22= " ".join(sptext[3:len(sptext)])
		linef22 = line2.rpartition(',')[0]
		sptext = line3.split(" ") 
		linen33 = " ".join(sptext[3:len(sptext)])
		linef33 = line3.rpartition(',')[0]
		sptext = line4.split(" ") 
		linen44= " ".join(sptext[3:len(sptext)])
		linef44 = line4.rpartition(',')[0]
	elif num == 5:
		line1 = lines[0]
		line2 = lines[1]
		line3 = lines[2]
		line4 = lines[3]
		line5 = lines[4]
		sptext = line1.split(" ") 
		linen11 = " ".join(sptext[3:len(sptext)])
		linef11 = line1.rpartition(',')[0]
		sptext = line2.split(" ") 
		linen22 = " ".join(sptext[3:len(sptext)])
		linef22 = line2.rpartition(',')[0]
		sptext = line3.split(" ") 
		linen33 = " ".join(sptext[3:len(sptext)])
		linef33 = line3.rpartition(',')[0]
		sptext = line4.split(" ") 
		linen44 = " ".join(sptext[3:len(sptext)])
		linef44 = line4.rpartition(',')[0]
		sptext = line5.split(" ") 
		linen55 = " ".join(sptext[3:len(sptext)])
		linef55 = line5.rpartition(',')[0]
	file.close()
	p = localtime
	p = str(localtime)
	year = p.split(" ") 
	checkf= " ".join(year[4:len(year)])
	checkf = str(checkf)
	check = p.rsplit(' ', 1)[0]
	if linef1 == check:
		subprocess.Popen(["open", "buzz.mp3"])
		print ("ALARM: "+linen11)
	elif linef2 == check:
		subprocess.Popen(["open", "buzz.mp3"])
		print ("ALARM: "+linen22)
	elif linef3 == check:
		subprocess.Popen(["open", "buzz.mp3"])
		print ("ALARM: "+linen33)
	elif linef4 == check:
		subprocess.Popen(["open", "buzz.mp3"])
		print ("ALARM: "+linen44)
	elif linef5 == check:
		subprocess.Popen(["open", "buzz.mp3"])
		print ("ALARM: "+linen55)
		
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    audio = r.listen(source)
	try:
		question= ""
		question = (r.recognize(audio))
	except LookupError:
	    print("Could not understand audio")
	
	if "Help" == question or "help" == question or "?" == question:
		os.system('clear')
		print ("\033[1m"+"> Commands:"+"\033[0m")
		print (youtubeh)
		print (helph)
		print (conversionh1)
		print (conversionh2)
		print (conversionh3)
		print (conversionh4)
		print (iph)
		print (computeraliash)
		print (validateurlh)
		print (validateurlh1)
		print (searchamazonh)
		print (searchgoogleh)
		print (searchimagesh)
		print (encryptionh)
		print (encryptionh1)
		print (encryptionh2)
		print (encryptionh3)
		print (encryptionh4)
		print (encryptionh5)
		print (musich)
		print (musich1)
		print (cdandlsh)
		print (cdandlsh1)
		print (cdandlsh2)
		print (weatherh)
		print (togglespeechh)
		print (mynameish)
		print (reminderh)
		print (reminderh1)
		print (reminderh2)
		print (reminderh3)
		print (reminderh4)
		print (whoareyouh)
		print (computerinfoh)
		print (weighth)
		print (weighth1)
		print (weighth2)
		print (weighth3)
		print (dbh)
		print (dbh1)
		print (dbh2)
		print (dbh3)
		print (dffurlh)
		print (dffurlh1)
		print (lolh)
		print (dawnmh)
		print (dawnmh1)
		print (dawnmh2)
		print (dawnmh3)
		print (matrixrh)
		print (matrixrh1)
		print (newcustomcommand)
		print (newcustomcommand1)
		print (newcustomcommand2)
		print (newcustomcommand3)
		print (exith)
	elif "search youtube for" in question or "Search_Youtube for" in question or "Search youtube for" in question or "search Youtube for" in question or "search youtube For" in question or "Search Youtube For" in question or "Search youtube For" in question or "search Youtube For" in question:
		sptext = question.split(" ") 
		youtube = " ".join(sptext[3:len(sptext)])
		webbrowser.open("http://www.youtube.com/results?search_query="+youtube)
	elif "Conversion" == question or "conversion" == question:
		convertq = raw_input(">Input Conversion Group (Temperature/Length): ")
		if "Temperature" == convertq or "temperature" == convertq:
			units = raw_input(">Input Origin Units (Celsius/Kelvin/Fahrenheit): ")
			unitsa = input(">Input Measurement (12): ")
			unitsd = raw_input(">Input End Conversion Units (Celsius/Kelvin/Fahrenheit): ")
			if "Celsius" == units or "celsius" == units:
				if "Fahrenheit" == unitsd == "fahrenheit" == unitsd:
					unitsda = ((unitsa*2)+30)
					ust = str(unitsda)
					popf = (ust+"F")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Kelvin" == unitsd or "kelvin" == unitsd:
					unitsda = (unitsa+273.15)
					ust = str(unitsda)
					popf = (ust+"K")
					print popf
					if speak == 1:
						os.system("say "+popf) 
			elif "Fahrenheit" == units == "fahrenheit" in units:
				if "Celsius" == unitsd == "celsius" in unitsd:
					unitsda = ((unitsa - 32)/1.8000)
					ust = str(unitsda)
					popf = (ust+"C")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Kelvin" == unitsd or "kelvin" == unitsd:
					unitsda = int(unitsa - 32)
					unitsda = int((unitsda/1.8)+273.15)
					ust = str(unitsda)
					popf = (ust+"K")
					print popf
					if speak == 1:
						os.system("say "+popf) 
			elif "Kelvin" == units or "kelvin" == units:
				if "Celsius" == unitsd or "celsius" == unitsd:
					unitsda = (unitsa-273.15)
					ust = str(unitsda)
					popf = (ust+"C")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Fahrenheit" == unitsd or "fahrenheit" == unitsd:
					unitsdaaa = (unitsa-273)
					unitsdaa = (unitsdaaa*1.8)
					unitsda = (unitsdaa+32)
					ust = str(unitsda)
					popf = (ust+"F")
					print popf
					if speak == 1:
						os.system("say "+popf) 
		elif "Length" == convertq or "length" == convertq:
			lengthdd = raw_input(">Input Origin Units (Minimeter/Meter): ")
			lengtha = input(">Input Measurement (12): ")
			if "Millimeter" == lengthdd or "millimeter" == lengthdd:
				lengthq = raw_input(">Input End Conversion Units (Millimeter/Centimeter/Meter/Kilometer/Mile/Inch/Feet/Yard/Nautical_Mile): ")
				if "Meter" == lengthq or "meter" == lengthq:
					lengthda = float(lengtha/1000)
					lst = str(lengthda)
					popf = (lst+"m")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Centimeter" == lengthq or "centimeter" == lengthq:
					lengthda = float(lengtha/10)
					lst = str(lengthda)
					popf = (lst+"cm")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Kilometer" == lengthq or "kilometer" == lengthq:
					lengthda = float(lengtha/1000000)
					lst = str(lengthda)	
					popf = (lst+"km")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Mile" == lengthq or "mile" == lengthq:
					lengthda = float(lengtha/1000000)
					lengthda = (lengthda*0.62137)
					lst = str(lengthda)
					popf (lst+" miles")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Inch" == lengthq or "inch" == lengthq:
					lengthda = float(lengtha*0.039370)
					lst = str(lengthda)
					popf = (lst+" inches")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Feet" == lengthq or "feet" == lengthq:
					lengthda = float(lengtha*0.0032808)
					lst = str(lengthda)
					popf = (lst+" ft")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Yard" == lengthq or "yard" == lengthq:
					lengthda = float(lengtha*0.0010936)
					lst = str(lengthda)
					popf = (lst+" yards")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Nautical_Mile" == lengthq or "nautical_mile" == lengthq or "Nautical_mile" == lengthq or "nautical_Mile" == lengthq:
					lengthda = float(lengtha*0.000000540)
					lst = str(lengthda)
					popf = (lst+" nautical miles")
					print popf
					if speak == 1:
						os.system("say "+popf) 
			elif "Centimeter" == lengthdd or "centimeter" == lengthdd:
				lengthq = raw_input(">Input End Conversion Units (Millimeter/Centimeter/Meter/Kilometer/Mile/Inch/Feet/Yard/Nautical_Mile): ")
				if "Millimeter" == lengthq or "millimeter" == lengthq:
					lengthda = float(lengtha*10)
					lst = str(lengthda)
					popf = (lst+"mm")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Meter" == lengthq or "meter" == lengthq:
					lengthda = float(lengtha/100)
					lst = str(lengthda)
					popf = (lst+"m")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Kilometer" == lengthq or "kilometer" == lengthq:
					lengthda = float(lengtha/1000)
					lst = str(lengthda)
					popf = (lst+"km")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Mile" == lengthq or "mile" == lengthq:
					lengthda = float(lengtha*0.0000062137)
					lst = str(lengthda)
					popf = (lst+" mile(s)")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Inch" == lengthq or "inch" == lengthq:
					lengthda = float(lengtha*0.39)
					lst = str(lengthda)
					popf (lst+"  inch(es)")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Feet" == lengthq or "feet" == lengthq:
					lengthda = float(lengtha*0.032)
					lst = str(lengthda)
					popf (lst+" ft")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Yard" == lengthq or "yard" == lengthq:
					lengthda = float(lengtha*0.010936)
					lst = (lengthda)
					popf = (lst+" yard(s)")
					print popf
					if speak == 1:
						os.system("say "+popf) 
				elif "Nautical_Mile" == lengthq or "nautical_mile" == lengthq or "Nautical_mile" == lengthq or "nautical_Mile" == lengthq:
					lengthda = float(lengtha/185200)
					lst = str(lengthda)
					popf (lst+" Nautical Mile(s)")
					print popf
					if speak == 1:
						os.system("say "+popf) 
			elif "Meter" == lengthdd or "meter":
				lengthq = raw_input(">Input End Conversion Units (Millimeter/Centimeter/Meter/Kilometer/Mile/Inch/Feet/Yard/Nautical_Mile): ")
				if "Millimeter" == lengthq or "millimeter" == lengthq:
					lengthda = float(lengtha*1000)
					lst = str(lengthda)
					popf = (lst+"mm")
					if speak == 1:
						os.system("say "+popf) 
				elif "Centimeter" == lengthq or "centimeter" == lengthq:
					lengthda = float(lengtha*100)
					lst = str(lengthda)
					popf = (lst+"cm")
					if speak == 1:
						os.system("say "+popf)
				elif "Kilometer" == lengthq or "kilometer" == lengthq:
					lengthda = float(lengtha/1000)
					lst = str(lengthda)
					popf = (lst+"km")
					if speak == 1:
						os.system("say "+popf)
				elif "Mile" == lengthq or "mile" == lengthq:
					lengthda = float(lengthda*0.00062137)
					lst = str(lengthda)
					popf = (lst+" mile(s)")
					if speak == 1:
						os.system("say "+popf)
				elif "Inch" == lengthq or "inch" == lengthq:
					lengthda = float(lengthda*39.370)
					lst = str(lengthda)
					popf = (lst+" inch(es)")
					if speak == 1:
						os.system("say "+popf)
				elif "Feet" == lengthq or "feet" == lengthq:
					lengthda = float(lengtha*3.2808)
					lst = str(lengthda)
					popf = (lst+" ft")
					if speak == 1:
						os.system("say "+popf)
				elif "Yard" == lengthq or "yard" == lengthq:
					lengthda = float(lengtha*1.0936)
					lst = str(lengthda)
					popf = (lst+" yard(s)")
					if speak == 1:
						os.system("say "+popf)
				elif "Nautical_Mile" == lengthq or "nautical_mile" == lengthq or "Nautical_mile" == lengthq or "nautical_Mile" == lengthq:
					lengthda = float(lengtha*0.000539956803456)
					lst = str(lengthda)
					popf = (lst+" Nautical Mile(s)")
					if speak == 1:
						os.system("say "+popf)
	elif "Hello" == question or "Hi" == question or "hello" == question or "hi" == question:
		print ("Greetings Human..")
		if speak == 1:
			os.system("say 'Greetings Human'")
		time.sleep(1)
		print ("What would you like to do? ")
		if speak == 1:
			os.system("say 'What would you like to do?'")
		time.sleep(1)
	elif "exit()" == question:
		print ("> Stopping...")
		time.sleep(1)
		sys.exit()
	elif "search amazon for" in question or "Search Amazon for" in question or "search Amazon for" in question or "Search amazon for" in question or "search amazon For" in question or "Search Amazon For" in question or "search Amazon For" in question or "Search amazon For" in question:
		sptext = question.split(" ") 
		amazq = " ".join(sptext[3:len(sptext)])
		pageFile = urllib2.urlopen("http://www.infosniper.net/")
		pageHtml = pageFile.read()
		pageFile.close()
		soup = pageHtml
		if "europe" in soup or "Europe" in soup:
			webbrowser.open("http://www.amazon.co.uk/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+amazq)
		elif "America" in soup or "america" in soup or "usa" in soup or "USA" in soup:
			webbrowser.open("http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="+amazq)
	elif "ip" == question or "IP" == question or "what is my ip" == question or "what is my IP" == question:
		inip = so.gethostbyname(so.gethostname())
		data = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
		exip = data["ip"]
		print ("> Internal IP address: "+inip)
		print ("> External IP address: "+exip)
	elif "Computer Alias" == question or "computer alias" == question:
		name = platform.node()
		name = name.rstrip(".local")
		print ("> Computer alias is "+name)
	elif "validate url:" in question or "Validate URL:" in question or "validate URL:" in question:
		sptext = question.split(" ") 
		linkd = " ".join(sptext[2:len(sptext)])
		if "http://" not in linkd or "www." not in linkd:
			print ("> Invalid URL!")
		elif "http://www." in linkd and ".com" in linkd or ".org" in linkd or ".co.uk" in linkd or ".io" in linkd or ".net" in linkd or ".gov" in linkd:
			print ("> URL is valid!")
	elif "Encryption" == question or "encryption" == question:
		PADDING = '{'
		BLOCK_SIZE = 32
		pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
		EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
		DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
		option=raw_input("Would You Like to Encrypt Or Decrypt Text?\n>Encrypt or Decrypt: ")
		if "Encrypt" == option or "encrypt" == option:
			secret1 = raw_input(">Input An Encryption Key Must Be 16 Characters Long: ")
			countTotal= (len(secret1))
			cipher = AES.new(secret1)
			data=raw_input(">Input Text You'd Like Encrypted: ")
			encoded = EncodeAES(cipher, data)
			print '>Encrypted string: ', encoded
		if "Decrypt" == option or "decrypt" == option:
			encoded=raw_input(">Input Encoded Text: ")
			secret=raw_input(">Input Decryption Key: ")
			cipher = AES.new(secret)
			decoded = DecodeAES(cipher, encoded)
			print '>Decrypted string: ', decoded
	elif "Play" in question or "play" in question:
		path = ""
		sptext = question.split(" ") 
		result = ' '.join(sptext[1:len(sptext)])
		patternh = str("*"+result+"*.mp3")
		for root, dirs, files in os.walk(rootPath):
		    for filename in fnmatch.filter(files, patternh):
		        path = ( os.path.join(root, filename))
		if path == "":
			print "> File Does Not Exist!"
			q = raw_input("> Search for .m4a files?: ")
			if "Yes" == q or "yes" == q:
				patternh = str("*"+result+"*.m4a")
				for root, dirs, files in os.walk(rootPath):
				    for filename in fnmatch.filter(files, patternh):
				        path = ( os.path.join(root, filename))
				if path == "":
					print "> Song not found"
		if path != "":
			print ("> Playing "+result+" now")
			if speak == 1:
				os.system("say playing "+result+" for you now!") 
			time.sleep(0.24)
			subprocess.Popen(["open", path])
	elif "Search Google for" in question or "search google for" in question or "Search google for" in question or "search Google for" in question or "Search Google For" in question or "search google For" in question or "Search google For" in question or "search Google For" in question:
		sptext = question.split(" ") 
		google = " ".join(sptext[3:len(sptext)])
		webbrowser.open("http://www.google.co.uk/?gfe_rd=cr&ei=T7aMVL3oO4zDUPXqgUA&gws_rd=cr#q="+google)
	elif "Search Images for" in question or "search images for" in question or "Search images for" in question or "search Images for" in question or "Search Images For" in question or "search images For" in question or "Search images For" in question or "search images For" in question:
		sptext = question.split(" ") 
		image = " ".join(sptext[3:len(sptext)])
		webbrowser.open("http://www.google.co.uk/search?q="+image+"&source=lnms&tbm=isch&sa=X&ei=s7uMVMyKMYiV7Aal3YGYAw&ved=0CAYQ_AUoAQ&biw=1361&bih=676")
	elif "clear()" == question:
		osname = platform.system()
		if "darwin" == osname or "Darwin" == osname or "Linux" == osname or "linux" == osname:
			os.system('clear')
		elif "window" in osname or "Window" in osname:
			os.system("cls")
	elif "ls" == question or "LS" == question:
		dirList=os.listdir(pathcd)
		f = dirList
		if ".DS_Store" in f:
			f.remove(".DS_Store")
		for item in dirList:
			print item
	elif "cd " in question:
		sptext = question.split(" ") 
		result = ' '.join(sptext[1:len(sptext)])
		pathcd = (pathcd+"/"+result)
	elif "cd" == question:
		if pathcd != "":
			pathcd = '/'.join(pathcd.split('/')[:-1])
		elif pathcd == "":
			pathcd = pathcd
	elif "time" == question or "Time" == question:
		localtime = time.asctime( time.localtime(time.time()) )
		print "Local current time :", localtime
		sptext = p.split(" ") 
		timecheck = " ".join(sptext[3:len(sptext)])
		timecheck = timecheck.rsplit(' ', 1)[0]
		daytecheck = p.rsplit(' ', 2)[0]
		yearcheck = " ".join(sptext[4:len(sptext)])
		if speak == 1:
			os.system("say "+"The time now is "+timecheck+" on the "+daytecheck+" in "+yearcheck)
	elif "Weather" == question or "weather" == question or "what is the weather like" == question or "What Is The Weather Like" == question:
		weather_com_result = pywapi.get_weather_from_weather_com('UKXX0085')
		yahoo_result = pywapi.get_weather_from_yahoo('UKXX0085')
		noaa_result = pywapi.get_weather_from_noaa('KJFK')
		lolp = ("> Weather.com says it is " + string.lower(weather_com_result['current_conditions']['text']) + " and it is " + weather_com_result['current_conditions']['temperature'] + " degrees celsius now in the United Kingdom!")
		lolps = ("Weather.com says it is " + string.lower(weather_com_result['current_conditions']['text']) + " and it is " + weather_com_result['current_conditions']['temperature'] + " degrees celsius now in the United Kingdom!")
		print lolp
		if speak == 1:
			os.system("say "+lolps) 
	elif "Toggle Speech" == question or "toggle speech" == question or "Toggle speech" == question or "toggle Speech" == question or "turn speech on" == question or "turn speech off" == question:
		if speak == 1:
			speak = (speak-1)
			print ("> Speech output is toggled off")
		elif speak == 0:
			speak = (speak+1)
			print ("> Speach output is toggled on")
	elif "my name is " in question or "My name is " in question or "my Name is " in question or "my name Is " in question or "My Name is " in question or "my Name Is " in question or "My Name Is " in question:
		sptext = question.split(" ") 
		name= " ".join(sptext[3:len(sptext)])
		names = ("Hello there "+name)
		print ("> Hello there "+name)
		if speak == 1:
			os.system("say "+names)
	elif "make reminder" == question or "make a reminder" == question or "set reminder" == question or "set a reminder" == question:
		timer = raw_input("> Input day (eg.Mon,Tues,Wed,Thu,Fri,Sat,Sun): ")
		timed = raw_input("> Input date (eg.1 - 30/31): ")
		timem = raw_input("> Input month (eg. Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec): ")
		timet = raw_input("> Input time (eg. 13:11:00) = 1:11pm): ")
		note = raw_input("> Input note: ")
		leep = (timer+" "+timem+" "+timed+" "+timet+", "+ note)
		leel = (leep+"\n")
		file.write(leel)
		rs = ("> Reminder set!")
		rss = ("Reminder set!")
		print (rs)
		if speak == 1:
			os.system("say "+rss)
	elif "who are you" == question:
		print ("> Me?")
		time.sleep(2)
		print ("> I am Corbulo, named after Gnaeus Domitius Corbulo, a Roman general who believed in honour and legacy.")
		time.sleep(4)
		print ("> He cryed out 'Axios!' when dying, although this having different meanings, it is most known to mean 'I am worthy!' as he believed that no matter what, a person or any mighty being can achieve greatness.")
		time.sleep(8)
		print("> What is your name?")
	elif "computer info" == question or "Computer Info" == question:
		osname = platform.system()
		if "darwin" == osname or "Darwin" == osname:
			osid = ("OS X")
		elif "Linux" == osname or "linux" == osname:
			osid = ("Linux")
		elif "window" in osname or "Window" in osname:
			osid = ("Windows")
		name = platform.node()
		name = name.rstrip(".local")
		computerinfo = ("> Name of Computer: "+name+"\n> Type of Operating System: "+osid)
		print computerinfo
	elif "calculate weight" == question or "Calculate Weight" == question:
		mass = raw_input("> kg or lb: ")
		if "lb" in mass:
			mass = input("> Input mass in lb: ")
			mass = (mass/2.2)
		elif "kg" in mass:
			mass = input("> Input mass in kg: ")
		planet = raw_input("> Input Planet For Weight Calculation Simulation: ")
		if "Mecury" in planet or "mecury" in planet:
			weight = (mass*3.8)
		elif "Venus" in planet or "venus" in planet:
			weight = (mass*8.8)
		elif "Earth" in planet or "earth" in planet:
			weight = (mass*9.8)
		elif "Mars" in planet or "mars" in planet:
			weight = (mass*3.8)
		elif "Jupiter" in planet or "jupiter" in planet:
			weight = (mass*25)
		elif "Saturn" in planet or "saturn" in planet:
			weight = (mass*10.4)
		elif "Uranus" in planet or "uranus" in planet:
			weight = (mass*10.4)
		elif "Neptune" in planet or "neptune" in planet:
			weight = (mass*13.8)
		weight = str(weight)
		winfo = ("> Your weight on the planet "+planet+" is "+weight+" N")
		winfos = ("Your weight on the planet "+planet+" is "+weight+" Newtons")
		print (winfo)
		if speak == 1:
			os.system("say "+winfos)
	elif "wget " in question:
		sptext = question.split(" ") 
		sop = " ".join(sptext[1:len(sptext)])
		print "> URL is valid!"
		time.sleep(2)
		if "." in sop:
			extracted_url = sop[sop.rfind("/")+1:];
			lop = sop.split(".")[-1]
			lopd = ("."+lop)
			binkd = os.path.isfile(lopd)
			if binkd == True:
				print ("> File Already Exits With That Alias!")
				time.sleep(1)
				editc = raw_input("> Would you like to delete this file and replace it, cancel process or save with a different name? (Delete/Rename/Cancel) ")
				if 'Cancel' == editc or 'cancel' == editc:
					exit('> Cancelled!')
				if 'Rename' == editc or 'rename' == editc:
					name = raw_input("> Enter alias for file to be saved as: ")
					extracted_url = name
				if 'Delete' == editc or 'delete' == editc:
					os.remove(extracted_url)
					print "> File Deleted, re-enter command to initiate download again"
					time.sleep(1)
					os.execl(sys.executable, *([sys.executable]+sys.argv))
			print ("> "+extracted_url + " is downloading..")
			urllib.urlretrieve (sop, extracted_url)
	elif "bmi calculator" == question or "BMI Calculator" == question:
		unit = raw_input("> Input units of which measurements would be entered(Imperial/Metric): ")
		if "Imperial"in unit or "imperial" in unit:
			pounds = input("> Input weight in pounds: ")
			height = input("> Input height in inches: ")
			bmi = (pounds*703)/(height*height)
			bmis = str(bmi)
			print ("> Your BMI is: "+bmis)
		if "Metric" in unit or "metric" in unit:
			kilog = input("> Input weight in kilograms: ")
			height = input("> Input height in meters: ")
			bmi = kilog/(height*height)
			bmis = str(bmi)
			print ("> Your BMI is: "+bmis)
		if bmi < 18.5:
			state = str("underweight")
		if 18.5 <= bmi < 24.9:
			state = str("normal weight")
		if 25.0 <= bmi < 29.9:
			state = str("overweight")
		if 30 < bmi:
			state = str("obese")
		print ("> Your BMI shows that you are "+state)
	elif "Create Database" == question or "Create database" == question or "create Database" == question or "create database" == question:
		aa = ""
		bb = ""
		cc = ""
		dd = ""
		ee = ""
		ff = ""
		gg = ""
		hh = ""
		ii = ""
		part1 = "import os\nimport sys\nfile = open('database.csv', 'a')\nquestion = raw_input('New Record / Query : ')\nif 'New Record' in question or 'new record' in question or 'New record' in question or 'new Record' in question:\n	num_lines = sum(1 for line in open('database.csv'))\n	num = str(num_lines)\n	file = open('database.csv', 'r')\n	lines=file.readlines()\n	poi = str(lines[0])\n	words = ''.join(c if c.isalnum() else ' ' for c in poi).split()\n	words = list(words)\n	words.pop(0)\n	words.pop(0)\n	words.insert(0, 'Primary Key')\n	hum = len(words)\n	hum = (hum+1)\n"
		file = open("database.csv", "a")
		u = input("> Input amount of fields database would have (maximum of 7): ")
		o = u
		leek = "Primary Key"
		while o != 0:
			if "Primary Key" == leek:
				field = raw_input("> Input first field (not the primary key): ")
			else:
				field = raw_input("> Input field: ")
			leek = (leek+","+field)
			o -= 1
		if 1 == u:
			popp, a = leek.split(",")
		elif 2 == u:
			popp, a, b = leek.split(",")
		elif 3 == u:
			popp, a, b, c = leek.split(",")
		elif 4 == u:
			popp, a, b, c, d = leek.split(",")
		elif 5 == u:
			popp, a, b, c, d, e = leek.split(",")
		elif 6 == u:
			popp, a, b, c, d, e, f = leek.split(",")
		elif 7 == u:
			popp, a, b, c, d, e, f, g = leek.split(",")
		elif 8 == u:
			popp, a, b, c, d, e, f, g, h = leek.split(",")
		if os.stat("database.csv")[6]==0 == False:
			file.write(leek)
			file.close()
		contin = raw_input("> Would you like to create python database management file for your database (this would allow you to enter new records and search for records) ?: ")
		if "yes" == contin or "Yes" == contin:
			filepy = open("database_managment.py", "w")
			if 1 == u:
				bb = raw_input("> Input question that user will be asked for field 1(not the primary key): ")
				aa = str("aa = raw_input("+"'"+bb+"'"+")")
				part2 = "	"+aa+"\n	wit=str('\\n'+num+','+aa)\n"
				part6 = "elif 'Query' in question or 'query' in question:\n		query = raw_input('Search query by field: : ')\n		if 'Primary Key' in query or 'Primary key' in query:\n			keyq = raw_input('Input Key query (eg.1): ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n						print lines\n		elif Name == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n"
			elif 2 == u:
				bb = raw_input("> Input question that user will be asked for field 1(not the primary key): ")
				cc = raw_input("> Input question that user will be asked for field 2(not the primary key): ")
				aa = str("aa = raw_input("+"'"+bb+"'"+")")
				bb = str("bb = raw_input("+"'"+cc+"'"+")")
				part2 = "	"+aa+"\n	"+bb+"\n	wit=str('\\n'+num+','+aa+','+bb)\n"
				part6 = "elif 'Query' in question or 'query' in question:\n		query = raw_input('Search query by field: : ')\n		if 'Primary Key' in query or 'Primary key' in query:\n			keyq = raw_input('Input Key query (eg.1): ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n						print lines\n		elif '"+a+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+b+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n"
			elif 3 == u:
				bb = raw_input("> Input question that user will be asked for field 1(not the primary key): ")
				cc = raw_input("> Input question that user will be asked for field 2(not the primary key): ")
				dd = raw_input("> Input question that user will be asked for field 3(not the primary key): ")
				aa = str("aa = raw_input("+"'"+bb+"'"+")")
				bb = str("bb = raw_input("+"'"+cc+"'"+")")
				cc = str("cc = raw_input("+"'"+dd+"'"+")")
				part2 =	"	"+aa+"\n	"+bb+"\n	"+cc+"\n	wit=str('\\n'+num+','+aa+','+bb+','+cc)"
				part6 = "elif 'Query' in question or 'query' in question:\n		query = raw_input('Search query by field: : ')\n		if 'Primary Key' in query or 'Primary key' in query:\n			keyq = raw_input('Input Key query (eg.1): ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n						print lines\n		elif '"+a+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+b+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+c+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n"
			elif 4 == u:
				bb = raw_input("> Input question that user will be asked for field 1(not the primary key): ")
				cc = raw_input("> Input question that user will be asked for field 2(not the primary key): ")
				dd = raw_input("> Input question that user will be asked for field 3(not the primary key): ")
				ee = raw_input("> Input question that user will be asked for field 4(not the primary key): ")
				aa = str("aa = raw_input("+"'"+bb+"'"+")")
				bb = str("bb = raw_input("+"'"+cc+"'"+")")
				cc = str("cc = raw_input("+"'"+dd+"'"+")")
				dd = str("dd = raw_input("+"'"+ee+"'"+")")
				part2 = "	"+aa+"\n	"+bb+"\n	"+cc+"\n	"+dd+"\n	wit=str('\\n'+num+','+aa+','+bb+','+cc+','+dd)"
				part6 = "elif 'Query' in question or 'query' in question:\n		query = raw_input('Search query by field: : ')\n		if 'Primary Key' in query or 'Primary key' in query:\n			keyq = raw_input('Input Key query (eg.1): ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n						print lines\n		elif '"+a+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+b+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+c+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+d+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n"
			elif 5 == u:
				bb = raw_input("> Input question that user will be asked for field 1(not the primary key): ")
				cc = raw_input("> Input question that user will be asked for field 2(not the primary key): ")
				dd = raw_input("> Input question that user will be asked for field 3(not the primary key): ")
				ee = raw_input("> Input question that user will be asked for field 4(not the primary key): ")
				ff = raw_input("> Input question that user will be asked for field 5(not the primary key): ")
				aa = str("aa = raw_input("+"'"+bb+"'"+")")
				bb = str("bb = raw_input("+"'"+cc+"'"+")")
				cc = str("cc = raw_input("+"'"+dd+"'"+")")
				dd = str("dd = raw_input("+"'"+ee+"'"+")")
				ee = str("ee = raw_input("+"'"+ff+"'"+")")
				part2 = "	"+aa+"\n	"+bb+"\n	"+cc+"\n	"+dd+"\n	"+ee+"\n	wit=str('\\n'+num+','+aa+','+bb+','+cc+','+dd+','+ee)"
				part6 = "elif 'Query' in question or 'query' in question:\n		query = raw_input('Search query by field: : ')\n		if 'Primary Key' in query or 'Primary key' in query:\n			keyq = raw_input('Input Key query (eg.1): ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+a+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+b+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+c+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+d+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+e+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n"

			elif 6 == u:
				bb = raw_input("> Input question that user will be asked for field 1(not the primary key): ")
				cc = raw_input("> Input question that user will be asked for field 2(not the primary key): ")
				dd = raw_input("> Input question that user will be asked for field 3(not the primary key): ")
				ee = raw_input("> Input question that user will be asked for field 4(not the primary key): ")
				ff = raw_input("> Input question that user will be asked for field 5(not the primary key): ")
				gg = raw_input("> Input question that user will be asked for field 6(not the primary key): ")
				aa = str("aa = raw_input("+"'"+bb+"'"+")")
				bb = str("bb = raw_input("+"'"+cc+"'"+")")
				cc = str("cc = raw_input("+"'"+dd+"'"+")")
				dd = str("dd = raw_input("+"'"+ee+"'"+")")
				ee = str("ee = raw_input("+"'"+ff+"'"+")")
				ff = str("ff = raw_input("+"'"+gg+"'"+")")
				part2 = "	"+aa+"\n	"+bb+"\n	"+cc+"\n	"+dd+"\n	"+ee+"\n	"+ff+"\n	wit=str('\\n'+num+','+aa+','+bb+','+cc+','+dd+','+ee+','+ff)"
				part6 = "elif 'Query' in question or 'query' in question:\n		query = raw_input('Search query by field: : ')\n		if 'Primary Key' in query or 'Primary key' in query:\n			keyq = raw_input('Input Key query (eg.1): ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n						print lines\n		elif '"+a+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+b+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+c+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+d+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+e+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+f+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n"
			elif 7 == u:
				bb = raw_input("> Input question that user will be asked for field 1(not the primary key): ")
				cc = raw_input("> Input question that user will be asked for field 2(not the primary key): ")
				dd = raw_input("> Input question that user will be asked for field 3(not the primary key): ")
				ee = raw_input("> Input question that user will be asked for field 4(not the primary key): ")
				ff = raw_input("> Input question that user will be asked for field 5(not the primary key): ")
				gg = raw_input("> Input question that user will be asked for field 6(not the primary key): ")
				hh = raw_input("> Input question that user will be asked for field 7(not the primary key): ")
				aa = str("aa = raw_input("+"'"+bb+"'"+")")
				bb = str("bb = raw_input("+"'"+cc+"'"+")")
				cc = str("cc = raw_input("+"'"+dd+"'"+")")
				dd = str("dd = raw_input("+"'"+ee+"'"+")")
				ee = str("ee = raw_input("+"'"+ff+"'"+")")
				ff = str("ff = raw_input("+"'"+gg+"'"+")")
				gg = str("gg = raw_input("+"'"+hh+"'"+")")
				part2 = "	"+aa+"\n	"+bb+"\n	"+cc+"\n	"+dd+"\n	"+ee+"\n	wit=str('\\n'+num+','+aa+','+bb+','+cc+','+dd+','+ee+','+ff+','+gg)"
				part6 = "elif 'Query' in question or 'query' in question:\n		query = raw_input('Search query by field: : ')\n		if 'Primary Key' in query or 'Primary key' in query:\n			keyq = raw_input('Input Key query (eg.1): ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n						print lines\n		elif '"+a+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+b+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+c+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+d+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+e+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+f+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+g+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n"
			elif 8 == u:
				bb = raw_input("> Input question that user will be asked for field 1(not the primary key): ")
				cc = raw_input("> Input question that user will be asked for field 2(not the primary key): ")
				dd = raw_input("> Input question that user will be asked for field 3(not the primary key): ")
				ee = raw_input("> Input question that user will be asked for field 4(not the primary key): ")
				ff = raw_input("> Input question that user will be asked for field 5(not the primary key): ")
				gg = raw_input("> Input question that user will be asked for field 6(not the primary key): ")
				hh = raw_input("> Input question that user will be asked for field 7(not the primary key): ")
				ii = raw_input("> Input question that user will be asked for field 8(not the primary key): ")
				aa = str("aa = raw_input("+"'"+bb+"'"+")")
				bb = str("bb = raw_input("+"'"+cc+"'"+")")
				cc = str("cc = raw_input("+"'"+dd+"'"+")")
				dd = str("dd = raw_input("+"'"+ee+"'"+")")
				ee = str("ee = raw_input("+"'"+ff+"'"+")")
				ff = str("ff = raw_input("+"'"+gg+"'"+")")
				gg = str("gg = raw_input("+"'"+hh+"'"+")")
				hh = str("hh = raw_input("+"'"+ii+"'"+")")
				part2 = "	"+aa+"\n	"+bb+"\n	"+cc+"\n	"+dd+"\n	"+ee+"\n	"+ff+"\n	"+gg+"\n	"+hh+"\n	wit=str('\\n'+num+','+aa+','+bb+','+cc+','+dd+','+ee+','+ff+','+gg+','+hh)"
				part6 = "elif 'Query' in question or 'query' in question:\n		query = raw_input('Search query by field: : ')\n		if 'Primary Key' in query or 'Primary key' in query:\n			keyq = raw_input('Input Key query (eg.1): ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					if keyq in lines:\n						print lines\n		elif '"+a+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+b+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+c+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+d+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+e+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+f+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+g+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n		elif '"+h+"' == query:\n			keyq = raw_input('Input Query: ')\n			file = open('database.csv', 'r')\n			for lines in file:\n				if keyq in lines:\n					print lines\n"
			part3 = "\n	file = open('database.csv', 'a')\n	file.write(wit)\n	file.close()\n	words=str(words)\n"
			filepy.write(part1)
			filepy.write(part2)
			filepy.write(part3)
			filepy.write(part4)
			filepy.write("	print ('Recored Saved')\n")
			filepy.write(part6)
			print ("> Database.csv has been created!")
	elif "lol" == question or "LOL" == question or "Lol" == question:
		print ("> Yes, I know, it's very funny..")
		time.sleep(1.2)
		print ("> But just take some herbal remedies and it should go away..")
		time.sleep(1.5)
		print ("> Hopefully")
		time.sleep(1.2)	
	elif "dawn messenger" == question or "Dawn messenger" == question or "Dawn Messenger" == question or "dawn messenger" == question:
		dmi = 0
		lmi = 0
		host = ""
		secret= "jacobnewburyjaco"
		secret1 = secret
		PADDING = '{'
		checkcode = ''.join(random.choice('0123456789QWERTYUIOPLKJHGFDSAZXCVBNMasdfgjhklpoiuytrewqmnzbxvc') for i in range(16))
		BLOCK_SIZE = 32
		pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
		EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
		DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
		if dmi == 0:
			hostl = raw_input("> Input IP of computer message will be sent to: ")
			port = 13000
			buf = 1024
			addr = (host, port)
			addrl = (hostl, port)
			UDPSock = socket(AF_INET, SOCK_DGRAM)
			UDPSock.bind(addr)
			UDPSock.sendto(checkcode, addrl)
			while lmi == 0:
				print ("Waiting for connection...")
				(data, addr) = UDPSock.recvfrom(buf)
				if len(data) == 16:
					print "> Connection found!"
					lmi += 1	
				elif len(data) == 16 and data != checkcode:
					UDPSock.sendto(data, addrl)
					(data, addr) = UDPSock.recvfrom(buf)
					if len(data) == 16:
						print "> Connection found!"
			addr = (host, port)
			addrl = (hostl, port)
			dmi += 1
		print "Waiting to receive messages..."
		while dmi == 1:
			datal = raw_input("Enter message to send or type 'exit': ")
			countTotal= (len(secret1))	
			cipher = AES.new(secret1)
			encoded = EncodeAES(cipher, datal)
			UDPSock.sendto(encoded, addrl)
			if datal == "exit":
				UDPSock.close()
				dmi +=1
			else:
				(data, addr) = UDPSock.recvfrom(buf)
				encoded = data
				cipher = AES.new(secret)
				decoded = DecodeAES(cipher, encoded)
				print "Received message: "+ decoded
		print "Done!"	
	elif "matrix rain" == question or "Matrix Rain" == question or "Matrix rain" == question or "martix Rain" == question:
		print "> Sequence will begin in a moment, press 'ctrl'+'c' to end sequence"
		def Random(INT): 
		    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		    randstring = ''
		    try:
		        x = random.sample(chars, INT)
		    except ValueError:
		        print '\n[-]Maximum number of characters is 62'
		        return None
		    randstring = randstring.join(x)
		    return randstring
		try:
			while 1:
				a = Random(62)
				print a
		except KeyboardInterrupt:
				print "> Rain Ended!"
	elif "live binary translate" == question or "Live binary translate" == question or "Live Binary Translate" == question or "live Binary translate" == question or "live binary Translate" == question:
		TERMIOS = termios
		def getkey():
		        fd = sys.stdin.fileno()
		        old = termios.tcgetattr(fd)
		        new = termios.tcgetattr(fd)
		        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
		        new[6][TERMIOS.VMIN] = 1
		        new[6][TERMIOS.VTIME] = 0
		        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
		        c = None
		        try:
		                c = os.read(fd, 1)
		        finally:
		                termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
		        return c
		s = ""
		c = ""
		print "type something"
		while 1: 
			c = ""
			d = getkey()
			if d == "\n":
				break
			d = str(d)
			s = str(s+d)
			c = bin(int(binascii.hexlify(s), 16))
			c = c.replace("b","")
			c = str(c)
			print (c)
			sys.stdout.write("\033[F")
	elif "repeat" in question and "times" in question:
		if speak == 1:
			sptext = question.split(" ") 
			repeattext = " ".join(sptext[1:len(sptext)])
			repeattext = repeattext.rsplit(' ', 2)[0]
			sptext = question.split(" ") 
			repeattimes = question.split()[-2]
			repeattimes = int(repeattimes)
			checkrepeattimes = 0
			while repeattimes != checkrepeattimes:
				os.system("say "+repeattext)
				checkrepeattimes = (checkrepeattimes + 1)
		elif speak != 1:
			print ("Speech Must Be Toggled On First! This Can Be Done By Using The Command 'toggle_speech' ")
	elif question == "execute protocol 117":
		print ("John 117 activated!")
	elif "add new custom command" == question:
		file = open("customdictone.txt", "a")
		questioncmd = raw_input("> Enter custom command: ")
		tagcommand = raw_input("> Enter python script executed(use 'help' command to see needed syntax): ")
		leel = str(questioncmd+":"+tagcommand+"\n\n")
		file.write(leel)
		file.close()
	else:
		file = open("customdictone.txt", "r")
		linecheck = 0
		lines=file.readlines()
		num = sum(1 for line in open("customdictone.txt"))
		while num != linecheck:
			lol = lines[linecheck]
			word = lol.split(':', 1)[0]
			sptext = lol.split(":") 
			linecmd= ":".join(sptext[1:len(sptext)])
			if question == word:
				exec(linecmd)
				break
			elif question != word:
				linecheck = (linecheck + 1)
		print ("> Error 404: Command Not Found!")
