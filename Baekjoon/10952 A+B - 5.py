lst = []
while True:
    try:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        else:
            lst.append(A+B)
    except:
        break
for a in lst:
    print(a)

