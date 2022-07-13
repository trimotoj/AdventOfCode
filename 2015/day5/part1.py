#CONDITIONS
def vowel_counter(line):
    global vowel
    for char in line:
        if char in 'aeiou':
            vowel+=1

def double_letters(line):
    for char in range(len(line)-1):
        if line[char] == line[char+1]:
            return True   

def prohibited_strings(line):
    for i in con3:
        if i in line:
            return False
# EXUCUTION
nice_strings = 0
con3 = ('ab' , 'cd' , 'pq' , 'xy')
with open('2015/day5/vstup') as file:
    for line in file:
        line=line.strip()
        vowel = 0
        vowel_counter(line)
        if vowel >= 3:
            if double_letters(line) == True:
                if prohibited_strings(line) != False:
                    nice_strings+=1

print(nice_strings)                  




