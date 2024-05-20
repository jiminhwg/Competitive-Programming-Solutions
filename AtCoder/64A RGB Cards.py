R, G, B = input().split()
Combined = R+G+B

if int(Combined) % 4 == 0:
    print("YES")
else:
    print("NO")

