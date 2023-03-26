a = int(input())
answer = 'NO'
if a%400==0 :
    answer = 'YES'
elif a%4==0 and a%100!=0:
    answer = 'YES'
print(answer)
