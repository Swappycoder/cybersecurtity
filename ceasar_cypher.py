plaintext = input("Enter a msg:")
text = ""
key = int(input("Enter key:"))  

for ch in plaintext:
    if ch == " ":
        text += " "
         
    elif ch.isupper():
        cipher = chr((ord(ch) + key - 65) % 26 + 65)  
        text += cipher.upper()

    else:
        cipher = chr((ord(ch) + key - 97) % 26 + 97)  
        text += cipher.lower()
    
print("Cipher is: " + text)


ciphertext = input("Enter a msg:")
text = ""
key = int(input("Enter key:"))  

for ch in ciphertext:
    if ch == " ":
        text += " "
         
    elif ch.isupper():
        decipher = chr((ord(ch) - key - 65) % 26 + 65)  
        text += decipher.upper()

    else:
        decipher = chr((ord(ch) - key - 97) % 26 + 97)  
        text += decipher.lower()
    
print("Deciphered is: " + text)
