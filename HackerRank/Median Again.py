A = list(input().split())
A = [int(x) for x in A]
A.sort()

if len(A)%2 != 0:
    Number = len(A)//2 
    print(A[Number])

elif len(A)%2 == 0:
    Number1 = len(A)//2 - 1
    Number2 = len(A)//2 
    print((A[Number1] + A[Number2])/2)
   
