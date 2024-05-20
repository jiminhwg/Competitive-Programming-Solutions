n = int(input())
A = 100
D = 100

for i in range(0,n):
    A_dice, D_dice = map(int, input().split())
    if A_dice > D_dice:
        D -= A_dice
    elif A_dice < D_dice:
        A -= D_dice
    else:
        continue

print(A)
print(D)

    