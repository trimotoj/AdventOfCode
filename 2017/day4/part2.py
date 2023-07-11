valid=0
with open('2017/day4/input') as file:
    for line in file:
        line = [''.join(sorted(word)) for word in line.strip().split()]
        if len(line) == len(set(line)):
            valid+=1
print(valid)