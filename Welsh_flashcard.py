# welsh_flashcard_cli.py
# Simple CLI Flashcard Application

import random

def show_flashcard(glossary, score):
    """
    Displays a random flashcard and checks user knowledge.
    Returns updated score.
    """

    random_key = random.choice(list(glossary.keys()))
    welsh_word = random_key
    english_word = glossary[random_key]

    choice_lang = input("Enter 'w' to see Welsh first or 'e' to see English: ").lower()

    if choice_lang == 'w':
        print(f"\nWelsh word: {welsh_word}")
        answer = input("Do you know the English word? (y/n): ").lower()
        if answer == 'y':
            score += 1
        else:
            print(f"English: {english_word}")

    elif choice_lang == 'e':
        print(f"\nEnglish word: {english_word}")
        answer = input("Do you know the Welsh word? (y/n): ").lower()
        if answer == 'y':
            score += 1
        else:
            print(f"Welsh: {welsh_word}")

    else:
        print("Invalid option. Please choose 'w' or 'e'.")

    return score


def main():
    glossary = {
        'coch': 'red',
        'oren': 'orange',
        'melyn': 'yellow',
        'gwyrdd': 'green',
        'glas': 'blue',
        'fioled': 'violet',
        'du': 'black',
        'gwyn': 'white',
        'amryliw': 'multicoloured'
    }

    total_attempts = 0
    correct_answers = 0

    print("Welcome to the Welsh Colour Flashcard App!")

    while True:
        user_input = input("\nEnter 's' to show a flashcard or 'q' to quit: ").lower()

        if user_input == 'q':
            if total_attempts > 0:
                percentage = (correct_answers / total_attempts) * 100
                print(f"\nFinal Score: {correct_answers}/{total_attempts}")
                print(f"Success Rate: {percentage:.1f}%")
            else:
                print("\nNo flashcards attempted.")
            break

        elif user_input == 's':
            total_attempts += 1
            correct_answers = show_flashcard(glossary, correct_answers)

        else:
            print("Please enter 's' or 'q'.")


if __name__ == "__main__":
    main()
