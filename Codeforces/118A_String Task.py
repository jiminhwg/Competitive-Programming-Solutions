word = list(input())
newword = []
for a in word:
    if a in "AEIOUYaeiouy": #removes vowels
        continue
    else:
        newword.append(a)
for b in newword:
    print(".", end = "")
    print(b.lower(), end = "")
