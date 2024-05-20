Transactions = int(input())
Receivedlst = []
Spentlst = []
toprint = []
for a in range(Transactions):
    b = int(input())
    if b == 1:
        Received = int(input())
        Receivedlst.append(Received)
    elif b == 2:
        Spent = int(input())
        Spentlst.append(Spent)
    elif b == 3:
        toprint.append(sum(Receivedlst))
    elif b == 4:
        toprint.append(sum(Spentlst))
    else:
        toprint.append(sum(Receivedlst)-sum(Spentlst))

for c in toprint:
    print(c)

    