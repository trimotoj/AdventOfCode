with open('2015/day2/vstup') as file:
    total=0
    for line in file:
        line=line.rstrip().split('x')
        line = sorted(list(map(int, line)))
        stuha=(2*line[0]+2*line[1])+(line[0]*line[1]*line[2])
        total+=stuha
print(total)