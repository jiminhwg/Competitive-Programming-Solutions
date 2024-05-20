lst = []
Rows, Column = map(int, input().split())

for a in range(Rows):
    b = list(input().split())
    lst.append(b[Column-1])

lst = [int(i) for i in lst]
print(lst)

