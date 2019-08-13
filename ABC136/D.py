S = input()

setList = []
RFlag = False
Lcount = 0
Rcount = 0

for i in range(len(S)) :
    if RFlag :
        if S[i] == 'L' :
            setList.append([i, Rcount])
            Rcount = 0
            RFlag = False
            Lcount += 1
            if i == len(S) - 1 :
                setList[-1].append(Lcount)
        else :
            Rcount += 1
    else :
        if S[i] == 'L' :
            Lcount += 1
            if i == len(S) - 1 :
                setList[-1].append(Lcount)
        else :
            Rcount += 1
            if len(setList) != 0 :
                setList[-1].append(Lcount)
                Lcount = 0
            RFlag = True


#print(setList)

ansList = [0] * len(S)

for i in range(len(setList)) :
    Lnum1 = setList[i][1] // 2
    Rnum1 = setList[i][1] - Lnum1

    Rnum2 = setList[i][2] // 2
    Lnum2 = setList[i][2] - Rnum2

    ansList[setList[i][0] - 1] = Rnum1 + Rnum2
    ansList[setList[i][0]] = Lnum1 + Lnum2

for i in range(len(S)) :
    print(ansList[i], end=' ')
