X, Y = map(int, input().split())
a = []

if Y%2 == 0:
   for i in range(Y//4+1):
       a.append(int(i+(Y-i*4)/2))
       
print("Yes" if X in a else "No")