S = input()

ans = True

for i in range(3) :
    if S[i:i+1] == S[i+1:i+2] :
        ans = False

if ans :
    print('Good')
else :
    print('Bad')
