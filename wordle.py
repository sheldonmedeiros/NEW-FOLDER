secret_word = "drive"
guess_is_correct =  False
guess_count = 0

while guess_is_correct == False: 
    user_guess = input("what is your guess? ")
    guess_count += 1 
    if user_guess == secret_word: 
        guess_is_correct = True 
    else: 
        print("your guess is not correct. ")

print("Congrats you guessed it.")
print(f"Guess Count: {guess_count}")        