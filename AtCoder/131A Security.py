S = str(input())
A = True
for b in range(3):
  if S[b+1] == S[b]:
    A = False
    
if A:
  print("Good")
else:
  print("Bad")


