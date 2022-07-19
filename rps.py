#!/usr/bin/python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

npc_rps = ['Rock', 'Paper', 'Scissors']

while True:

    rock_paper_sci = ['Rock', 'Paper', 'Scissors',"r", "R", "s", "S", "p", "P", 'rock', 'scissors', 'paper']
    npcChoice = random.choice(npc_rps)
    playerchoice = input('Rock, Paper or scissors? ')

    while playerchoice not in rock_paper_sci:
        playerchoice = input("That is not a valid choice. Please try again: ").lower()

    
    print("Your choice:", playerchoice)
    print("Computer's choice:", npcChoice)
    

    if playerchoice == 'Rock' or playerchoice == 'rock' or playerchoice == 'r' or playerchoice == 'R':
        if npcChoice == 'Scissors':
            print(f'You chose Rock, computer chose {npcChoice}\nRock {rock}Smaashes scissors! {scissors} You win!')
        elif npcChoice == 'Paper':
            print(f'''You chose Rock and computer chose {npcChoice}\nPaper {paper}covers Rock! {rock} You lose!''')
        else:
            print(f'''Player chose Rock {rock}computer chose {npcChoice}{rock}\n It's a tie!''')
    elif playerchoice == 'Paper' or playerchoice == 'paper' or playerchoice == 'p' or playerchoice == 'P':
        if npcChoice == 'Scissors':
            print(f'You chose Paper, computer chose {npcChoice}\nscissors {scissors}cuts paper! {paper} You lose!')
        elif npcChoice == 'Rock':
            print(f'''You chose Paper and computer chose {npcChoice}\nPaper {paper}covers Rock! {rock} You win!''')
        else:
            print(f'''Player chose Paper {paper}computer chose {npcChoice}{paper}\n It's a tie!''')
    elif playerchoice == 'Scissors' or playerchoice == 'scissors' or playerchoice == 's' or playerchoice == 'S':
        if npcChoice == 'Paper':
            print(f'''You chose Scissors and computer chose {npcChoice}\nScissors {scissors}Cuts paper! {paper} You win!''')
        elif npcChoice == 'Rock':
            print(f'''You chose Scissors and computer chose {npcChoice}\nRock {rock}Smaashes Scissors {scissors} You lose!''')
        else:
            print(f'''Player chose Scissors {scissors}computer chose {npcChoice}{scissors}\n It's a tie!''')
    else:
        print(f'Please choose\nRock{rock}Paper{paper}or Scissors{scissors}')

    print()

    repeat = input("Play again? (Y/N) ").lower()
    while repeat not in ['y', 'n']:
        repeat = input("That is not a valid choice. Please try again: ").lower()
  
    if repeat == 'n':
        print("Good Bye!")
        break

    