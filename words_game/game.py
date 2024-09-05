from utils.util_functions import read_data, write_data
from spellchecker import SpellChecker

def game(words):
    spell = SpellChecker(language='ru')
    while True:
        last_word = words[-1]
        print("Последнее слово:", last_word)
        answer = input('Введите слово (или 0 чтобы выйти):').strip().lower()

        if answer == '0':
            print(f'Вы вышли из игры. Количество слов: {len(words)}')
            break

        if answer[0] == last_word.rstrip('ьъы')[-1]:

            if not spell.unknown([answer]):
                if answer not in words:
                    words.append(answer)
                    write_data(answer)
                    # chosen_word = next((word for word in spell if word.startswith(answer.rstrip('ьъы')[-1]) and word not in words), None)
                    #
                    # print("cccc", chosen_word)
                    # write_data(chosen_word)
                else:
                    print('Такое слово уже есть в списке.')
            else:
                print('Такого слова нет в словаре.')
        else:
            print('Не та буква.')

