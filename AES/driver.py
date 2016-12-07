from AES import * 
import os

def main():
	# Get user input
	eOrd = ''
	while eOrd != 'encrypt' and eOrd != 'decrypt':
		eOrd = input("Encrypt or Decrypt?: ")
		eOrd = eOrd.lower()
		if eOrd != 'encrypt' and eOrd != 'decrypt':
			print(eOrd + " is an invalid input.")

	input_file = input("What file would you like to " + str(eOrd) + '?: ')
	file = ''
	filename, file_extension = os.path.splitext(input_file)
	with open(input_file, 'rb') as f:
		file = f.read()

	mode = ""
	while mode != 'ECB' and mode != 'CBC':
		mode = input("Please enter a mode (ECB, CBC): ")
		mode = mode.upper()
		if mode != 'ECB' and mode != 'CBC':
			print("Invalid input")

	key = ""
	while len(key) != 16 and len(key) != 24 and len(key) != 32:
		key = input("Inputs a 16, 24, or 32 bit key: ")
		if len(key) != 16 and len(key) != 24 and len(key) != 32:
			print("Invalid key size of: " + str(len(key)))

	iv = None
	if mode == 'CBC':
		iv = ''
		while len(iv) != 16:
			iv = input("Please enter a 16 bit iv: ")
			if len(iv) != 16:
				print("Invalid IV size of: " + str(len(iv)))

	saveAs = input("What should the output file be called (with extension)?: ")

	# AES
	aes = AES(key, iv)

	enOrDecrypted = ''
	if eOrd == 'encrypt':
		enOrDecrypted = aes.encrypt(file, mode)	
	else:
		enOrDecrypted = aes.decrypt(file, mode)	

	# Save cipher or plain text to files
	with open(saveAs, 'wb') as f:
		f.write(enOrDecrypted)


if __name__ == "__main__":
	main()