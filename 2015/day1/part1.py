subor=open('2015/day1/vstup','r')
subor = subor.read()
poschodie=0

for i in subor:
    if i == '(':
        poschodie+=1
    else:
        poschodie-=1

print(poschodie)            