n = int(input())
Answers = []
for a in range(n):
    word = input()
    if word.lower() == "yes":
        Answers.append("YES")
    else:
        Answers.append("NO")

for b in Answers:
    print(b)
    