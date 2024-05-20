A = int(input())

def multiples(x):
    lst = []
    for a in range(1,11):
        lst.append(x*a)
    return lst

print(multiples(A))