class Character:
    """
    ...
    """
    def __init__(self, name_of_character):
        self.name = name_of_character

    def __str__(self):
        return "base character class"


class CreateCharacter(Character):
    """
    ...
    """
    def __init__(self, name_of_character, race_of_character='unnamed', class_of_character='unnamed',
                 health_points=40, mana_points=5, armor_points=5, damage_points=5):
        super().__init__(name_of_character)
        self.race_of_character = race_of_character
        self.class_of_character = class_of_character
        self.health_points = health_points
        self.mana_points = mana_points
        self.armor_points = armor_points
        self.damage_points = damage_points

    def character_information(self) -> dict:
        return {'name': self.name,
                'race': self.race_of_character,
                'class': self.class_of_character,
                'health': self.health_points,
                'mana': self.mana_points,
                'armor': self.armor_points,
                'damage': self.damage_points}

    def __str__(self):
        return f"Name: {self.name}, Race: {self.race_of_character}, Class: {self.class_of_character}, " \
               f"Health: {self.health_points}, Mana: {self.mana_points}, Armor: {self.armor_points}, " \
               f"Damage: {self.damage_points}"


class Races:
    """
    ...
    """
    def __init__(self, name_of_race):
        self.name_of_race = name_of_race

    def __str__(self):
        return "base races class"


class CreateRace(Races):
    """
    ...
    """
    def __init__(self, name_of_race, factor, type_of_race="unnamed",
                 race_attributes=None, description="pass"):
        super().__init__(name_of_race)
        if race_attributes is None:
            race_attributes = []
        self.factor = factor
        self.type_of_race = type_of_race
        self.race_attributes = race_attributes
        self.description = description

    def race_information(self) -> dict:
        return {
            'name': self.name_of_race,
            'type': self.type_of_race,
            'attributes': self.race_attributes,
            'factor': self.factor,
            'description': self.description
        }

    def __str__(self):
        return (f"Race Info:\n"
                f"{'Name:':<12} {self.name_of_race}"
                f"{'Type:':<12} {self.type_of_race}"
                f"{'Attributes:':<12} {', '.join(self.race_attributes)}"
                f"{'Factor:':<12} {self.factor}"
                f"{'Description:':<12} {self.description}")
