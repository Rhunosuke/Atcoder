import fractions

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

A, B, C, D = map(int, input().split())

B_C = B // C
B_D = B // D
B_C_D = B // lcm(C, D)

A_C = (A - 1) // C
A_D = (A - 1) // D
A_C_D = (A - 1) // lcm(C, D)

B_div = B_C + B_D - B_C_D
A_div = A_C + A_D - A_C_D



print(B - A + 1 - (B_div - A_div))
