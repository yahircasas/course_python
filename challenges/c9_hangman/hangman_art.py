import random

# Lista de logos para adivinar
logos = [
    "PYTHON",
    "JAVA",
    "JAVASCRIPT",
    "HTML",
    "CSS",
    "RUBY",
    "PHP",
    "GO",
    "SWIFT",
    "KOTLIN",
    "PERL",
    "RUST"
]

# Lista de etapas del ahorcado
stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

def choose_logo():
    return random.choice(logos).upper()

def display_logo(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

def display_hangman(mistakes):
    print(stages[mistakes])

def hangman():
    logo_to_guess = choose_logo()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(stages) - 1

    print("Welcome to Hangman - Guess the Programming Language Logo!")
    display_logo(logo_to_guess, guessed_letters)

    while True:
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        elif guess not in logo_to_guess:
            mistakes += 1
            display_hangman(mistakes)
        guessed_letters.append(guess)

        display_logo(logo_to_guess, guessed_letters)

        # Verificar si todas las letras del logo han sido adivinadas
        if all(letter in guessed_letters for letter in logo_to_guess):
            print(f"Congratulations! You guessed the logo '{logo_to_guess}' correctly.")
            break

        if mistakes == max_mistakes:
            print(f"Sorry, you ran out of guesses. The logo was '{logo_to_guess}'.")
            break

if __name__ == "__main__":
    hangman()
