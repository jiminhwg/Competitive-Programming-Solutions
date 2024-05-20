#lst = list(input().split())
#lst = [int(i) for i in lst]
#number = int(input())

#ranges = list(range(number))
#ranges.reverse()

#for a in ranges: 
#    del (lst[a])

#print(lst)

lst = list(input().split())
lst = [int(i) for i in lst]
number = int(input())

for a in range(number-1, -1, -1): 
    del (lst[a])
print(lst)
