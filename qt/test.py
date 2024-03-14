import hashlib

haslo = 'qwerty123'

haslo = hashlib.md5(haslo.encode('utf-8')).hexdigest()

print(haslo)