n = int(input())
l = [int(i) for i in input().split()]
k = 0
for i in range(1,n-1):
    if l[i] > l[i-1] and l[i] > l[i+1]:
        k += 1
print(k)