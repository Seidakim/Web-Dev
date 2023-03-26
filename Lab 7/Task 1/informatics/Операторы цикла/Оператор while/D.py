n = int(input())
is_ok = False
while n>=1:
    if n==1:
        is_ok = True
    n/=2
print('YES' if is_ok else 'NO')