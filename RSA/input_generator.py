import random

alphaNumberic = '0123456789abcdefghijklmnopqrstuvwxyz'

max_128 = len('messa')

with open('input128.txt', 'w') as f:
	for i in range(1000):
		s = ''
		for i in range(max_128):
			s += random.choice(alphaNumberic)
		f.write(s + '\n')

max_196 = len('messagemessage')

with open('input196.txt', 'w') as f:
	for i in range(1000):
		s = ''
		for i in range(max_196):
			s += random.choice(alphaNumberic)
		f.write(s + '\n')

max_256 = len('messagemessagemessage')

with open('input256.txt', 'w') as f:
	for i in range(1000):
		s = ''
		for i in range(max_256):
			s += random.choice(alphaNumberic)
		f.write(s + '\n')