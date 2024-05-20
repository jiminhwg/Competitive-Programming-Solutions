from collections import Counter

List = []
Word = Counter(input().upper())
for a in Word:
    List.append(Word[a])

if List.count(max(List)) > 1:
    print("?")
else:
    print(max(Word, key = Word.get))
