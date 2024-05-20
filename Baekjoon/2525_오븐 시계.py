hour, minute = map(int,input().split())
add = int(input())

sum_of_minutes = add+minute

if sum_of_minutes < 60:
    print(hour,add+minute)

elif sum_of_minutes >= 60:
    print((hour+(sum_of_minutes//60))%24, sum_of_minutes%60)
