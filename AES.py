
def string_to_bytes(text):
	return list(ord(c) for c in text)

def bytes_to_string(binary):
	return "".join(chr(b) for b in binary)

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

	def __init__(self, key, bit_size = 128):
		self.bit_size = bit_size
		self.key = string_to_bytes(key)

		self.Nb = 4			# Number of Columns

		if len(self.key) != 16 and len(self.key) != 24 and len(self.key) != 32:
			 raise ValueError('Invalid key size')

		if bit_size == 128:
			self.Nk = 4		# 4 32-bit words for key
			self.Nr = 10	# 10 rounds for 128 bit key size

	def encrypt(self, message):
		print(len(message))
		message = string_to_bytes(message)
		print(len(message))
		print(type(message))
		print(message)

		w = self.KeyExpansion()
		message = self.pad(message)
		print(len(message))
		print(message)

		cipher_text = ''
		for bits_128 in range(0, len(message), 16):			
			cipher_text += bytes_to_string(self.cipher(message[bits_128: (bits_128 + 16)], w))

		return cipher_text


	def decrypt(self, cipher_text):
		cipher_text = string_to_bytes(cipher_text)

		w = self.KeyExpansion()

		plain_text = ''
		for bits_128 in range(0, len(cipher_text), 16):
			plain_text += bytes_to_string(self.plain(cipher_text[bits_128: (bits_128 + 16)], w)) 

		plain_text = self.unpad(plain_text)

		return plain_text

	# Padding is implemented using RKCS#7 as described in this post:
	# https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7
	def pad(self, message):
		extra = 16 - (len(message) % 16)
		if extra == 0:
			# If message is a multiple of 128 bits, pad with a block of f to indicate padding
			message += [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		elif extra == 1:
			# Padd with the padding value
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
		extra = message[-1]
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
		w = []
		for i in range(self.Nk):
			w.append([self.key[4 * i], self.key[4 * i + 1], self.key[4 * i + 2], self.key[4 * i + 3]])

		for i in range(self.Nk, self.Nb * (self.Nr + 1)):
			temp = w[i-1]

			if i % self.Nk == 0:
				temp = self.SubWord(self.RotWord(temp))
				temp[0] = temp[0] ^ self.Rcon[i // self.Nk - 1]
			elif self.Nk > 6 and i % self.Nk == 4:
				temp = SubWord()

			w.append([0, 0, 0, 0])
			for row in range(4):
				w[i][row] = w[i - self.Nk][row] ^ temp[row]

		all_words = []

		for i in w:
			for j in i:
				all_words.append(j)

		return all_words

	def SubWord(self, word):
		post_s = []
		for b in word:
			post_s.append(self.S[b >> 4][b & 0x0F])

		return post_s

	def RotWord(self, word):
		return word[1:] + word[:1]


	def cipher(self, message, w):
		state = []
		for row in range(4):
			state.append([])

		for i in range(len(message)):
			state[i % 4].append(message[i])
				
		state = self.AddRoundKey(state, self.make_2d_list(w, 0, 4 * self.Nb))

		for rounds in range(self.Nr - 1):
			state = self.SubBytes(state)
			state = self.ShiftRows(state)
			state = self.MixColumns(state)
			state = self.AddRoundKey(state, self.make_2d_list(w, 4 * (rounds + 1) * self.Nb, 4 * (rounds + 2) * (self.Nb)))

		state = self.SubBytes(state)
		state = self.ShiftRows(state)
		state = self.AddRoundKey(state, self.make_2d_list(w, 4 * self.Nr * self.Nb, 4 * (self.Nr + 1) * (self.Nb)))

		self.print(state)

		cipher_text = []

		for column in range(self.Nb):
			for row in range(4):
				cipher_text.append(state[row][column])

		return cipher_text

	def plain(self, message, w):
		state = []
		for row in range(4):
			state.append([])

		for i in range(len(message)):
			state[i % 4].append(message[i])

		state = self.AddRoundKey(state, self.make_2d_list(w, 4 * self.Nr * self.Nb, 4 * (self.Nr + 1) * (self.Nb)))

		for rounds in range(self.Nr - 1, 0, -1): # Goes from Nr - 1 to 1
			state = self.InvShiftRows(state)
			state = self.InvSubBytes(state)
			state = self.AddRoundKey(state, self.make_2d_list(w, 4 * (rounds) * self.Nb, 4 * (rounds + 1) * (self.Nb)))
			state = self.InvMixColumns(state)


		state = self.InvShiftRows(state)
		state = self.InvSubBytes(state)
		state = self.AddRoundKey(state, self.make_2d_list(w, 0, 4 * self.Nb))

		print()
		self.print(state)

		plain_text = []

		for column in range(self.Nb):
			for row in range(4):
				plain_text.append(state[row][column])

		return plain_text


	def print(self, state):
		print()
		for row in range(4):
			for column in range(self.Nb):
				print(hex(state[row][column]), end='\t')
			print()

	def make_2d_list(self, w, start, end):
		d2 = []
		for row in range(4):
			d2.append([])

		for i in range(end - start):
			d2[i % 4].append(w[start + i])

		return d2

	def AddRoundKey(self, state, w):
		for row in range(4):
			for column in range(self.Nb):
				state[row][column] = int(hex(state[row][column] ^ w[row][column]), 16)
		return state

	def SubBytes(self, state):
		b = []

		for row in range(4):
			b.append([])

		for column in range(self.Nb):
			for row in range(4):
				b[row % 4].append(self.S[(state[row][column] >> 4) % 16][(state[row][column] & 0x0F)])

		return b

	def InvSubBytes(self, state):
		b = []

		for row in range(4):
			b.append([])

		for column in range(self.Nb):
			for row in range(4):
				b[row % 4].append(self.Si[(state[row][column] >> 4) % 16][(state[row][column] & 0x0F)])

		return b

	def ShiftRows(self, state):
		# Second row
		state[1] = state[1][1:] + state[1][:1]
		# Third row
		state[2] = state[2][2:] + state[2][:2]
		# Fourth row
		state[3] = state[3][3:] + state[3][:3]

		return state

	def InvShiftRows(self, state):
		# Second row
		state[1] = state[1][3:] + state[1][:3]
		# Third row
		state[2] = state[2][2:] + state[2][:2]
		# Forth row
		state[3] = state[3][1:] + state[3][:1]

		return state

	def MixColumns(self, state):
		s = []
		for row in range(4):
			s.append([])

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
		s = []
		for row in range(4):
			s.append([])

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
		if(h > 127):
			return ((h << 1) % 256) ^ int('00011011', 2)
		return (h << 1)

	def xtime_0e(self, h): 	# 0e = 08 + 04 + 02
		h_02 = self.xtime(h)
		h_04 = self.xtime(h_02)
		h_08 = self.xtime(h_04)

		return h_02 ^ h_04 ^ h_08

	def xtime_0b(self, h):	# 0b = 08 + 02 + 01
		h_02 = self.xtime(h)
		h_04 = self.xtime(h_02)
		h_08 = self.xtime(h_04)

		return h ^ h_02 ^ h_08

	def xtime_0d(self, h):	# 0d = 08 + 04 + 01
		h_02 = self.xtime(h)
		h_04 = self.xtime(h_02)
		h_08 = self.xtime(h_04)

		return h ^ h_04 ^ h_08

	def xtime_09(self, h):	# 09 = 08 + 01
		h_02 = self.xtime(h)
		h_04 = self.xtime(h_02)
		h_08 = self.xtime(h_04)

		return h ^ h_08












