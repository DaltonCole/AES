import pyaes

key = b'abcdefghijklmnop'
iv = b'abcdefghijklmnop'

aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
plaintext = "TextMustBe16Byte"
ciphertext = aes.encrypt(plaintext)

# '\xd6:\x18\xe6\xb1\xb3\xc3\xdc\x87\xdf\xa7|\x08{k\xb6'
print (repr(ciphertext))


# The cipher-block chaining mode of operation maintains state, so 
# decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
decrypted = aes.decrypt(ciphertext)

# True
print (decrypted == plaintext)
print(decrypted)
print(plaintext)