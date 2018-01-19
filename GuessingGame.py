import random

name = input("Enter your name: ")
print("Hello, " + name + "!")
print("Let's play a guessing game 3 times.")
done = False

total_guesses = 0
while not done:
    for i in range(1, 4):
        print("Game ", i)
        answer = random.randint(1, 10)
        guess = 0
        guesses_this_round = 0
    
        while guess != answer:
            while True:
                try:
                    guess = int(input("Pick a number from 1-10. (-1 to quit): "))
                except ValueError:
                    print("Invalid input")
                    continue
                if guess < -1 or guess > 10:
                    print("Sorry, the number must be from 1-10.")
                    continue
                else:
                    guesses_this_round = guesses_this_round + 1
                    break  
            if guess == -1:
                break
            elif guess < answer:
                print("Too low!")
            elif guess > answer:
                print("Too high!")
            else:
                print("That's right!")
                print("It took you " + str(guesses_this_round) + " guesses!")
                total_guesses = guesses_this_round
        if guess == -1:
            print("Thanks for playing!")
            break
    if guess != -1:
        print("You finished all of the games!")
        print("It took you about " + str(total_guesses / 3) + " guesses to figure it out on average!")
    play_again = input("Do you want to play again [y/n]: ")
    if play_again == "n":
        done = True
    
print("Goodbye")
        
