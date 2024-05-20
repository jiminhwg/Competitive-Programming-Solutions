Number = int(input())
Numbers = list(input().split())
Numbers = [int(x) for x in Numbers]

print(str(min(Numbers)) + " " + str(max(Numbers)))
