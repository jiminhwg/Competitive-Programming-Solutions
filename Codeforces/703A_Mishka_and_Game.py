NumberOfRounds = int(input())
MishkaCount = 0
ChrisCount = 0

#counting whoever won each round 
for a in range(NumberOfRounds):
    Mishka, Chris = input().split()
    if Mishka < Chris:
        ChrisCount += 1
    elif Mishka > Chris:
        MishkaCount += 1

if MishkaCount > ChrisCount:
    print("Mishka")
elif MishkaCount < ChrisCount:
    print("Chris")
else:
    print("Friendship is magic!^^")