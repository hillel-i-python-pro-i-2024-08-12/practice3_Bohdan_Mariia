from words_game.game import game
from utils.util_functions import read_data, write_data
from spellchecker import SpellChecker

def main():
    words = read_data()

    if len(words) == 0:
        print("Добро пожаловать в игру в слова, пожалуйста введите первое слово")

        spell = SpellChecker(language='ru')

        while True:
            first_word = input("Введите первое слово (или 0 чтобы выйти): ").strip().lower()

            if first_word == '0':
                print("Игра завершена.")
                break

            if not spell.unknown([first_word]):
                words.append(first_word)
                write_data(first_word)
                print(f'Вы ввели первое слово: {first_word}. Начинаем игру!')
                game(words)
                break
            else:
                print("Первое слово некорректно или не существует, попробуйте снова.")
    else:
        game(words)


if __name__ == "__main__":
    main()