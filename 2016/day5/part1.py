import hashlib
md5hash=''
num=0
password = ''
while len(password) != 8:
    while md5hash[:5] != '00000':
        vstup='reyedfim'
        vstup+=str(num)
        md5hash=hashlib.md5(vstup.encode('utf-8')).hexdigest()
        if md5hash[:5] != '00000':
            num+=1
    password+=md5hash[5]
    md5hash=''
    num+=1
print(password)