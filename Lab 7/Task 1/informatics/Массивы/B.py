n = int(input())
l = [int(i) for i in input().split()]
s = ''
for i in l:
    if i%2==0:
        s += str(i) + ' '
print(s)
