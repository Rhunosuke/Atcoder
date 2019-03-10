S = input()

string = "abcdefg"
string = string.lstrip("acba")
print(string)

while len(S) > 0 :
    print(S)
    if S.startswith("dreameraser") :
        S = S.lstrip("dreameraser")
        continue
    elif S.startswith("dreamerase") :
        S = S.lstrip("dreamerase")
        continue
    elif S.startswith("dreamer") :
        S = S.lstrip("dreamer")
        print(S)
        continue
    elif S.startswith("erase") :
        S = S.lstrip("erase")
        continue
    elif S.startswith("eraser") :
        S = S.lstrip("eraser")
        continue
    else :
        print(S)
        break

if len(S) == 0 :
    print('YES')
else :
    print('NO')
