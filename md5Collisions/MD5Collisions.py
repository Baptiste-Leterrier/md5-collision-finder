import hashlib
import string
import random
import time
import psutil
import os
import sys
import argparse
__author__ = 'Shepah'

start = time.time()

stringLength = 17
hashLength = 8
maxRam = 89
maxCollisionNum = 3

parser = argparse.ArgumentParser(description='MD5 - Collision Finder')
parser.add_argument('-s','--stringL', help='String Length to Hash',required=True)
parser.add_argument('-t','--hashL',help='Hash length to test', required=True)
parser.add_argument('-r','--maxRam', help='Max RAM to use for this program',required=True)
parser.add_argument('-c','--maxColl',help='Number of collision to find before stopping', required=True)
args = parser.parse_args()

stringLength = int(args.stringL)
hashLength = int(args.hashL)
maxRam = int(args.maxRam)
maxCollisionNum = int(args.maxColl)

def showInfo():
	print "/////////"
	print "MD5 collision finder"
	print "created by Shepah"
	print "Licence: GPL GNU (i don't give a shit)"
	print "///////// \n"

	print "Parameters: \n -Length of string used for random generation: "+ str(stringLength) + " \n -Length of hash analyzed for collision: "+ str(hashLength) + " \n -Max RAM used before auto stop: "+ str(maxRam) +"% \n -The program will find "+ str(maxCollisionNum)+ " collisions before stopping \n -The program will prompt a message every 100000 tests \n \n"

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

def stringGenerator(chars=string.ascii_uppercase):
	chaine = ''
	for i in range(1,stringLength): 	
		chaine += random.choice(chars)
	return chaine

def setAndHashString(value ,chars=string.ascii_uppercase):
	chaine = ''
	for i in range(1,stringLength):	
		chaine += random.choice(chars)
	chaine = ' '.join(format(ord(x), 'b') for x in chaine)
	chaine = hashlib.md5(chaine).hexdigest()
	chaine = chaine[:hashLength]
	return chaine

def controlOrStore(key, value):
	global hashmap
	if key in hashmap and hashmap.get(key) != value:
		global collisionFound
		collisionFound.update({hashmap.get(key) : value})
		print "*****COLLISION FOUND*****"
		print "Hash 1: "+ key +" with value " + value
		print "Hash 2: "+ key +" with value " + hashmap.get(key)
		print "Using "+ str(hashLength) + " caracters long hash in "+ str(time.time() - start) + " seconds"
		print "************************* \n"
		return True
	else:
		hashmap.update({key : value})
		return False
cls()
showInfo()
print "Running"
collisionNum = 1
testNum = 0
hashmap = {'import': 'trade'}
collisionFound = {'': ''}
hashmap.clear()
while collisionNum <= maxCollisionNum:
	variab = psutil.phymem_usage()
	variab = str(variab)
	variab = variab[55:57]
	variab = int(variab)
	testNum += 1	
	if testNum % 100000 == 0:
		print "-----------------------------------------------"
		print str(testNum) + " values tested in " + str(time.time() - start) + " seconds"
		print "RAM used: " + str(variab) +"%"
		print str(collisionNum - 1) + " collisions found !"
		print str(len(hashmap)) + " entries in hashmap"
		print "----------------------------------------------- \n"
	a = stringGenerator()
	b = stringGenerator()
	hasha = setAndHashString(a)
	hashb = setAndHashString(b)
	if controlOrStore(hasha, a) or controlOrStore(hashb, b):
		collisionNum += 1
	if variab > maxRam:
		print "Stopping. Too much RAM used"
		break
	 	
end = time.time()
total = end - start
print "Stopping"
print "List of collisions found: \n" + str(collisionFound.items())
print "Execution time: " + str(total)
