from AES import * 
import os
import sys

"""Inputs:
	1. Encrypt or Decrypt
	2. file
	3. mode
	4. key
	5 (optional). iv
"""
eOrD = input()
file_name = input()
mode = input()
key  = input()


iv = None
if mode == 'CBC':
	iv = input()

print(eOrD)
print(file_name)
print(mode)
print(key)
print(iv)

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
