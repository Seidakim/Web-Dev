n = input()
d = [i for i in input().split()]
s = ''
for i in range(len(d)):
    if i%2==0:
        s+= d[i] + ' '
print(s)