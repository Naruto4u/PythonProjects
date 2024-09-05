import random
word_list = ['performer', 'crackpot', 'combination', 'expertise', 'mourning', 'secretary', 'broccoli', 'health','outfit', 'timber', 'receipt', 'star', 'domestic', 'large', 'irony', 'root', 'building', 'laser','far', 'swim', 'lunch', 'budge', 'acceptable', 'tiptoe', 'museum', 'familiar', 'science', 'corruption','enlarge', 'musical', 'reliable', 'bite', 'rest', 'heel', 'atmosphere', 'secure', 'evoke', 'consolidate','modernize', 'joke', 'liability', 'enthusiasm', 'aspect', 'tendency', 'crime', 'hostile', 'orbit','ballet', 'clarify', 'stable']
random_word = "combination"
# For testing purposes, using a fixed word. When ready, replace with:
#random_word = random.choice(word_list)
# Create a string of underscores (with spaces in between for readability) to represent the word
wrd_holder = ' '.join("_" * len(random_word))

# Convert the underscore string into a list for easier modification
list_holder = list(wrd_holder)

# To keep track of guessed positions

# Number of guesses the user is allowed
attempts_remaining = 5

# Main game loop - keeps running until the user runs out of attempts
while attempts_remaining > 0:
    print(f"Current guess: {wrd_holder}")  # Show current state of the word to the user
    usr_input = input("Please guess a letter: ")

    # Initialize the index to search for the letter
    index = random_word.find(usr_input)

    if index != -1:
        # If the guessed letter is found, loop to find and update all occurrences of the letter
        while index != -1:
            # Store index where the letter was found
            index *= 2
            # Update the list_holder at the correct position with the guessed letter
            list_holder[index] = usr_input

            # Search for the next occurrence of the letter
            index = random_word.find(usr_input, index + 1)

        # Convert the list_holder back to a string to show progress to the user
        wrd_holder = ''.join(list_holder)
    else:
        # If the letter is not found, notify the user and decrement the attempts
        print(f"Wrong letter! {attempts_remaining - 1} attempts left.")
        attempts_remaining -= 1

# Final state of the game
print("Final word guess: ", wrd_holder)
print(random_word)
