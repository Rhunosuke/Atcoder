N, M = map(int, input().split())
drinkList = [list(map(int, input().split())) for i in range(N)]

drinkList.sort()
drinkCount = 0
money = 0

while drinkCount < M :
    for i in range(N) :
        if M - drinkCount > drinkList[i][1] :
            money += drinkList[i][0] * drinkList[i][1]
            drinkCount += drinkList[i][1]
        else :
            money += drinkList[i][0] * (M - drinkCount)
            drinkCount += M - drinkCount
            break

print(money)
