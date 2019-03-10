sum = 0

num = int(input())

for i in range(num) :
    money, currency = input().split()
    money = float(money)
    if currency == 'JPY' :
        sum += money
    else :
        sum += money * 380000

print(sum)
