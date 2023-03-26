def min_num(a,b,c,d):
    l = [a,b,c,d]
    min = l[0]
    for i in range(1,4):
        if min > l[i]:
            min = l[i]
    return min
a,b,c,d = [int(i) for i in input().split()]

print(min_num(a,b,c,d))