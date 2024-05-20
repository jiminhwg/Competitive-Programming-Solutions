Number = int(input())
lst = []
for a in range(Number):
    A, B = map(int, input().split())
    lst.append(A+B)

count = 1
for b in lst:
    print("Case #"+ str(count)+":" + " " + str(b))
    count = count + 1
