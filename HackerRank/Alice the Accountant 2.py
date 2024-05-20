lst = list(input().split())
spent = []
received = []

for a in lst:
    if "-" in a:
        spent.append(a)
    else:
        received.append(a)
received = [int(i) for i in received]
spent = [int(i) for i in spent]

print(sum(received))
print(abs(sum(spent)))
print(sum(received) + sum(spent))
