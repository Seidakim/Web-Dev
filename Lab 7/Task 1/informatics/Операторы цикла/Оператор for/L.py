k = input()
num = 0
for i in range(len(k)):
    degree = len(k)-1 - i
    num += int(k[i])* 2**degree
print(num)
