A = list(input().split())
A = [int(i) for i in A]
count = 0
for a in A:
    if a%2 ==0:
        count += 1
    else:
        print("False")
        break
if count == len(A):
    print("True")

