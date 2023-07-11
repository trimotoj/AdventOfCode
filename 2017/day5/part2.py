with open('2017/day5/input') as file:
    steps = [int(line.strip()) for line in file]

index=0
count=0
while True:
    try:
        step=steps[index]
        if steps[index] >= 3:
            steps[index]-=1
        else:
            steps[index]+=1
        index+=step
        count+=1
    except:
        print(count)
        break
    