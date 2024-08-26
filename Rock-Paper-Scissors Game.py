                               # Rock-Paper-Scissors Game
import random
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'+ "Rock vs Paper -> Paper wins \n"+ "Rock vs Scissors -> Rock wins \n"+ "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # input from user
    userchoice = int(input("Enter your choice :"))

    #loop until user enter invalid input
    while userchoice > 3 or userchoice < 1:
        userchoice = int(input('Enter a valid choice please '))

    #initializing the value of users
    if userchoice == 1:
        choice_name = 'Rock'
    elif userchoice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # print user choice
    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')
    
    #computer choose any random number between 1 to 3
    comp_choice = random.randint(1, 3)
    while comp_choice == userchoice:
        comp_choice = random.randint(1, 3)
    # initializing the value of computer
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    #checking for draw 
    if (userchoice == comp_choice):
        print('Its a Draw', end="")
        result = "DRAW"
        
    #condition for winning
    if (userchoice == 1 and comp_choice == 2):
        print('paper wins =>\n', end="")
        result = 'Paper'
        
    elif (userchoice == 2 and comp_choice == 1):
        print('paper wins =>\n', end="")
        result = 'Paper'

    if (userchoice == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
        
    elif (userchoice == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'Rock'

    if (userchoice == 2 and comp_choice == 3):
        print('Scissors wins =>\n', end="")
        result = 'Scissors'
        
    elif (userchoice == 3 and comp_choice == 2):
        print('Scissors wins =>\n', end="")
        result = 'Scissors'
     
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    
    res = input().lower()
    if res == 'n':
        break
print("Thank you for playing")
