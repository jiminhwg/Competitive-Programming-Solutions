String = list(input())

for a in String:
    if a == "+":
        String.remove(a)

count = 0
String.sort()

for b in String:
    print(b, end ="")
    count += 1
    if len(String) == count:
        break
    else:
        print("+", end="")


