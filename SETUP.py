import platform
import os
from os.path import expanduser
osname = platform.system()
if "darwin" == osname or "Darwin" == osname:
	osid = ("OS X")
elif "Linux" == osname or "linux" == osname:
	osid = ("Linux")
elif "window" in osname or "Window" in osname:
	osid = ("Windows")
name = platform.node()
name = name.rstrip(".local")
f1 = open('CORBULO.py', 'r')
f2 = open('CORBULO1.py', 'w')
if "darwin" == osname or "Darwin" == osname or "Linux" == osname or "linux" == osname:
	for line in f1:
		f2.write(line.replace("os.system('clear')", "os.system('clear')"))
elif "windows" == osname or "Windows" == osname:
	for line in f1:
		f2.write(line.replace("os.system('clear')", "os.system('cls')"))
		f2.write(line.replace("speak = 1", "speak = 0"))
		f2.write(line.replace("print ('> Speach output is toggled on')", "print ('> Windows does not have this functionality..sorry')"))
elif "linux" == osname or "Linux" == osname:
	for line in f2:
		f2.write(line.replace('os.system("say "+names)', "os.system('echo '+names+'|espeak')"))
f1.close()
f2.close()
home = expanduser("~")
home = (home+"/CORBULO")
if not os.path.exists(home):
    os.makedirs(home)
source = "setupfolder/buzz.mp3"
destination = (home+"/buzz.mp3")
os.rename(source, destination)
source = "setupfolder/temp.txt"
destination = (home+"/temp.txt")
os.rename(source, destination)
source = "setupfolder/customdictone.txt"
destination = (home+"/customdictone.txt")
os.rename(source, destination)
print ("Setup Complete!")
