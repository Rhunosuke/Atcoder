L, R = map(int, input().split())

min1 = 10000
border = 4039
ancker = 99999

'''
for i in range(L, min(R+1, L + border)) :
    if i % 2019 < min1 :
        min1 = i % 2019
        ancker = i

min2 = 100000

for i in range(L, min(R+1, L + border)) :
    if i % 2019 < min2 and i != ancker:
        min2 = i % 2019
'''

min1 = 100000

for i in range(L,  min(R+1, L + border)) :
    for j in range(i + 1, min(R+1, L + border)) :
        if (i * j) % 2019 < min1 :
            min1 = (i * j) % 2019

#ans = (min1 * min2) % 2019

print(min1)
