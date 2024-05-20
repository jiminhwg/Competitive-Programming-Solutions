Number = int(input())
lst = []
for a in range(1, Number + 1):
    if a % 2 != 0 and a == Number:
        lst.append("I hate it")
        continue
    elif a % 2 != 0 and a != Number:
        lst.append("I hate that")
        continue
    elif a % 2 == 0 and a == Number:
        lst.append("I love it")
        continue
    elif a % 2 == 0 and a != Number:
        lst.append("I love that")
        continue

lstToStr = ' '.join(map(str, lst))

print(lstToStr)
    
