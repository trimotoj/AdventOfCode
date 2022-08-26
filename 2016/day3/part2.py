pocet=0
triangels=[]
with open('2016/day3/vstup','r') as file:
    for line in file:
        line=line.strip().split()
        line = list(map(int, line))
        triangels.append(line)
        if len(triangels) == 3:
            for i in range(len(triangels[0])):
                if triangels[0][i] + triangels[1][i] > triangels[2][i]:
                    if triangels[0][i] + triangels[2][i] > triangels[1][i]:
                        if triangels[1][i] + triangels[2][i] > triangels[0][i]:
                            pocet+=1
            triangels=[]                
print(pocet)
        