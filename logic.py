
from texts import (
    welcome_text,
    main_menu_text,
    separation_of_the_text,

)

from game_components.main_menu import (
    main_menu,

)
from characters.heroes import (
    all_heroes,
    view_all_heroes

)

"""Ну впринципе тут можно было обойтись и без создания функции но я подумал
 а почему бы и нет к тому же функция вызываемая и её будет легче отслеживать"""


def user_input():
    user_input_data = None
    try:
        user_input_data = input("\nВвод:")
    except ValueError:
        print('Произошла ошибка проверьте правильно ли вы ввели данные')

    return user_input_data


def start_game():
    print('Здравствуй Странник чтоже пора в путь но для это этого тебе понадобиться команда\n'
          'Важное уточнение взять можно только от 1 до 4 героев не меньше не больше удачи! :)\n'
          'ниже представлен список всех доступных на данный момент героев:\n')
    view_all_heroes(all_heroes)

    main_loop = True
    while main_loop:
        pass


def main():
    print(welcome_text, f'\n{separation_of_the_text}',
          '\n', main_menu_text, f'\n{separation_of_the_text}')

    main_menu(user_input(), start_game())


if __name__ == '__main__':
    main()
