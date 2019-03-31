n = int(input())
a = list(map(int, input().split()))

sum = a[0]
count1 = 0
count2 = 0

sum1 = 0
sum2 = 0

for i in range(n) :
    sum1 += a[i]
    sum2 += a[i]
    if i % 2 == 0 :
        if sum1 >= 0 :
            count1 += abs(sum1) + 1
            sum1 = -1
        if sum2 <= 0 :
            count2 += abs(sum2) + 1
            sum2 = 1
    elif i % 2 == 1 :
        if sum1 <= 0 :
            count1 += abs(sum1) + 1
            sum1 = 1
        if sum2 >= 0 :
            count2 += abs(sum2) + 1
            sum2 = -1

print(min(count1, count2))
