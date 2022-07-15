x=1000
y=1000
gridline = []
grid = []
for i in range(x):
    gridline.append(0)
for i in range(y):
    grid.append(list(gridline))

with open('2015/day6/vstup') as file:
    for line in file:
        line = line.strip().replace(',',' ').split()
        if 'turn' in line:
            line=line[1:]           
        for gridline in grid[int(line[2]):int(line[5])+1]:
                for i in range(int(line[1]),int(line[4])+1):
                    if line[0] == 'toggle':
                        if gridline[i] == 0:
                            gridline[i] = 1
                        else:
                            gridline[i] = 0    
                    elif line[0] == 'on':
                        gridline[i] = 1
                    else:
                        gridline[i] = 0
lit_light=0
for gridline in grid:
    for i in gridline:
        if i == 1:
            lit_light+=1 

print(lit_light)