Received = list(input().split())
Received = [int(i) for i in Received]
Spent = list(input().split())
Spent = [int(i) for i in Spent]

print(sum(Received))
print(sum(Spent))
print(sum(Received) - sum(Spent))
