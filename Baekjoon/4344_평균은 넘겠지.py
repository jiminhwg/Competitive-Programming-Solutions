NewList = []
FinalAnswers = []

for a in range(0,int(input())):
    List = input().split()
    List = [int(x) for x in List]
    for b in List:
        if b <= (sum(List[1:len(List)])/(len(List)-1)):
            continue
        else:
            NewList.append(b)
    FinalAnswers.append((len(NewList)/int(List[0]))*100)
    NewList.clear()

for c in FinalAnswers:
    percentage = "{:.3f}".format(c)
    print(f"{percentage}%")

        
