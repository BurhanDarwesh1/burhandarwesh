import random
i = 0
mylist = ["snake", "water", "gun"]
userWin = 0
userLose = 0
systemWin = 0
systemLose = 0
sameChoice = 0
print("This is snake water game:choose 'snake', 'water' and 'gun' ")
while(i <= 10):
    random.shuffle(mylist)
    systemChoice = random.choice(mylist)
    userChoice = input("Enter your choice:")
    c = f"you choose {userChoice}"
    if systemChoice == "snake" and userChoice.lower() == "water":
        print(c)
        print("Sorry you lose the game because snake drinks the water")
        systemWin = systemWin + 1
        userLose = userLose + 1
    elif systemChoice == "water" and userChoice.lower() == "snake":
        print(c)
        print("Hurry..! your won the game because snake drinks the water")
        userWin = userWin + 1
        systemLose = systemLose + 1

    elif systemChoice == "gun" and userChoice.lower() == "snake":
        print(c)
        print("Sorry you lose the game because Gun kills the snake")
        systemWin = systemWin + 1
        userLose = userLose + 1

    elif systemChoice == "snake" and userChoice.lower() == "gun":
        print(c)
        print("Hurry..! your won the game because gun kills the snake")
        userWin = userWin + 1
        systemLose = systemLose + 1

    elif systemChoice == "water" and userChoice.lower() == "gun":
        print(c)
        print("Sorry you lose the game because gun drown in water")
        systemWin = systemWin + 1
        userLose = userLose + 1
    elif systemChoice == "gun" and userChoice.lower() == "water":
        print(c)
        print("Hurry..! your won the game because gun drown in water")
        userWin = userWin + 1
        systemLose = systemLose + 1

    elif systemChoice == "snake" and userChoice.lower() == "snake":
        print(c)
        print("Match draw because both player choices are same")
        sameChoice = sameChoice + 1
    elif systemChoice == "water" and userChoice.lower() == "water":
        print(c)
        print("Match draw because both player choices are same")
        sameChoice = sameChoice + 1
    elif systemChoice == "gun" and userChoice.lower() == "gun":
        print(c)
        print("Match draw because both player choices are same")
        sameChoice = sameChoice + 1
    else:
        print("Your entered invalid choice:please try again!")
    i= i + 1

print(" System lose:", str(systemLose) + " times")
print(" System Wins:", str(systemWin) + " times")
print(" User lose:", str(userLose) + " times")
print(" User Wins:", str(userWin) + " times")
print(" Match Draw due to same choices:", str(sameChoice) + " times")
