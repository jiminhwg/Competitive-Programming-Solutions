WordNumber = int(input())
lst = []
for a in range(WordNumber):
    Words = input()
    if len(Words) > 10:
        lst.append(Words[0] + str(len(Words)-2) + Words[-1])
    else:
        lst.append(Words)

print(*lst, sep = "\n")
        


