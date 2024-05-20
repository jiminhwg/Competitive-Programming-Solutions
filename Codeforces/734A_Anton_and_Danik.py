NumberOfGames = int(input())

Results = list(input())

if Results.count("A") > Results.count("D"):
    print('Anton')
elif Results.count("A") == Results.count("D"):
    print("Friendship")
else:
    print("Danik")