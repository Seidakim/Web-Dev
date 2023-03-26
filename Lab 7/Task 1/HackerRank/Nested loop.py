n = int(input())
p = set()
d= {}
for i in range(n):
    s = input()
    k = float(input())
    p.add(k)
    d[s] = k
p = list(p)
p.sort()
l = []
for i,j in d.items():
    if j == p[1]:
        l.append(i)
l.sort()
for i in l:
    print(i)