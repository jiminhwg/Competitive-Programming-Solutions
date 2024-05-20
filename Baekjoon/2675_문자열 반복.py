List = []
for a in range(0, int(input())):
    number, letters = input().split()
    List.append(''.join([char*int(number) for char in letters]))

for b in List:
    print(b)


