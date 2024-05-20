count = 0
for a in range(5):
    b = int(input())
    if b < 40:
        count+=40
    else:
        count+=b
print(count//5)
    
