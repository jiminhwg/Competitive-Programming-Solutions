n = int(input())
number = n
count = 0

while True:             
    first = number//10 
    last = number%10    
    number = (last*10) + ((first+last)%10)
    
    count += 1
    if number == n:
        print(count)
        break
    else:
        continue
