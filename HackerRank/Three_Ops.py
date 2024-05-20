A = input()
B = int(input())
C = int(input())

if A == '0':
    print(abs(B-C))
elif '-' in A:
    print(min(B,C)) 
elif '-' not in A:
    print(max(B,C))
    