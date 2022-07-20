def urcovac_smeru(instruction):
    global smer
    if smer == '>':
        if instruction[:1] == 'R':
            smer = 'v'
        else:
            smer = '^'    
    elif smer == '<':
        if instruction[:1] == 'R':
            smer = '^'
        else:
            smer = 'v'
    elif smer == 'v':
        if instruction[:1] == 'R':
            smer = '<'
        else:
            smer = '>'    
    else:
        if instruction[:1] == 'R':
            smer = '>'
        else:
            smer = '<'
def pohyb(smer):
    global x, y
    if instruction[:1] == 'R':
        if smer == '>':
            x+=int(instruction[1:])
        elif smer == '<':
            x-=int(instruction[1:])
        elif smer == 'v':
            y-=int(instruction[1:])
        else:
            y+=int(instruction[1:])
    else:
        if smer == '>':
            x+=int(instruction[1:])
        elif smer == '<':
            x-=int(instruction[1:])
        elif smer == 'v':
            y-=int(instruction[1:])
        else:
            y+=int(instruction[1:]) 
smer = ''
x, y = 0, 0
with open('2016/day1/vstup','r') as file:
    instructions=file.read().strip().split(', ')
    for instruction in instructions:
        urcovac_smeru(instruction)
        pohyb(smer)
print(abs(x)+(abs(y)))