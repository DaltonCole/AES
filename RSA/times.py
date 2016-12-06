from AES import *
import os
import time

def aes128_ecb():
	key = 'abcdefghijklmnop'
	file = 'input128.txt'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('aesTimes_128_ECB.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1

				# Start time
				start_time = time.time()

				# Perform AES
				aes = AES(key)
				e = aes.encrypt(line)
				d = aes.decrypt(e)

				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average_aes128_ECB.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 128 bit key AES\'s performed using ECB: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')

def aes196_ecb():
	key = 'abcdefghijklmnopabcdefgh'
	file = 'input196.txt'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('aesTimes_196_ECB.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1

				# Start time
				start_time = time.time()

				# Perform AES
				aes = AES(key)
				e = aes.encrypt(line)
				d = aes.decrypt(e)

				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average_aes196_ECB.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 196 bit key AES\'s performed using ECB: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')

def aes256_ecb():
	key = 'abcdefghijklmnop'
	file = 'input256.txt'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('aesTimes_256_ECB.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1

				# Start time
				start_time = time.time()

				# Perform AES
				aes = AES(key)
				e = aes.encrypt(line)
				d = aes.decrypt(e)

				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average_aes256_ECB.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 256 bit key AES\'s performed using ECB: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')

def aes128_cbc():
	key = 'abcdefghijklmnop'
	file = 'input128.txt'
	IV = 'abcdefghijklmnop'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('aesTimes_128_CBC.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1

				# Start time
				start_time = time.time()

				# Perform AES
				aes = AES(key, IV)
				e = aes.encrypt(line, 'CBC')
				d = aes.decrypt(e, 'CBC')

				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average_aes128_CBC.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 128 bit key AES\'s performed using CBC: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')

def aes196_cbc():
	key = 'abcdefghijklmnopabcdefgh'
	file = 'input196.txt'
	IV = 'abcdefghijklmnop'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('aesTimes_196_CBC.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1

				# Start time
				start_time = time.time()

				# Perform AES
				aes = AES(key, IV)
				e = aes.encrypt(line, 'CBC')
				d = aes.decrypt(e, 'CBC')

				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average_aes196_CBC.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 196 bit key AES\'s performed using CBC: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')

def aes256_cbc():
	key = 'abcdefghijklmnop'
	file = 'input256.txt'
	IV = 'abcdefghijklmnop'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('aesTimes_256_CBC.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1

				# Start time
				start_time = time.time()

				# Perform AES
				aes = AES(key, IV)
				e = aes.encrypt(line, 'CBC')
				d = aes.decrypt(e, 'CBC')

				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average_aes256_CBC.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 256 bit key AES\'s performed using CBC: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')

def main():
	aes128_ecb()
	aes196_ecb()
	aes256_ecb()
	aes128_cbc()
	aes196_cbc()
	aes256_cbc()


if __name__ == "__main__":
	main()