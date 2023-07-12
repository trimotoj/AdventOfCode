
with open('2017/day6/input') as file:
    memory_banks = [int(i) for i in file.read().strip().split()]

patterns=[]
cycles=0
while True:
    i=0
    while memory_banks[i] != max(memory_banks):
        i+=1
    position=i+1
    cycle_counter = 0
    number_of_cycles = memory_banks[i]
    memory_banks[i] = 0
    while cycle_counter != number_of_cycles:
        if position == len(memory_banks):
            position = 0
        memory_banks[position]+=1
        position+=1
        cycle_counter+=1
    if memory_banks not in patterns:
        patterns.append(list(memory_banks))
        cycles+=1
    else:
        cycles+=1
        break
print(cycles)

