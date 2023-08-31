plaintext = input("Enter a msg:")
key = "qwertyuiopasdfghjklzxcvbnm"

ciphertext = ""

for c in plaintext :
    if(c == " "):
        ciphertext += " "
        continue

    elif (c.isupper()):
            cipher =  key[(ord(c) - 65)]
            ciphertext = ciphertext + cipher.upper()

    else:
        cipher =  key[(ord(c) - 97)]
        ciphertext = ciphertext + cipher   

print("Cipher is : "+ ciphertext)

ciphertext = input("Enter the ciphertext: ")
key = "qwertyuiopasdfghjklzxcvbnm"

plaintext = ""

for c in ciphertext:
    if c == " ":
        plaintext += " "
        continue

    elif c.isupper():
        plain_char = chr(key.index(c.lower()) + 65)
        plaintext += plain_char.upper()

    else:
        plain_char = chr(key.index(c) + 97)
        plaintext += plain_char

print("Decrypted text is:", plaintext)

