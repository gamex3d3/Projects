
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"encrypted message: {cipher_text}")

decrypt= input("Decryption key: ")
if decrypt == 'lol':
    print(f"original message : {plain_text}")
else:
    print(f"Incorrect decryption key")

              



