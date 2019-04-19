S = input()

ans1 = 0
ans2 = 0

for i in range(len(S)) :
    if i % 2 == 1 :
        if S[i:i+1] == '0' :
            ans1 += 1
        else :
            ans2 += 1
    else :
        if S[i:i+1] == '1' :
            ans1 += 1
        else :
            ans2 += 1

print(min(ans1, ans2))
