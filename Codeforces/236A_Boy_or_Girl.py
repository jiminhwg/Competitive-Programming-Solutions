Username = input()
NewUsername = "".join(set(Username))
print(NewUsername)
if len(NewUsername) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")