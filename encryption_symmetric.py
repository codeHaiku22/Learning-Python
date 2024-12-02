import cryptography.fernet

def generateKey():
    try:
        key  = cryptography.fernet.Fernet.generate_key()
        return key
    except Exception as e:
        print(str(e))

def enrcyptString(plainText, key):
    try:
        fernet = cryptography.fernet.Fernet(key)
        encText = fernet.encrypt(plainText.encode())
        return encText
    except Exception as e:
        print(str(e))

def decryptString(encText, key):
    try:
        fernet = cryptography.fernet.Fernet(key)
        plainText = fernet.decrypt(encText).decode()
        return plainText
    except Exception as e:
        print(str(e))    

key = generateKey()

#To convert key to string for storage in a file
strKey = key.decode('utf-8')

#To convert key back ot bytes after retrieval from a file where it was stored
key = str.encode(strKey, 'utf-8')

encrypted = enrcyptString('Hello World!', key)

print(encrypted)

decrypted = decryptString(encrypted, key)

print(decrypted)
