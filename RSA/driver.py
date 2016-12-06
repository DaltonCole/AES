import rsa
import os
import time

def RSA128():
	key_size = 128
	file = 'input128.txt'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('times128.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1
				# Start time
				start_time = time.time()

				# Perform RSA
				(bob_pub, bob_priv) = rsa.newkeys(key_size)
				e = rsa.encrypt(line, bob_pub)
				d = rsa.decrypt(e, bob_priv)
				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average128.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 128 bit key RSA\'s performed: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')

def RSA196():
	key_size = 196
	file = 'input196.txt'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('times196.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1
				# Start time
				start_time = time.time()

				# Perform RSA
				(bob_pub, bob_priv) = rsa.newkeys(key_size)
				e = rsa.encrypt(line, bob_pub)
				d = rsa.decrypt(e, bob_priv)
				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average196.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 196 bit key RSA\'s performed: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')

def RSA256():
	key_size = 256
	file = 'input256.txt'

	average_time = 0
	lines = 0

	with open(file, 'rb') as f:
		with open('times256.txt', 'w') as g:
			for line in f:
				line = line[:-1]
				lines += 1
				# Start time
				start_time = time.time()

				# Perform RSA
				(bob_pub, bob_priv) = rsa.newkeys(key_size)
				e = rsa.encrypt(line, bob_pub)
				d = rsa.decrypt(e, bob_priv)
				if d != line:
					print('FALSE: ' + str(line) + ' ' + str(d))

				time_difference = time.time() - start_time
				average_time += time_difference

				g.write(str(time_difference) + '\n')

	with open('average256.txt', 'w') as f:
		f.write('Total time: ' + str(average_time) + '\n')
		f.write('Number of 256 bit key RSA\'s performed: ' + str(lines) + '\n')
		f.write('Average Run time: ' + (str(average_time / lines)) + '\n')


def main():
	RSA128()
	RSA196()
	RSA256()

if __name__ == "__main__":
	main()