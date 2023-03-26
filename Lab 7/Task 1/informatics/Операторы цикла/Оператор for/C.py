a = int(input())
b = int(input())
s = ''
for i in range(a,b+1):
    if i**(1/2) == int(i**(1/2)):
        s+= str(i) + ' '
print(s)