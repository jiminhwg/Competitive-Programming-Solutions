array = []

for num in range(5):
    array.append(list(input().split())) #makes array
for i in range(5):
    n = 0
    for j in range(5):
        if array[i][j] == "1":
            numi = i
            numj = j
            n = 1
            break
    if n == 1:
        break

print(abs(numi-2)+abs(numj-2))
