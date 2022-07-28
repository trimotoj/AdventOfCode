triangels=0
with open('2016/day3/vstup','r') as file:
    for line in file:
        line=line.strip().split()
        line = list(map(int, line))
        if line[0] + line[1] > line[2]:
            if line[1] + line[2] > line[0]:
                if line[0] + line[2] > line[1]:
                    triangels+=1
print(triangels)