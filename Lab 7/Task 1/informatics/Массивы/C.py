n = input()
l = [int(i) for i in input().split()]
k = 0
for i in l:
    if i > 0:
        k+=1
print(k)