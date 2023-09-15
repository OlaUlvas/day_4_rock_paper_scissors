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



import random

print("\nWelcome to Rock Paper Scissors!")

computer_score = 0
my_score = 0
game_on = True
while game_on:



    if my_score < 10 and computer_score < 10:

        my_choice = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
        print("My Choice")
        if my_choice == 0:
            print(rock)
        elif my_choice == 1:
            print(paper)
        else:
            print(scissors)
        computer_choice = random.randint(0, 2)
        print("Computers Choice")
        if computer_choice == 0:
            print(rock)
        elif computer_choice == 1:
            print(paper)
        else:
            print(scissors)



        if my_choice == 0 and computer_choice == 1:
            print("One point to the Computer.")
            computer_score += 1
        elif my_choice == 0 and computer_choice == 2:
            print("Yeah - One point to the Me.")
            my_score += 1
        elif my_choice == 1 and computer_choice == 0:
            print("Yeah - One point to the Me.")
            my_score += 1
        elif my_choice == 1 and computer_choice == 2:
            print("One point to the Computer.")
            computer_score += 1
        elif my_choice == 2 and computer_choice == 0:
            print("One point to the Computer.")
            computer_score += 1
        elif my_choice == 2 and computer_choice == 1:
            print("Yeah - One point to the Me.")
            my_score += 1
        else:
            print("It's a draw.")


    else:
        if my_score == 10:
            print(f"\nCongratulation you won by {my_score} - {computer_score}.")
        elif computer_score == 10:
            print(f"You lost by {my_score} - {computer_score}.")
        game_on = False

