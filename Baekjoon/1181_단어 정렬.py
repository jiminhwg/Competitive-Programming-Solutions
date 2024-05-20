words = []
finalwords = []
for a in range(0,int(input())):
    words.append(input())

words = [*set(words)]
words.sort()
words.sort(key=len)
for b in words:
    print(b)