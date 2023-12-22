#! /usr/bin/python3

"""
Substitution Cipher: -
	A. Mono-alphabetic: -
		1. Additive Cipher (Shift Cipher or Caesar Cipher): It's total key space is 26. We add and subtract key value to ascii character to encrypt and decrypt resp.

  		2. Multiplicative Cipher: It's total key space is 12. We multiply and divide key value to ascii character to encrypt and decrypt resp.

  		3. Affine Cipher: It is a combination of additive and multiplicative cipher and it's key space is 312 (12 * 26). We multiply and add key value to ascii character to encrypt and divide and substract key value to ascii character to decrpty.
"""
# Additive Cipher
def additive_cipher_encrypt(text:str,n:int):
    encrypt_txt = ""
    for i in range(len(text)):
        if text[i].isupper():
            x = ord(text[i]) - 65		# convert character into integer
            En = (x + n) % 26			# formula
            encrypt_txt += chr(En + 65)	# convert integer into character
        elif text[i].islower():
            x = ord(text[i]) - 97		# convert character into integer
            En = (x + n) % 26			# formula
            encrypt_txt += chr(En + 97)	# convert integer into character
    return encrypt_txt

def additive_cipher_decrypt(text:str,n:int):
    decrypt_txt = ""
    for i in range(len(text)):
        if text[i].isupper():
            x = ord(text[i]) - 65		# convert character into integer
            Dn = (x - n) % 26			# formula
            decrypt_txt += chr(Dn + 65)	# convert integer into character
        elif text[i].islower():
            x = ord(text[i]) - 97		# convert character into integer
            Dn = (x - n) % 26			# formula
            decrypt_txt += chr(Dn + 97)	# convert integer into character
    return decrypt_txt

# Multiplicative Inverse
def multiplicative_inverse(a, b):
	dividend = max(a, b)
	divisor = min(a, b)
	quotient = dividend // divisor
	remainder = dividend - (quotient * divisor)
	t1 = 0
	t2 = 1
	t = t1 - (t2 * quotient)
	while(True):
		dividend = divisor
		divisor = remainder
		if divisor == 0:
			break
		quotient = dividend // divisor
		remainder = dividend - (quotient * divisor)
		t1 = t2
		t2 = t
		t = t1 - (t2 * quotient)
	return t2

# Multiplicative Cipher
def multiplicative_cipher_encrypt(text:str,n:int):
    encrypt_txt = ""
    for i in range(len(text)):
        if text[i].isupper():
            x = ord(text[i]) - 65		# convert character into integer
            En = (x * n) % 26			# formula
            encrypt_txt += chr(En + 65)	# convert integer into character
        elif text[i].islower():
            x = ord(text[i]) - 97		# convert character into integer
            En = (x * n) % 26			# formula
            encrypt_txt += chr(En + 97)	# convert integer into character
    return encrypt_txt

def multiplicative_cipher_decrypt(text:str,n:int):
    decrypt_txt = ""
    n = multiplicative_inverse(n,26)
    for i in range(len(text)):
        if text[i].isupper():
            x = ord(text[i]) - 65				# convert character into integer
            Dn = (x * n) % 26					# formula
            decrypt_txt += chr(int(Dn) + 65)	# convert integer into character
        elif text[i].islower():
            x = ord(text[i]) - 97				# convert character into integer
            Dn = (x * n) % 26					# formula
            decrypt_txt += chr(int(Dn) + 97)	# convert integer into character
    return decrypt_txt

#Affine Cipher
def affine_cipher_encrypt(text:str,n:int,m:int):
    encrypt_txt = ""
    for i in range(len(text)):
        if text[i].isupper():
            x = ord(text[i]) - 65		# convert character into integer
            En = ((x * n) + m) % 26		# formula
            encrypt_txt += chr(En + 65)	# convert integer into character
        elif text[i].islower():
            x = ord(text[i]) - 97		# convert character into integer
            En = ((x * n) + m) % 26		# formula
            encrypt_txt += chr(En + 97)	# convert integer into character
    return encrypt_txt

def affine_cipher_decrypt(text:str,n:int,m:int):
    decrypt_txt = ""
    n = multiplicative_inverse(n,26)
    for i in range(len(text)):
        if text[i].isupper():
            x = ord(text[i]) - 65		# convert character into integer
            Dn = ((x - m) * n) % 26	# formula
            decrypt_txt += chr(Dn + 65)	# convert integer into character
        elif text[i].islower():
            x = ord(text[i]) - 97		# convert character into integer
            Dn = ((x - m) * n) % 26	# formula
            decrypt_txt += chr(Dn + 97)	# convert integer into character
    return decrypt_txt


msg = 'HELLO'
shift = 7	# addition / subtraction shift
shift2 = 7	# multiplication / division shift

print(additive_cipher_encrypt(msg,shift))
print(multiplicative_cipher_encrypt(msg,shift))
print(affine_cipher_encrypt(msg,shift,shift2))


print(additive_cipher_decrypt(additive_cipher_encrypt(msg,shift),shift))
print(multiplicative_cipher_decrypt(multiplicative_cipher_encrypt(msg,shift),shift))
print(affine_cipher_decrypt(affine_cipher_encrypt(msg,shift,shift2),shift,shift2))
