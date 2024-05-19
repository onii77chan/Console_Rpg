from characters.config_characters import all_races

class RPG:
    def __init__(self, name, class_of_character, damage_type, race_of_character):
        self.name = name
        self.class_of_character = class_of_character
        self.damage_type = damage_type
        self.race_of_character = race_of_character


class Characters(RPG):
    def __init__(self, name, class_of_character, damage_type, race_of_character,
                 health_point, mana_point, def_point, damage_point):
        super().__init__(name, class_of_character, damage_type, race_of_character)
        self.health_point = health_point
        self.mana_point = mana_point
        self.def_point = def_point
        self.damage_point = damage_point

    def create_character(self):
        return {
            'Имя': self.name,
            'Раса': self.race_of_character,
            'Класс': self.class_of_character,
            'Здоровье': self.health_point,
            'Мана': self.mana_point,
            'Защита': self.def_point,
            'Тип_урона': self.damage_type,
            'Урон': self.damage_point,
        }


class Races(RPG):
    def __init__(self,):
        super().__init__(self.race_of_character, self.class_of_character, self.damage_type, self.name)

    def is_race_of_character(self,race_of_character):
        for race in  all_races.keys():
            if race == race_of_character:
                return True
        return False

    def Human_Race(self, race_of_character):
        if self.is_race_of_character(race_of_character):



    def character_race(self, race_of_character):
        if race_of_character in



class Locations:
    def __init__(self, environment, complexity):
        self.environment = environment
        self.complexity = complexity

    def __str__(self):
        return f"Окружение: {self.environment}, Уровень сложности: {self.complexity}"


characters = Characters("Gandalf", "Mage", "Magic", "Human", health_point=60, mana_point=40, def_point=40, damage_point=15)
mage = characters.create_character()
print(mage)

