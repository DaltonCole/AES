from AES import * 
import codecs


def main():
	input_file = 'button.mp3'
	key = 'abcdefghijklmnopabcdefgh'
	iv = 'abcdefghijklmnop'

	print(len(key))

	file = ''
	with open(input_file, 'rb') as f:
		file = f.read()

	# AES
	aes = AES(key, iv)
	e = aes.encrypt(file, 'CBC')	

	d = aes.decrypt(e, 'CBC')

	with open(str(input_file) + '.aes', 'wb') as f:
		f.write(e)

	with open('decrypted.mp3', 'wb') as f:
		f.write(d)

	print(d == file)

if __name__ == "__main__":
	main()