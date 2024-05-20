Hour, Minute = map(int, input().split())

if Minute >= 45:
    if Minute - 45 < 10:
        print(Hour, Minute-45)
    else:
        print(Hour, Minute-45)

else:
    if Hour == 0:
        Hour = 23
    else:
        Hour = Hour - 1
    Difference = abs(Minute - 45)
    print(Hour, 60-Difference)


