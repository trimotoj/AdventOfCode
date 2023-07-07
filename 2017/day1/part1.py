with open('2017/day1/input') as file:
    data=file.read()
solution=0
for i in range(-1,len(data)-1):
    if data[i] == data[i+1]:
        solution+=int(data[i])
print(solution)