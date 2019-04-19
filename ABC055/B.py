import math

N = int(input())

power = 1
NUM = 10 ** 9 + 7

for i in range(1, N + 1) :
    power *= i 
    if power >= NUM :
        power %= NUM
print(power)
"""
power = math.factorial(N)

print(power % (10 ** 9 + 7))
"""
