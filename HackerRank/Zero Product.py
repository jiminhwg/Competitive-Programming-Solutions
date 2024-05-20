A = list(input().split())
A = [int(i) for i in A]
product = 1

for a in A:
    product = product * a 

if product == 0:
    print("Zero")
else:
    print("Not Zero")