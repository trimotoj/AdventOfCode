#CONDITIONS
def double_letters(line):
    for char in range(len(line)-1):
        if line[char:char+2] in line[char+2:]:
            return True
def triple_letters(line):
    for char in range(len(line)-2):
        if line[char] == line[char+2]:
            return True

#EXECUTION            
nice_strings=0
with open('2015/day5/vstup') as file:
    for line in file:
        line=line.strip()
        if double_letters(line) == True:
            if triple_letters(line) == True:
                nice_strings+=1
                
print(nice_strings)       
            