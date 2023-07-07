with open('2017/day1/input') as file:
    data=file.read()
solution=0
for i in range(len(data)//2):
    if data[i] == data[int(len(data)/2+i)]:
        solution+=int(data[i])*2
print(solution)