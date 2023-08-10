import random
import hangManStages
import hangManWords
# Build hangMan

# 1.1 randomly choose a word from the word_list and assign it to a variable
# called chosen_word
# 1.2 ask the user to guess a letter and assign their answer to a variable called guess.
# Make guess lowercase
# 2.1 create an empty List called display
# For each letter in the chosen_word, add a "_" to display list

chosen_word = random.choice(hangManWords.word_list)
display = []
chosen_word = chosen_word.lower()
for letter in chosen_word:
    display.append("_")
print(f"Shh! The word is {chosen_word}")
# 1.3 Check if the letter the user guessed is one of the letters in the chosen_word
# 2.3 Loop through each position in the chosen_word; If the letter at that position
# matches the guess then reveal the letter in the display at that position
# 3.1 Use a while loop to let the user guess again. The loop should only stop
# the user has guessed all the letters in the chosen_word and display has no more blanks
# Then, you can tell the user they won
# 4.1 create a variable named life which is equal to 6
# reduce lives by one if the chosen word is incorrect, if lives = 0 -> you lost

blank_count = len(display)
lives = 6
while blank_count > 0 and lives >0:
    guess = input("guess a letter from the word: ").lower()
    for letter_position in range(len(chosen_word)):
        if chosen_word[letter_position] == guess:
            display[letter_position] = guess
            blank_count -= 1
    if guess not in chosen_word:
        lives -= 1
    formatted_display = ' '.join(display)
    print(formatted_display)
    print(hangManStages.stages[lives])
    print(f"Lives: {lives}")
    if blank_count == 0:
        print("You won!")
    if lives == 0:
        print("You lost!")
