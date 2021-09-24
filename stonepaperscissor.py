import random
def game():
    # x = int(input("Enter the number of rounds"))

    answer = input("What do you choose Rock 'r' or Paper 'p' or Scissor 's'?")
    comp_ans = random.choice(['r', 'p', 's'])
    if answer == comp_ans:
        print("That's a tie.")
    elif answer == 'r' and comp_ans == 's' or answer == 's' and comp_ans == 'p' or answer == 'p' and comp_ans == 'r':
        print(f"The computer played {comp_ans}, so you WIN!!")
    else:
        print(f"The computer played {comp_ans}, hence You Lose!")

game()