N, A, B = map(int, input().split())

partA = (N//(A+B))*A
partB = min([N % (A+B), A])
print(partA+partB)
