Word = str(input())

count = 0
for a in Word:
    if a.isupper():
        count = count +1

count2 = 0
for b in Word:
    if b.islower():
        count2 = count2 + 1

if count > count2:
    print(Word.upper())
else:
    print(Word.lower())