def string_to_bytes(text):
	if isinstance(text, bytes):
		#return text
		b = bytearray()
		for i in text:
			b.append(i)
		l = []
		for i in b:
			l.append((i))
		return l
	return [ord(c) for c in text]

# In Python 3, we return bytes
def bytes_to_string(binary):
	return bytes(binary)

class AES:
	# S-box
	S = [ 	[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
			[0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
			[0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
			[0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
			[0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
			[0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
			[0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
			[0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
			[0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
			[0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
			[0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
			[0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
			[0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
			[0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
			[0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
			[0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

	# S-box inverse
	Si = [	[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
			[0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
			[0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
			[0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
			[0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
			[0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
			[0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
			[0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
			[0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
			[0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
			[0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
			[0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
			[0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
			[0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
			[0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
			[0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

	# Round constant words
	Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91]

	def __init__(self, key,  iv = None):
		"""Constructor for AES

		Sets:
			bit_size	=	Number of bytes in key
			key 		=	key paramater
			iv 			= 	iv paramater
			Nb 			=	Number of columns
			Nk 			=	Number of 32 bit words, 4 for 128 bit key, 6 for 196, 8 for 256
			Nr 			=	Number of rounds, 10 for 128 bit key, 12 for 196, 14 for 256

			:param str key: encryption key

			:param str iv: initialization vector

			Errors:
				*	If iv is not 128 bits, ValueError is raised
				*	If key is not 128, 196, nor 256 bits, ValueError is raised

			:return None
		"""
		# Number of bytes in key
		self.bit_size = len(key)
		# Change key to a list of bytes
		self.key = string_to_bytes(key)

		# Set iv is one is provided
		if iv is not None:
			self.iv = string_to_bytes(iv)
			# If iv is not 128 bits, raise error
			if len(iv) != 16:
				raise ValueError('Invalid IV size')

		# Number of Columns
		self.Nb = 4			

		# If key is not 128 bits, 196, nor 256, raise error
		if len(self.key) != 16 and len(self.key) != 24 and len(self.key) != 32:
			 raise ValueError('Invalid key size')

		if self.bit_size == 16:		# 128 bit
			self.Nk = 4					# 4 32-bit words for Cipher Key
			self.Nr = 10				# 10 rounds
		elif self.bit_size == 24:	# 196 bit
			self.Nk = 6					# 6 32-bit words for Cipher Key
			self.Nr = 12				# 12 rounds
		elif self.bit_size == 32:	# 256 bit
			self.Nk = 8					# 8 32-bit words for Cipher Key
			self.Nr = 14				# 14 rounds

	def encrypt(self, message, mode='ECB'):
		"""Encrypts the plain text from message

		:param byte string message: Message to be encrypted

		:param string mode:	Mode to encrypt message in 
			Mode is either:
				* 'ECB' = Electronic Code Book
				* 'CBC' = Cipher Block Chaining

		:return: Cipher text after AES encryption in the specified mode

		:rtype: Byte string
		"""
		# Convert message to a list of bytes
		message = string_to_bytes(message)

		# Expand the key
		w = self.KeyExpansion()

		# Pad message using RKCS#7
		message = self.pad(message)

		# Initialize cipher_text
		cipher_text = bytes()

		# Increment over every 128 bits in message
		for bits_128 in range(0, len(message), 16):	
			# If CBC mode
			if mode == 'CBC':
				# XOR message with IV first round
				if bits_128 == 0:
					for i in range(16):
						message[i] = message[i] ^ self.iv[i]
				else:
					# XOR with message with preious cipher block
					for i in range(16):
						message[bits_128 + i] = message[bits_128 + i] ^ cipher_block[i]
				# Encrypt
				cipher_block = self.cipher(message[bits_128: (bits_128 + 16)], w)
				cipher_text += bytes_to_string(cipher_block)
			# ECB mode
			elif mode == 'ECB':	
				# Encrypt	
				cipher_text += bytes_to_string(self.cipher(message[bits_128: (bits_128 + 16)], w))

		return cipher_text


	def decrypt(self, cipher_text, mode='ECB'):
		"""Decrypts the cipher_text into plain text

		:param byte string cipher_text: cipher text to be converted to plain text

		:param string mode:	Mode to encrypt message in 
			Mode is either:
				* 'ECB' = Electronic Code Book
				* 'CBC' = Cipher Block Chaining

		:return: Plaintext

		:rtype: Byte string
		"""
		# Convert cipher_text into a list of bytes
		cipher_text = string_to_bytes(cipher_text)

		# Expand the key
		w = self.KeyExpansion()

		# Initialize plain text
		plain_text = bytes()
		# Increment over every 128 bits in message
		for bits_128 in range(0, len(cipher_text), 16):
			# If CBC mode
			if mode == 'CBC':
				# Decrypt
				plain_block = self.plain(cipher_text[bits_128: (bits_128 + 16)], w)
				# XOR plain block with iv for first round
				if bits_128 == 0:
					for i in range(16):
						plain_block[i] = plain_block[i] ^ self.iv[i]
				else:
					# XOR plain block with previous cipher block
					for i in range(16):
						plain_block[i] = plain_block[i] ^ cipher_text[bits_128 - 16 + i]
				# Add block to plain text
				plain_text += bytes_to_string(plain_block)
			else:
				plain_text += bytes_to_string(self.plain(cipher_text[bits_128: (bits_128 + 16)], w)) 

		# Unpad plain text using RKCS#7
		plain_text = self.unpad(plain_text)

		return plain_text

	# Padding is implemented using RKCS#7 as described in this post:
	# https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7
	def pad(self, message):
		"""Pad the message such that it is a multiple of 128 bits

		Padding is implemented using RKCS#7 as described here:
		https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7

		:param string message: Message to be padded

		:return: Padded message

		:rtype: list of bytes
		"""
		# Find the amound of padding that is needed
		extra = 16 - (len(message) % 16)

		# Pad the end of the message such that the value of the padding equals the amound of padding
		if extra == 0:
			# If message is a multiple of 128 bits, pad with a block of 0 to indicate padding
			message += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		elif extra == 1:
			# Pad with the padding value
			message += [1]
		elif extra == 2:
			message += [2, 2]
		elif extra == 3:
			message += [3, 3, 3]
		elif extra == 4:
			message += [4, 4, 4, 4]
		elif extra == 5:
			message += [5, 5, 5, 5, 5]
		elif extra == 6:
			message += [6, 6, 6, 6, 6, 6]
		elif extra == 7:
			message += [7, 7, 7, 7, 7, 7, 7]
		elif extra == 8:
			message += [8, 8, 8, 8, 8, 8, 8, 8]
		elif extra == 9:
			message += [9, 9, 9, 9, 9, 9, 9, 9, 9]
		elif extra == 10:
			message += [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
		elif extra == 11:
			message += [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
		elif extra == 12:
			message += [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
		elif extra == 13:
			message += [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
		elif extra == 14:
			message += [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
		elif extra == 15:
			message += [15 ,15, 15 ,15, 15 ,15, 15 ,15, 15 ,15, 15 ,15, 15 ,15, 15]
		return message

	def unpad(self, message):
		"""Unpad the message such that it is the size of the original message

		Padding is implemented using RKCS#7 as described here:
		https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7

		:param string message: Message to be unpadded

		:return: Unpadded message

		:rtype: list of bytes
		"""
		# Find the amound of padding that is needed to be removed
		extra = message[-1]

		# Remove the padding
		if extra == 1:
			message = message[:-1]
		elif extra == 2:
			message = message[:-2]
		elif extra == 3:
			message = message[:-3]
		elif extra == 4:
			message = message[:-4]
		elif extra == 5:
			message = message[:-5]
		elif extra == 6:
			message = message[:-6]
		elif extra == 7:
			message = message[:-7]
		elif extra == 8:
			message = message[:-8]
		elif extra == 9:
			message = message[:-9]
		elif extra == 10:
			message = message[:-10]
		elif extra == 11:
			message = message[:-11]
		elif extra == 12:
			message = message[:-12]
		elif extra == 13:
			message = message[:-13]
		elif extra == 14:
			message = message[:-14]
		elif extra == 15:
			message = message[:-15]
		elif extra == 0:
			message = message[:-16]
		return message
		

	def KeyExpansion(self):
		"""Expand the key according to AES standards

		:return: The expanded key

		:rtype: List of bytes
		"""
		# Initialize the word list
		w = []

		# Set the first word to the first four key bytes
		for i in range(self.Nk):
			w.append([self.key[4 * i], self.key[4 * i + 1], self.key[4 * i + 2], self.key[4 * i + 3]])

		# Fill w so there will be a new word list for every round
		for i in range(self.Nk, self.Nb * (self.Nr + 1)):
			# Set temp to previous word
			temp = w[i-1]

			# Every Nk rounds
			if i % self.Nk == 0:
				# Mix up temp
				temp = self.SubWord(self.RotWord(temp))
				temp[0] = temp[0] ^ self.Rcon[i // self.Nk - 1]
			# When key size is 256 bit and  i - 4 is a multiple of Nk
			elif self.Nk > 6 and i % self.Nk == 4:	
				temp = self.SubWord(temp)

			# XOR current word with the Nk preivous word
			w.append([0, 0, 0, 0])
			for row in range(4):
				w[i][row] = w[i - self.Nk][row] ^ temp[row]

		# Convert word to a list of bytes
		all_words = []
		for i in w:
			for j in i:
				all_words.append(j)

		return all_words

	def SubWord(self, word):
		"""Uses the S-box on the extended key algorithm

		:param list of bytes word: Word to apply s-box on

		:return: Word after applying s-box to it

		:rtype: List of bytes
		"""
		# Initialize word
		post_s = []
		for b in word:
			# For each word, apply s-box
			post_s.append(self.S[b >> 4][b & 0x0F])

		return post_s

	def RotWord(self, word):
		"""Rotate word such that [a0, a1, a2, a3] = [a1, a2, a3, a0]

		:param list of bytes word: Word to rotate

		:return: Rotated word

		:rtype: List of bytes
		"""
		# Rotate word such that a0 is not at the end
		return word[1:] + word[:1]


	def cipher(self, message, w):
		"""Cipher to encode a single block with

		:param lists of bytes message: Message to encode

		:param list of bytes w: Extended key to encrypt with

		:return: Encrypted message block

		:rtype: List of bytes
		"""
		# Initialize byte matrix to message
		state = []
		for row in range(4):
			state.append([])

		for i in range(len(message)):
			state[i % 4].append(message[i])
				
		# Apply round key to state
		state = self.AddRoundKey(state, self.make_2d_list(w, 0, 4 * self.Nb))

		# For Nr - 1 rounds
		for rounds in range(self.Nr - 1):
			# SubBytes
			state = self.SubBytes(state)
			# ShiftRows
			state = self.ShiftRows(state)
			# MixColumns
			state = self.MixColumns(state)
			# AddRoundKey, tranform part of w into a matrix
			state = self.AddRoundKey(state, self.make_2d_list(w, 4 * (rounds + 1) * self.Nb, 4 * (rounds + 2) * (self.Nb)))

		# For last round, do not do mix columns
		state = self.SubBytes(state)
		state = self.ShiftRows(state)
		state = self.AddRoundKey(state, self.make_2d_list(w, 4 * self.Nr * self.Nb, 4 * (self.Nr + 1) * (self.Nb)))

		# Initialize cipher text
		cipher_text = []
		# Turn state into a list of bytes
		for column in range(self.Nb):
			for row in range(4):
				cipher_text.append(state[row][column])

		return cipher_text

	def plain(self, message, w):
		"""Decode an encoded cipher block

		:param lists of bytes message: Message to decode

		:param list of bytes w: Extended key to decrypt with

		:return: Decrypted message block

		:rtype: List of bytes
		"""
		# Initialize byte matrix to message
		state = []
		for row in range(4):
			state.append([])

		for i in range(len(message)):
			state[i % 4].append(message[i])

		# Apply round key
		state = self.AddRoundKey(state, self.make_2d_list(w, 4 * self.Nr * self.Nb, 4 * (self.Nr + 1) * (self.Nb)))

		# For Nr - 1 rounds
		for rounds in range(self.Nr - 1, 0, -1): # Goes from Nr - 1 to 1
			# Inverse ShiftRows
			state = self.InvShiftRows(state)
			# Inverse SubBytes
			state = self.InvSubBytes(state)
			# AddRoundKey, tranform part of w into a matrix
			state = self.AddRoundKey(state, self.make_2d_list(w, 4 * (rounds) * self.Nb, 4 * (rounds + 1) * (self.Nb)))
			# Inverse MixColumns
			state = self.InvMixColumns(state)

		# Do not inverse columns last round
		state = self.InvShiftRows(state)
		state = self.InvSubBytes(state)
		state = self.AddRoundKey(state, self.make_2d_list(w, 0, 4 * self.Nb))

		# Initialize plain text
		plain_text = []
		# Transform state into a list of bytes
		for column in range(self.Nb):
			for row in range(4):
				plain_text.append(state[row][column])

		return plain_text

	def print(self, state):
		"""Prints a matrix

		:param list of lists of bytes state: Matrix to print

		:return: None
		"""
		print()
		for row in range(4):
			for column in range(self.Nb):
				print(hex(state[row][column]), end='\t')
			print()

	def make_2d_list(self, w, start, end):
		"""Makes a matrix from w

		:param list of bytes w: Extended key to make a matrix from

		:param int start: Starting index in w for matrix

		:param int end: Ending index in w for matrix
			End should be s + 16

		:return: Matrix made from w[start] to w[end]

		:rtype: List of list of bytes
		"""
		d2 = []
		for row in range(4):
			d2.append([])

		for i in range(end - start):
			d2[i % 4].append(w[start + i])

		return d2

	def AddRoundKey(self, state, w):
		"""AddRoundKey as specified in AES. XORs state with coresponding w

		:param list of list of bytes state: Matrix to XOR with w

		:param list of list of bytes w: Matrix to XOR with state

		:return: Matrix = state[i][j] ^ w[i][j]

		:rtype: List of list of bytes
		"""
		for row in range(4):
			for column in range(self.Nb):
				state[row][column] = int(hex(state[row][column] ^ w[row][column]), 16)
		return state

	def SubBytes(self, state):
		"""SubBytes as specified in AES. Subsitutes byte with corresponding value in S-table

		:param list of list of bytes state: State matrix

		:return: Matrix after applying SubBytes to it

		:rtype: List of list of bytes
		"""
		# Initalize matrix
		b = []
		for row in range(4):
			b.append([])

		# For each element in matrix
		for column in range(self.Nb):
			for row in range(4):
				# Subsitutes byte with corresponding value in S-table
				b[row % 4].append(self.S[(state[row][column] >> 4) % 16][(state[row][column] & 0x0F)])

		return b

	def InvSubBytes(self, state):
		"""InvSubBytes as specified in AES. Subsitutes byte with corresponding value in Si-table

		:param list of list of bytes state: State matrix

		:return: Matrix after applying InvSubBytes to it

		:rtype: List of list of bytes
		"""
		# Initalize matrix
		b = []
		for row in range(4):
			b.append([])

		# For each element in matrix
		for column in range(self.Nb):
			for row in range(4):
				# Subsitute byte with corresponding value in Si-table
				b[row % 4].append(self.Si[(state[row][column] >> 4) % 16][(state[row][column] & 0x0F)])

		return b

	def ShiftRows(self, state):
		"""ShiftRows as specified in AES. 
			Shifts row1 left by 1
			Shifts row2 left by 2
			Shifts row3 left by 3

		:param list of list of bytes state: State matrix

		:return: Matrix after applying ShiftRows to it

		:rtype: List of list of bytes
		"""
		# Second row
		state[1] = state[1][1:] + state[1][:1]
		# Third row
		state[2] = state[2][2:] + state[2][:2]
		# Fourth row
		state[3] = state[3][3:] + state[3][:3]

		return state

	def InvShiftRows(self, state):
		"""ShiftRows as specified in AES. 
			Shifts row1 right by 1
			Shifts row2 right by 2
			Shifts row3 right by 3

		:param list of list of bytes state: State matrix

		:return: Matrix after applying InvShiftRows to it

		:rtype: List of list of bytes
		"""
		# Second row
		state[1] = state[1][3:] + state[1][:3]
		# Third row
		state[2] = state[2][2:] + state[2][:2]
		# Forth row
		state[3] = state[3][1:] + state[3][:1]

		return state

	def MixColumns(self, state):
		"""MixColumns as specified in AES. 
			s[0][c] = ({02} * s[0][c]) ^ ({03} * s[1][c]) ^ s[2][c] ^ s[3][c]
			s[1][c] = s[0][c] ^ ({02} * s[1][c]) ^ ({03} * s[2][c]) ^ s[3][c]
			s[2][c] = s[0][c] ^ s[1][c] ^ ({02} * s[2][c]) ^ ({03} * s[3][c])
			s[3][c] = ({03} * s[0][c]) ^ s[1][c] ^ s[2][c] ^ ({02} * s[3][c])

		:param list of list of bytes state: State matrix

		:return: Matrix after applying MixColumns to it

		:rtype: List of list of bytes
		"""
		# Initalize matrix
		s = []
		for row in range(4):
			s.append([])

		# For each columns
		for c in range(self.Nb): # c = column
			# s'[0][c]
			s_00 = self.xtime(state[0][c])
			s_01 = self.xtime(state[1][c]) ^ state[1][c]
			s[0].append(s_00 ^ s_01 ^ state[2][c] ^ state[3][c])
			
			# s'[1][c]
			s_11 = self.xtime(state[1][c])
			s_12 = self.xtime(state[2][c]) ^ state[2][c]
			s[1].append(state[0][c] ^ s_11 ^ s_12 ^ state[3][c])

			# s'[2][c]
			s_22 = self.xtime(state[2][c])
			s_23 = self.xtime(state[3][c]) ^ state[3][c]
			s[2].append(state[0][c] ^ state[1][c] ^ s_22 ^ s_23)

			# s'[3][c]
			s_33 = self.xtime(state[3][c])
			s_30 = self.xtime(state[0][c]) ^ state[0][c]
			s[3].append(s_30 ^ state[1][c] ^ state[2][c] ^ s_33)

		return s

	def InvMixColumns(self, state):
		"""MixColumns as specified in AES. 
			s[0][c] = ({0e} * s[0][c]) ^ ({0b} * s[1][c]) ^ ({0d} * s[2][c]) ^ ({09} * s[3][c])
			s[1][c] = ({09} * s[0][c]) ^ ({0e} * s[1][c]) ^ ({0b} * s[2][c]) ^ ({0d} * s[3][c])
			s[2][c] = ({0d} * s[0][c]) ^ ({09} * s[1][c]) ^ ({0e} * s[2][c]) ^ ({0b} * s[3][c])
			s[3][c] = ({0b} * s[0][c]) ^ ({0d} * s[1][c]) ^ ({09} * s[2][c]) ^ ({0e} * s[3][c])

		:param list of list of bytes state: State matrix

		:return: Matrix after applying InvMixColumns to it

		:rtype: List of list of bytes
		"""
		# Initalize matrix
		s = []
		for row in range(4):
			s.append([])

		# For each columns
		for c in range(self.Nb): # c = column
			# s'[0][c] = ({0e} * s[0][c]) ^ ({0b} * s[1][c]) ^ ({0d} * s[2][c]) ^ ({09} * s[3][c])
			s[0].append(self.xtime_0e(state[0][c]) ^ self.xtime_0b(state[1][c]) ^ self.xtime_0d(state[2][c]) ^ self.xtime_09(state[3][c]))

			# s'[1][c] = ({09} * s[0][c]) ^ ({0e} * s[1][c]) ^ ({0b} * s[2][c]) ^ ({0d} * s[3][c])
			s[1].append(self.xtime_09(state[0][c]) ^ self.xtime_0e(state[1][c]) ^ self.xtime_0b(state[2][c]) ^ self.xtime_0d(state[3][c]))

			# s'[2][c] = ({0d} * s[0][c]) ^ ({09} * s[1][c]) ^ ({0e} * s[2][c]) ^ ({0b} * s[3][c])
			s[2].append(self.xtime_0d(state[0][c]) ^ self.xtime_09(state[1][c]) ^ self.xtime_0e(state[2][c]) ^ self.xtime_0b(state[3][c]))

			# s'[3][c] = ({0b} * s[0][c]) ^ ({0d} * s[1][c]) ^ ({09} * s[2][c]) ^ ({0e} * s[3][c])
			s[3].append(self.xtime_0b(state[0][c]) ^ self.xtime_0d(state[1][c]) ^ self.xtime_09(state[2][c]) ^ self.xtime_0e(state[3][c]))

		return s

	def xtime(self, h):
		"""Applies xtime to the given byte
			Multiplies polynomial modulo an irreducible polynomial m(x)
				m(x) = x^8 + x^4 + x^3 + x + 1

		:param byte h: Byte to be multiplied by 2

		:return: h polynomial multiplied by 2 mod m(x)
		
		:rtype: Byte
		"""
		# If is > 127
		if(h > 127):
			# Left shift and apply a conditional bitwise XOR with {1b}
			return ((h << 1) % 256) ^ int('00011011', 2)
		# Left shift by 1
		return (h << 1)

	def xtime_0e(self, h): 
		"""Applies xtime until h * {0e} is achived
			0e = 08 + 04 + 02

		:param byte h: Byte to be multiplied by {0e}

		:rtype: Byte
		"""
		h_02 = self.xtime(h)
		h_04 = self.xtime(h_02)
		h_08 = self.xtime(h_04)

		return h_02 ^ h_04 ^ h_08

	def xtime_0b(self, h):
		"""Applies xtime until h * {0b} is achived
			0b = 08 + 02 + 01

		:param byte h: Byte to be multiplied by {0b}

		:rtype: Byte
		"""
		h_02 = self.xtime(h)
		h_04 = self.xtime(h_02)
		h_08 = self.xtime(h_04)

		return h ^ h_02 ^ h_08

	def xtime_0d(self, h):
		"""Applies xtime until h * {0d} is achived
			0d = 08 + 04 + 01

		:param byte h: Byte to be multiplied by {0d}

		:rtype: Byte
		"""
		h_02 = self.xtime(h)
		h_04 = self.xtime(h_02)
		h_08 = self.xtime(h_04)

		return h ^ h_04 ^ h_08

	def xtime_09(self, h):
		"""Applies xtime until h * {09} is achived
			09 = 08 + 01

		:param byte h: Byte to be multiplied by {09}

		:rtype: Byte
		"""
		h_02 = self.xtime(h)
		h_04 = self.xtime(h_02)
		h_08 = self.xtime(h_04)

		return h ^ h_08