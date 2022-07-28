cislo = 5
x, y  = 0, 0
kod   = ''
with open('2016/day2/vstup','r') as file:
    for line in file:
        line=line.strip()
        for instruction in line:
            if x == -1 and instruction == 'L':
                continue
            elif x == 1 and instruction == 'R':
                continue
            elif y == -1 and instruction == 'D':
                continue
            elif y == 1 and instruction == 'U':
                continue
            else:            
                if instruction == 'L':
                    cislo -= 1
                    x -= 1
                elif instruction == 'R':
                    cislo += 1
                    x += 1
                elif instruction == 'U':
                    cislo -= 3
                    y += 1
                else:
                    cislo += 3
                    y -= 1        
        kod += str(cislo)
print(kod)        
        