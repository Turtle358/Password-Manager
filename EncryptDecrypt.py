def toInt(word):
    integer = []
    for i in range(len(word)):
        integer.append(ord(word[i]))
    return integer
def encrypt(word):
    encrypted, encryptedlist, encryptedstr = [],[],""
    integer = toInt(word)
    for i in range(len(integer)):
        encrypted.append(integer[i] << 2)
        encryptedstr += chr(encrypted[i])
    return encryptedstr

def decrypt(word):
    integer, decryptedlist, decrypted = [],[],""
    for i in range(len(word)):
        integer.append(ord(word[i]))
        decryptedlist.append(integer[i] >> 2)
        decrypted += chr(decryptedlist[i])
    return decrypted


encryptedword = encrypt("Hello World")
print(encryptedword)
print(decrypt(encryptedword))
