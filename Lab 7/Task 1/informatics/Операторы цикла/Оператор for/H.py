s = ''
a = int(input())
for i in range(1,a+1):
    if a%i==0:
        s+=str(i) + ' '
print(s)