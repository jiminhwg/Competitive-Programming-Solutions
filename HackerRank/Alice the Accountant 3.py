Transactions = int(input())
lst = []
newlst = []
for a in range(Transactions):
    b = int(input())
    if b == 0:
        newlst.append(sum(lst))
    elif b > 0:
        lst.append(b)
        continue 

for c in newlst:
    print(c)
