Receivedlst = []
Spentlst = []
toprint = []

while True:
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
    elif b == 5:
        toprint.append(sum(Receivedlst)-sum(Spentlst))
    elif b == 6:
        break

for c in toprint:
    print(c)

    