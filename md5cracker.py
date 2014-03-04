#-*- coding:utf-8 -*-
import hashlib

print """
Ahmet KOTAN
Md5 Hash Cracker
"""


h = raw_input("Hash: ")
oku = open('wordlist.txt').readlines()


for kelime in oku:
	kelime = kelime.strip()
	ha = hashlib.md5(kelime).hexdigest()
	
	if ha == h:
		print "Bulundu: " + kelime
		break




