#nOT FINISHED
n = int(input())
numbers = input().split()
numbers = [int(x) for x in numbers]

count = 0

for a in numbers:
    if a <= 1:
        continue
    else: #a is greater than 1
        if a == 2:
            count +=1
        elif a%2 == 0: #even number
            continue
        else:

                count +=1
print(count)

