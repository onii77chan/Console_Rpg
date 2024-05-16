class RPG:
    def __init__(self, heroes: [], boss: [], mobs: []):
        self.heroes = heroes
        self.boss = boss
        self.mobs = mobs

    def companions(self):
        choice_heroes = input("Выберите команду из 4 человек (список героев сверху).\n"
                              "Пример выбора героев: 1,3,4,9: ")
        indices = [int(index) for index in choice_heroes.split(',') if index.strip().isdigit()]
        if len(indices) == 4:
            selected_heroes = [self.heroes[index - 1] for index in indices if 0 < index <= len(self.heroes)]
            return selected_heroes
        else:
            return ('\n\n------------------------------------------------------------------------------------\n'
                    'Пожалуйста, выберите 4 героя.\n'
                    '[пусто]\n'
                    '------------------------------------------------------------------------------------\n\n')


rpg_game = RPG(['Герой1', 'Герой2', 'Герой3', 'Герой4', 'Герой5'], [], [])
selected_companions = rpg_game.companions()
print("Выбранные спутники:", selected_companions)
