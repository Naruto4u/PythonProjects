
attempts_remaining = 10
incorrect_guess_holder = []
def game_restart():
    global attempts_remaining
    global incorrect_guess_holder
    start_again = input("Do you want to play again?")
    if start_again.lower() in ("yes", "y"):
        attempts_remaining = 10
        incorrect_guess_holder = []
        play_game()
    else:
        raise SystemExit("Goodbye!")
def play_game():
    import random
    word_list = ['performer', 'crackpot', 'combination', 'expertise', 'mourning', 'secretary', 'broccoli', 'health','outfit', 'timber', 'receipt', 'star', 'domestic', 'large', 'irony', 'root', 'building', 'laser','far', 'swim', 'lunch', 'budge', 'acceptable', 'tiptoe', 'museum', 'familiar', 'science', 'corruption','enlarge', 'musical', 'reliable', 'bite', 'rest', 'heel', 'atmosphere', 'secure', 'evoke','consolidate', 'modernize', 'joke', 'liability', 'enthusiasm', 'aspect', 'tendency', 'crime','hostile', 'orbit', 'ballet', 'clarify', 'stable']
    random_word = "performer"#random.choice(word_list)
    wrd_holder = ''.join("_" * len(random_word))
    # Create a string of underscores (with spaces in between for readability) to represent the word

    list_holder = list(wrd_holder)
    # Convert the underscore string into a list for easier modification

    # To keep track of incorrect guesses
    global attempts_remaining
    global incorrect_guess_holder
    # Number of guesses the user is allowed
    while attempts_remaining > 0:
        # Main game loop - keeps running until the user runs out of guesses and exits
        wrd_holder_printed = " ".join(wrd_holder)
        print(f"Current guess: {wrd_holder_printed}")  # Show current state of the word to the user

        if not incorrect_guess_holder:
            pass #No current incorrect guesses
        else: print(f"Incorrect guesses: {incorrect_guess_holder}")
        usr_input = input("Please guess a letter: ").strip().lower()
        if len(usr_input) > 1:
            print("----------------------------")
            print("\033[31mPlease only type one letter\033[0m")
            print("----------------------------")
            continue
        elif usr_input == "":
            print("-----------------------")
            print("\033[31mPlease input something\033[0m")
            print("-----------------------")
            continue
        elif usr_input in incorrect_guess_holder:
            print("-------------------------------------")
            print("\033[31mYou have already guessed that letter\033[0m")
            print("-------------------------------------")
            continue
        index = random_word.find(usr_input)
        # Initialize the index to search for the letter

        if index != -1:
            # If the guessed letter is found, loop to find and update all occurrences of the letter
            while index != -1:
                # Update the list_holder at the correct position with the guessed letter
                list_holder[index] = usr_input
                # Search for the next occurrence of the letter
                index = random_word.find(usr_input, index + 1)

            # Convert the list_holder back to a string to show progress to the user
            wrd_holder = ''.join(list_holder)
            print("--------------------------------------")
            print(f"{attempts_remaining} attempts left.")
            print("--------------------------------------")
        else:
            incorrect_guess_holder.append(usr_input)
            # If the letter is not found, notify the user and decrement the attempts
            print("--------------------------------------")
            print(f"Wrong letter! {attempts_remaining - 1} attempts left.")
            print("--------------------------------------")
            attempts_remaining -= 1
        won_game = wrd_holder.replace(" ", "")
        if won_game == random_word:
            print("\033[32mGame Won!\033[0m")
            game_restart()
        if attempts_remaining == 0:
            game_restart()

    print("Final word guess: ", wrd_holder)
    print(random_word)
try_count = 0
while True:
    if try_count == 5:
        raise SystemExit("Really?")
    gamestart = input("Start Game?")
    if gamestart.lower() in ("yes", "y"):
        play_game()
        break
    elif gamestart.lower() in ("no", "n"):
        raise SystemExit("Goodbye!")
    else:
        print("Invalid input! Yes or No")
        try_count += 1
