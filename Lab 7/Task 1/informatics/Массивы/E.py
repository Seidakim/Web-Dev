n = int(input())
l = [int(i) for i in input().split()]
is_ok = False
for i in range(n-1):
    if (l[i] < 0 and l[i+1]<0) or (l[i] >= 0 and l[i+1] >= 0):
        is_ok =True
        break
print('YES' if is_ok else 'NO')