from effects.races.races_in_game import (
    all_races,

)



class RPG:
    def __init__(self, name, class_of_character, race_of_character):
        self.name = name
        self.class_of_character = class_of_character
        self.race_of_character = race_of_character


class CreateCharacters(RPG):
    def __init__(self, name, class_of_character, race_of_character,
                 health_point: int, mana_point: int, def_point: int, damage_point: int):
        super().__init__(name, class_of_character, race_of_character)
        self.health_point = health_point
        self.mana_point = mana_point
        self.def_point = def_point
        self.damage_point = damage_point

    def character_info(self):
        info = {
            'Имя': self.name,
            'Раса': self.race_of_character,
            'Класс': self.class_of_character,
            'Здоровье': self.health_point,
            'Мана': self.mana_point,
            'Защита': self.def_point,
            'Урон': self.damage_point,
        }
        return info


class Races(RPG):
    def __init__(self,):
        super().__init__(self.race_of_character, self.class_of_character, self.name)

    def is_race_of_character(self,):
        for race in all_races.keys():
            if race == self.race_of_character:
                return True
        return False


class Locations:
    def __init__(self, environment, complexity):
        self.environment = environment
        self.complexity = complexity

    def __str__(self):
        return f"Окружение: {self.environment}, Уровень сложности: {self.complexity}"


class Settings:
    def __init__(self, complexity_lvl, enemies_count, ):
        self.complexity_lvl = complexity_lvl
        self.enemies_count = enemies_count


class PlayerTeam:
    def __init__(self,):
        pass

    @staticmethod
    def assembly_of_the_team(team):
        if 1 < len(team) > 4 or team == []:
            return 'Произошла ошибка: можно взять от 1 до 4 героев, не больше и не меньше.'
        team_list = []
        for hero in team:
            if hero in team:
                team_list.append(hero)
            else:
                return 'Произошла ошибка: проверьте, правильно ли вы выбрали героев\n' \
                       'и существуют ли они в игре:)\n' \
                       'напоминаем, что можно взять от 1 до 4 героев, не больше и не меньше.'
        return team_list
