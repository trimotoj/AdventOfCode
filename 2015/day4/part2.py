import hashlib
from random import *
md5hash=''
num=0
while md5hash[:6] != '000000':
     vstup='ckczppom'
     vstup+=str(num)
     md5hash=hashlib.md5(vstup.encode('utf-8')).hexdigest()
     if md5hash[:6] != '000000':
        num+=1
print(num)