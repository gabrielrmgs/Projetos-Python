import random
from words import words
import string
from visual_dict import lives_visual_dict


def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print(f"Você tem {lives} vidas, e você ja usou as letra :{used_letters}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Letras correspondentes: ', ' '.join(word_list))

        user_letter = input('Escreva: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letra errada!")

        elif user_letter in used_letters:
            print("Letra já usada, tente outra!")

        else:
            print("Inválido, tente outro!")
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Você morreu!, a palavra era ', word, '!!')
    else:
        print("Você descobriu a palavra", word)

hangman()


