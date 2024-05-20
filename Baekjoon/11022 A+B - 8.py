Number = int(input())
lst = []
Anumber = []
Bnumber = []
for a in range(Number):
    A, B = map(int, input().split())
    Anumber.append(A)
    Bnumber.append(B)
    lst.append(A+B)

count = 1
count2 = 0
for b in lst:
    print("Case #"+ str(count)+": " + str(Anumber[count2]) + " + " + str(Bnumber[count2]) + " = " + str(b))
    count = count + 1
    count2 = count2 + 1
