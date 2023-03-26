n = input()
a = [int(i) for i in input().split()]
a = set(a)
a = list(a)
a.sort()
print(a[-2])
