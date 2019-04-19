N = int(input())

start = 0
end = 0

person = N

cap = [10 ** 15 + 1]

for _ in range(5) :
    cap.append(int(input()))

for i in range(1, 6) :
    person = N - (end - start) * cap[i]
    if person <= 0 :
        person = 1
    end += - (- person // cap[i])
    start += 1
print(end)
