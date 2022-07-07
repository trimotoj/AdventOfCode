with open('2015/day3/vstup') as file:
    file=file.read()
    x , y = 0 , 0
    arr=[]
    houses=1
    for i in file:
        if i == '^':
            y-=1
        if i == 'v':
            y+=1
        if i == '>':
            x+=1
        if i == '<':
            x-=1 
        if [x, y] not in arr:
            houses+=1
        arr.append([x,y])
print(houses)        