input=265149
x=1
i=1
while i != input:
    if i == x*x:
        x+=2
    i+=1
while input < (x*x) - (x//2):
    input+=x//2
print((x-1)-((x*x)-input))