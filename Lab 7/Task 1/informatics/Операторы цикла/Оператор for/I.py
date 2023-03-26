a = int(input())
if a == 1:
    print(1)
if a == 2:
    print(2)
if a >2:
    n = 2
    for i in range(2,a):
        if a%i==0:
            n+=1
    print(n)
