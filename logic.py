
from game_components.main_menu import (
    settings_menu,
    help_menu,

)
from texts import (
    welcome_text,
    main_menu_text,
    separation_of_the_text,

)
from config import (
    PlayerTeam,

)

from game_components.main_menu import (
    main_menu,

)
from characters.heroes import (
    all_heroes,
    view_all_heroes,
    view_hero_information,

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


def player_actions(input_data):
    if input_data == '1':
        pass


def start_game():
    player_team = PlayerTeam([])

    print('Здравствуй, Странник! Пора в путь, но для этого тебе понадобится команда.\n'
          'Важное уточнение: можно взять только от 1 до 4 героев, не меньше и не больше. Удачи! :)\n'
          'Ниже представлен список всех доступных на данный момент героев:\n')
    view_all_heroes(all_heroes)

    main_loop = True
    iscommand = True
    while main_loop:
        if iscommand:
            command = player_team.assembly_of_the_team(team=player_team.choice_teamates(), all_heroes=all_heroes)
            iscommand = False
        print('чтоже вы определились с выбором команды, какие теперь будут указания?\n'
              'Продолжить путь(1)/Посмотреть информацию о герое(2)/Посмотреть информацию о всех героях(3)/Выйти(4)\n',
              user_input())


def main():
    print(welcome_text, f'\n{separation_of_the_text}',
          '\n', main_menu_text, f'\n{separation_of_the_text}')

    main_menu(user_input(), start_game, settings_menu, help_menu)
