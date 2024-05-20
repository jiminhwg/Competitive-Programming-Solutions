from fractions import Fraction
Yakko, Wakko = map(int, input().split())

Yakkolst = []
Wakkolst = []
lst = []

for a in range(1,7):
    lst.append(a)

if Yakko > Wakko:
    for a in range(1,Yakko):
        Yakkolst.append(a)
    Answer = list(set(lst) - set(Yakkolst))
    fraction = Fraction(len(Answer), 6)
    if fraction == 0:
        print("0/1")
    elif fraction == 1:
        print("1/1")
    else:
        print(fraction)

else:
    for a in range(1,Wakko):
        Wakkolst.append(a)
    Answer = list(set(lst) - set(Wakkolst))
    fraction = Fraction(len(Answer), 6)
    if fraction == 0:
        print("0/1")
    elif fraction == 1:
        print("1/1")
    else:
        print(fraction)

    