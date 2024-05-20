s, e, t = map(int, input().split())

if abs(s-e) <= t and (t-abs(s-e))%2==0:
    print("YES")
else:
    print("NO")
