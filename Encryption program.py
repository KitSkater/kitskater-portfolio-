import random
import string

chars = string.punctuation + string.ascii_letters + string.digits + ' '

chars = list(chars)
key = chars.copy()
random.shuffle(key)

#emcrypt 
plain_text = input("Enter the text to encrypt: ")
cipher_text = ''
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print("Encrypted text: ", cipher_text)
#decrypt
cipher_text = input("Enter the text to decrypt: ")
plain_text = ''
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print("Decrypted text: ", plain_text)
