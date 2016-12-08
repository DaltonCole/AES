# RSA vs AES Comparison

This folder contains the data involving comparing RSA to AES with similar key sizes.

## AES RSA Comparison.pdf

Comparison data and graphs for RSA and AES

## REPORT.txt

Brief report on RSA vs AES

## driver.py

This file runs the RSA algorithm on key sizes of 128, 192, and 256 on 1000 different inputs of each size.

### To Run

python3 driver.py

#### Note

* input128.txt, input196.txt, input256.txt must exist

## input_generator.py

This file generates 1000 random words for key size 128, 196, 256 that works with RSA

### To Run

python3 input_generator.py

## times.py

This file runs the AES algorithm on key sizes of 128, 192, and 256 on 1000 different inputs of each size.

### To Run

python3 times.py

#### Note

* input128.txt, input196.txt, input256.txt must exist

## data/

This directory contains all of the data involving run times of RSA and AES

# Requirements

Python 3.5.1
pip install rsa