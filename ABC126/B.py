S = input()

S1 = int(S[0:2])

S2 = int(S[2:])

flag1 = False
flag2 = False

if S1 >= 1 and S1 <= 12 :
    flag1 = True
if S2 >= 1 and S2 <= 12 :
    flag2 = True

if flag1 and flag2 :
    print('AMBIGUOUS')
elif (not flag1) and flag2 :
    print('YYMM')
elif flag1 and (not flag2) :
    print('MMYY')
else :
    print('NA')
