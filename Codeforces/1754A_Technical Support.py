n = int(input())

Answers = []

for a in range(0,n):
    conversation_count = int(input()) #number of char in string
    conversation = list(input()) #string
    loopcount = 0
    while loopcount < conversation_count+1: #QAQQAQAAQQQAAA
        if conversation[loopcount] == "Q": #if it is a question 
            loopcount +=1
            if conversation[loopcount] == "A": #if it follows an answer
                continue
            elif conversation[loopcount] == "Q": #if it follows another question
                break
        

        



            

    """if Acount == Qcount:
        Answers.append("Yes")
    elif Acount > Qcount:
        Answers.append("Yes")
    elif Acount < Qcount:
        Answers.append("No")"""

