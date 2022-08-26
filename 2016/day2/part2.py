keypad=[
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ','1',' ',' ',' '],
    [' ',' ','2','3','4',' ',' '],
    [' ','5','6','7','8','9',' '],
    [' ',' ','A','B','C',' ',' '],
    [' ',' ',' ','D',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ']
]
def move(instruction):
    global x,y
    if instruction == 'R' and keypad[y][x+1] != ' ':
        x+=1
    elif instruction == 'L' and keypad[y][x-1] != ' ':
        x-=1
    elif instruction == 'U' and keypad[y-1][x] != ' ':
        y-=1
    elif instruction == 'D' and keypad[y+1][x] != ' ':
        y+=1    
x=1
y=3
code=''
with open('2016/day2/vstup','r') as file:
    for line in file:
        line=line.strip()
        for instruction in line:
            move(instruction)
        code+=keypad[y][x]      
print(code)       

