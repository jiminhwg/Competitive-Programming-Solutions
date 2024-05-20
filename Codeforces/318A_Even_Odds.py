
n, k = map(int, input().split())
odd = []
even = []

for a in range(1,n+1):
    if a%2 == 0:
        even.append(a)
    else:
        odd.append(a)

finallist = odd+even
print(finallist[k-1])


