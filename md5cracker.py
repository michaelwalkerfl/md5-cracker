#-*- coding:utf-8 -*-
import hashlib

h = raw_input("Hash: ")
oku = open('wordlist.txt').readlines()


for kelime in oku:
	kelime = kelime.strip()
	ha = hashlib.md5(kelime).hexdigest()
	
	if ha == h:
		print "Bulundu: " + kelime
		break




