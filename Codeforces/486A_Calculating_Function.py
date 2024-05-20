Number = int(input())
#if number is even, print its half
if Number % 2 == 0:
    print(Number//2)
#if number is odd, print its (half + 1)*(-1)
else:
    print((Number//2 +1) * (-1))

