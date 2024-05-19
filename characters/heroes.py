from config import Characters


class Heroes(Characters):
    def __init__(self):
        super().__init__(self.health_point, self.mana_point, self.def_point, self.damage_point, self.name,
                         self.race_of_character, self.class_of_character, self.damage_point)
