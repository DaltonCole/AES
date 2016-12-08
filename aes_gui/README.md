# AES GUI

## To Run

Either:
* Go to: https://obscure-castle-46174.herokuapp.com/ (RECOMMENDED METHOD)

* rails server
  * Then go to localhost:3000 in your web browser of choice

## Requirements for running locally:

* ruby 2.3.1p112 (2016-04-26 revision 54768) [x86_64-darwin15]
* Python 3.5.1
* Rails 5.0.0.1

## Note:

* You must refresh after each encryption and decryption

## Warning messages

### The following will generate a warning message

* If encrypt or decrypt is not specified
* No file is given
* No mode is specified
* Key is not 16, 24, or 32 characters long
* IV, if using CBC mode, is not given or not 16 characters long