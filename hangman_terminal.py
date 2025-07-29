import random

class WordBank:
    def __init__(self):
        with open("words.txt", 'r') as file:
            self.words = [word.strip() for word in file if word.strip()]

    def get_random_word(self, min_len, max_len):
        valid_words = []
        for word in self.words:
            if min_len <= len(word) <= max_len:
                valid_words.append(word)
        if len(valid_words) == 0:
            print("No valid words found")
            exit(0)
        return random.choice(valid_words)

class HangmanGame:
    def __init__(self, word, lives):
        self.secret_word = word
        self.lives_left = lives
        self.guessed_letters = []
    def masked_word(self):
        masked = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                masked += letter + ""
            else:
                masked += "_"
        return masked.strip()
    def guess_letter(self, letter):
        letter = letter.lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter (A-Z).")
            return
        self.guessed_letters.append(letter)

        if letter in self.secret_word:
            print("You've guessed that letter: " + letter)
        else:
            self.lives_left -= 1
            print("Wrong guess.")
    def end_game(self):
        return self.lives_left == 0 or self.victory()
    def victory(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

def choose_difficulty():
    print("Choose a difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")

    while True:
        difficulty = input("1, 2, or 3: ")

        if difficulty == "1":
            return 3, 5, 8
        elif difficulty == "2":
            return 5, 7, 5
        elif difficulty == "3":
            return 7, 8, 3
        else:
            print("Please enter a valid difficulty.")

def main():
    print("Welcome to Hangman!")
    min_len, max_len, lives = choose_difficulty()
    word_bank = WordBank()
    chosen_word = word_bank.get_random_word(min_len, max_len)
    game = HangmanGame(chosen_word, lives)

    while not game.end_game():
        print("\nWord: " + game.masked_word())
        print("Letters: " + "".join(game.guessed_letters))

        guess = input("Guess a letter: ")
        guess = guess.lower()
        game.guess_letter(guess)

    print("\nThe word was: " + chosen_word)

if __name__ == "__main__":
    main()