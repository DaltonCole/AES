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
button.mp3
CBC
abcdefghijklmnopabcdefghijklmnop
abcdefghijklmnop
```

# Output

* File containing encrypted text called encrypted.aes
* File containing the decrypted text called decrypted.<extension>
* Outputs True if original file equals decrypted file

## Example

```
True
```