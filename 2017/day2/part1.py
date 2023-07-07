solution=0
with open('2017/day2/input') as file:
    for line in file:
        line=list(map(int,line.strip().split()))
        solution+=max(line) - min(line)
print(solution) 