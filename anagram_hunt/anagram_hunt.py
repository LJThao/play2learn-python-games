"""Anagram Hunt Game"""
# Import modules
import time
import random
from anagram_data import anagrams


def select_word(length):
    """Randomly selects a word length"""
    word_set = anagrams.get(length, [])
    if word_set:
        return random.choice(word_set)
    return None

def anagram_game():
    """Start the Anagram Hunt Game"""
    print("Let's start the Anagram Hunt Game!")

    # Word length prompt
    while True:
        try:
            word_length = int(input("Please enter a word length [5, 6, 7, 8]: "))
            if word_length in anagrams:
                break
            print("This is not the correct word length. Please try again [5, 6, 7, 8]:")
        except ValueError:
            print("Please try again and enter a number.")

    # Select a word and display details
    word_list = select_word(word_length)
    if not word_list:
        print("No words found for that length.")
        return

    original_word = word_list[0]
    remaining_anagrams = set(word_list[1:])
    # Tracking the guessed words
    guessed_anagrams = set()

    print(f"The word is: {original_word.upper()}")
    print(f"There are {len(remaining_anagrams)} unguessed anagrams.")
    print("You have 60 seconds left.")

    # The 60 second timer
    start_time = time.time()
    time_limit = 60
    score = 0

    while time.time() - start_time < time_limit:
        remaining_time = int(time_limit - (time.time() - start_time))

        guess = input("Make a guess: ").strip().lower()

        # Checks remaining time
        if remaining_time <= 0:
            print("Time is up!")
            print("Sorry, you didn't get that last one in on time.")
            print(f"You got {score} anagrams for {word_length}-letter words!")
            input("Press Enter to play again.")
            return

        if guess in guessed_anagrams:
            print(f"You already got {guess.upper()}. Try again.")

        elif guess in remaining_anagrams:
            print(f"{guess.upper()} is correct!")
            guessed_anagrams.add(guess)
            remaining_anagrams.remove(guess)
            score += 1

            # Checks if all anagrams were guessed then chooses a new word
            if not remaining_anagrams:
                print(f"You got all the anagrams for {original_word.upper()}!")
                word_list = select_word(word_length)
                if word_list:
                    original_word = word_list[0]
                    remaining_anagrams = set(word_list[1:])
                    guessed_anagrams.clear()
                    print(f"The word is: {original_word.upper()}")
                    print(f"There are {len(remaining_anagrams)} unguessed anagrams.")
                    continue
                print(f"No more words available for {word_length}-letter words!")
                break
        else:
            print(f"{guess.upper()} is not a valid anagram. Please try again.")

        # Game status
        print(f"The word is: {original_word.upper()}")
        print(f"There are {len(remaining_anagrams)} unguessed anagrams.")
        print(f"You have {remaining_time} seconds left.")

    # Time's up display message
    print(f"Time's up!\nYou got {score} anagrams for {word_length}-letter words!")

    # Play again or exit
    if input("Press Enter to play again or any other key to exit: ").strip() == '':
        anagram_game()


if __name__ == "__main__":
    anagram_game()
