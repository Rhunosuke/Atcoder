N = int(input())
A = list(map(int, input().split()))

count = 0
while sum(list(map(lambda x: x % 2, A))) == 0 :
    count += 1
    A = list(map(lambda x: x / 2, A))

print(count)
