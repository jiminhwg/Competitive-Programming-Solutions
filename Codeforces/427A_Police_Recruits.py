NumberOfEvents = int(input())
lst = list(input().split())

CrimeCount = 0
RecruitCount = 0
#making list into integers
NewLst = [int(i) for i in lst]

for a in NewLst:
    if a == -1:
        #if there is no recruit, increase the crimecount by 1
        if RecruitCount == 0:
            CrimeCount += 1 
        #if there is a recruit already, if (RecruitCount - a != 0) or (RecruitCount -a == 0), subtract RecruitCount by 1
        elif RecruitCount > 0:
            if RecruitCount - a != 0:
                RecruitCount -= 1
                continue
            elif RecruitCount - a == 0:
                RecruitCount -= 1
    #increase recruitcount by the a
    elif a > 0:
        RecruitCount += a

print(CrimeCount)
