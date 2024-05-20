lst = list(input().split())
Number = int(input())

lst = [int(x) for x in lst]
lst.sort()
print(lst[-Number])