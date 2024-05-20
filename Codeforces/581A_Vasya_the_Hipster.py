Red, Blue = map(int, input().split())

if Red < Blue:
    NewRed = Red - Red
    NewBlue = Blue - Red
    print(Red, NewBlue//2)

else:
    NewRed = Red - Blue
    NewBlue = Blue - Blue
    print(Blue, NewRed//2)
    