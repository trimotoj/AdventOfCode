solution=0
with open('2017/day2/input') as file:
    for line in file:
        line = (sorted(list(map(int,line.strip().split()))))[-1::-1]
        for i in range(len(line)-1):
            for j in range(i+1,len(line)):
                if line[i] % line[j] == 0:
                    solution+=line[i] // line[j]
                    break
            if line[i] % line[j] == 0:
                    break
print(solution)         


        
