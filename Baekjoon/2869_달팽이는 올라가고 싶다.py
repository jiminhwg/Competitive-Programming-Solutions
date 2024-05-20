A, B, V = map(int,input().split())
#a = morning, b = night, v = height

C = 0
count = 0

while C < V:
    count +=1
    C = C+A
    C = C-B
    if C == V or C > V:
        print(count-1)
        break
    else:
        continue



