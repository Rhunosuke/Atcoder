A, B, C = map(int, sorted(list(map(int, input().split()))))

count = 0

A += C - B
count += C - B

count += (C - A) // 2

if (C - A) % 2 != 0 :
    count += 2

print(count)
