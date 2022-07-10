with open('2015/day3/vstup') as file:
    file=file.read()
    x , y = 0 , 0
    santa=((0,0),)
    robot=((0,0),)
    common=()
    houses=1
    for i in range(len(file)):
        if i % 2 == 1:
            (x,y) = robot[-1]
            if file[i] == '^':
                y-=1
            if file[i] == 'v':
                y+=1
            if file[i] == '>':
                x+=1
            if file[i] == '<':
                x-=1    
            robot+=(x,y),
        else:
            (x,y) = santa[-1]
            if file[i] == '^':
                y-=1
            if file[i] == 'v':
                y+=1
            if file[i] == '>':
                x+=1
            if file[i] == '<':
                x-=1   
            santa+=(x,y),
santa=set(santa)
robot=set(robot)
for i in santa:
    if i in robot:
        common+=(i),  
           
print((len(santa)+len(robot))-(len(common)))


