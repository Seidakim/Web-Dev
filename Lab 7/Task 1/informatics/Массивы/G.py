n = int(input())
l = [int(i) for i in input().split()]
s = ''
for i in range(n-1,-1,-1):
    s += str(l[i]) + ' '
print(s)