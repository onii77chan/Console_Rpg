class RPG:
    def __init__(self, name, class_of_character, damage_type, race_of_character):
        self.name = name
        self.class_of_character = class_of_character
        self.damage_type = damage_type
        self.race_of_character = race_of_character


class Characters(RPG):
    def __init__(self, health_point, mana_point, def_point, damage_point, bonus_damage,):
        self.health_point = health_point
        self.mana_point = mana_point
        self.def_point = def_point
        self.damage_point = damage_point
        self.bonus_damage = bonus_damage
        super().__init__(self.name, self.class_of_character, self.damage_type, self.race_of_character)

    def create_character(self):
        return {'Имя': self.name, 'Раса': self.race_of_character, 'Класс': self.class_of_character,
                'Здоровье': self.health_point, 'Мана': self.mana_point, 'Защита': self.def_point,
                'Тип_урона': self.damage_type, 'Урон': self.damage_point,}




class Locations:
    def __init__(self, environment, complexity, ):
        self.environment = environment

