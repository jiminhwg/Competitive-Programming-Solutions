input = int(input())
a = 1
b = 1
c = 0
d = 0
for x in range(0,input):
    if c == a:
        b = 0
        if d == a:
            c = 0
            d = 0
            a += 1
            b = 1
    if b == 1:
        print("PAK")
        c += 1
    else:
        print("GANERN")
        d += 1

