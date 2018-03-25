import hashlib as hasher
import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)

print("hello world")
# class Block:

string = "han gaisho"

hstring = hasher.sha256(string.encode('utf-8')).hexdigest()

print(hstring)