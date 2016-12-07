# AES

AES applies AES encryption on a given byte string

# Input

* File to encrypt using AES
* Mode to encrypt with
  * ECB
  * CBC
* Key
* IV if using CBC mode

## Example

```
encrypt
a.png
cbc
abcdefghijklmnopabcdefghijklmnop
abcdefghijklmnop
encrypted.png
```

# Output

* File containing the encrypted or decrypted file
