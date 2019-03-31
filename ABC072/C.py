N = int(input())
a = list(map(int, input().split()))

count = [0] * 10**5

for e in a :
    if e != 0 :
        count[e - 1] += 1
    count[e] += 1
    if e != 10**5 - 1 :
        count[e + 1] += 1

print(max(count))
