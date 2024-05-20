n, k = map(int, input().split())

for a in range(k): 
    b = n%10
    if b != 0:
        n = n-1
    else:
        n = n//10

print(n)

