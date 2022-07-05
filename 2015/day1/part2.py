subor=open('2015/day1/vstup','r')
subor = subor.read()
poschodie=0
for i in range(len(subor)):
    if subor[i] == '(':
        poschodie+=1
    else:
        poschodie-=1
    if poschodie == -1:
        zapor=i+1 
        break   
print(zapor) 