userName = input("Enter your name here : ")
print(f"Hello {userName} we will play hangman for sake of learning ! ")

myWord = "Cyber" +"Security"
myList = list()
life = 10
usrWord = ""
for x in myWord:
    myList.append(x)

while life > 0:
    character_left = 0
    for i in myList:
        if i in usrWord:
            print(i)
        else:
            print("-")
            character_left += 1

    if character_left == 0:
        print("You Won!")
        break

    usrGuess = input("Guess a letter:")
    if usrGuess in myList:
        print("Great ! ")
        usrWord += usrGuess
    else:
        life -= 1
        print(f"Try again you have {life} left")
        if life == 0:
            print("You Died ! ")
