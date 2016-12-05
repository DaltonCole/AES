from AES import * 
import os

def main():
	input_file = input("What file would you like to encrypt?: ")
	file = ''
	filename, file_extension = os.path.splitext(input_file)
	with open(input_file, 'rb') as f:
		file = f.read()

	mode = ""
	while mode != 'ECB' and mode != 'CBC':
		mode = input("Please enter a mode (ECB, CBC): ")
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
			iv = input("Please enter a 16 bit iv")
			if len(iv) != 16:
				print("Invalid IV size of: " + str(len(iv)))

	# AES
	aes = AES(key, iv)
	e = aes.encrypt(file, mode)	
	d = aes.decrypt(e, mode)


	# Save cipher and plain text to files
	with open('encryped.aes', 'wb') as f:
		f.write(e)
	with open('decrypted' + str(file_extension), 'wb') as f:
		f.write(d)

	print("Original equals decyrpted: ")
	print(d == file)

if __name__ == "__main__":
	main()