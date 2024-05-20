A = int(input())
count0 = 0
count1 = 0
for a in range(A):
    Number = int(input())
    if Number == 0:
        count0 = count0 + 1
        continue
    else:
        count1 = count1 + 1
        continue

if count0 > count1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

    