Word = input()

StrippedWords = []
FinalWords = []

for a in Word: #removes letters other than "helo"
    if a not in "helo":
        continue
    else:
        StrippedWords.append(a)

count = 0
for b in StrippedWords:
    if count == 0 and b == "h":
        FinalWords.append(b)
        count +=1 
    elif count == 1 and b == "e":
        FinalWords.append(b)
        count +=1
    elif count == 2 and b == "l":
        FinalWords.append(b)
        count +=1
    elif count == 3 and b == "l":
        FinalWords.append(b)
        count +=1 
    elif count == 4 and b == "o":
        FinalWords.append(b)
        count +=1
    else:
        continue


if FinalWords == ["h", "e", "l", "l","o"]:
    print("YES")
else:
    print("NO")