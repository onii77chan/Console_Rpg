
"""функция main_menu принимает в себя методы такие как (начать игру, настройки, помощь и выйти из игры
 а также метод который принимает выбор пользователя и на основе этого через условие запускаются методы.

 насчёт последнего elif конечно можно было бы поставить условие по короче например:
 q == user_input_data == quit or user_input_data == quit, но тогда ракция только на quit"""


def main_menu(user_input_data, start_game_method, settings_method, help_method):
    if user_input_data == '1':
        start_game_method()
        return False
    elif user_input_data == '2':
        settings_method()
        return False
    elif user_input_data == '3':
        help_method()
        return False
    elif 'q' == user_input_data or user_input_data == 'quit' or user_input_data == 'exit':
        print('Bye bye!')
        exit()
    else:
        print('Возможно вы ввели чтото не так попробуйте еще раз')
        return True


def settings_menu():
    pass


def help_menu():
    pass
