lst = []
while True:
    try:
        A, B = map(int, input().split())
        lst.append(A+B)
    except:
        break
for a in lst:
    print(a)

