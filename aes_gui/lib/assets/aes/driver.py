from AES import * 
import os
import sys

"""Argumetns:
	1. Encrypt or Decrypt
	2. file
	3. mode
	4. key
	5. iv
"""
eOrD = sys.argv[1]
file_name = sys.argv[2]
mode = sys.argv[3]
key  = sys.argv[4]

iv = None
if len(sys.argv) == 6:
	iv = sys.argv[5]

file = ''
with open('public/uploads/' + str(file_name), 'rb') as f:

	file = f.read()

# AES
aes = AES(key, iv)

final_file = ''
if eOrD == "Encrypt":
	final_file = aes.encrypt(file, mode)
else:
	final_file = aes.decrypt(file, mode)

with open('public/uploads/' + str(file_name), 'wb') as f:
	f.write(final_file)
