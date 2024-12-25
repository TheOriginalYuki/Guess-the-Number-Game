import random

def guess_game():
    count = 0
    play = True
    number = random.randint(1,100)
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    while play:
        try:
            count += 1
            user_input = int(input("Please guess a number between 1-100: "))
            if(user_input == number):
                print("Correct!\n")
                print("Amount of times you've guessed:", count)
                continue_playing = input("Do you wish to continue to play? Yes or No:").strip().lower()
                if continue_playing == "no":
                    play = False
                else:
                    count = 0
                    number = random.randint(1, 100)
            elif user_input < number :
                print("Too Low!")
            elif( user_input > number):
                print("Too High!")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.\n")



if __name__ == "__main__":
    guess_game()