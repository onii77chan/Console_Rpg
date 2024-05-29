from scrapers.rpg_data_scraping import what_is_rpg_text

start_menu = {
    '1': 'Welcome', '2': what_is_rpg_text
}


def user_input():
    while True:
        try:
            user_input_data = int(input(": "))
            return str(user_input_data)
        except ValueError:
            print('ОШИБКА!!! Напоминаем, что вводить можно только цифры.\n'
                  'но иногда можно и числа:) ознакомьтесь с возможными\n'
                  'на данный момент действиями и повторите попытку с новыми силами')


def main():
    user_choice = user_input()
    try:
        if user_choice in start_menu:
            start_menu[user_choice]()

    except TypeError:
        print('ОШИБКА!!! возможно вы ввели чтото не так\n'
              'посмотрите еще раз список доступных вариантов\n'
              'и повторите попытку еще раз:)))\n'
              'НО если ничего не изменилось то ждите обновлений')
