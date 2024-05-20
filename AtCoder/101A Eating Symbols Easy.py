S = input()
count = 0 

for n in range(len(S)):
    if S[n] == '+':
        count+=1
    else:
        count-=1
print(count)