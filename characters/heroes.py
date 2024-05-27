from config import CreateCharacter


class CharacterSkills:
    def __init__(self, character, skill_name, skill_type, damage_type):
        self.character = character
        self.skill_name = skill_name
        self.skill_type = skill_type
        self.damage_type = damage_type

    def __str__(self):
        return (f'навык персонажа: {self.character} название навыка:{self.skill_name} '
                f'тип навыка:{self.skill_type} тип урона:{self.damage_type}')


class CreateSkill(CharacterSkills):
    def __init__(self, character, skill_name, skill_type, damage_type):
        CharacterSkills.__init__(self, character, skill_name, skill_type, damage_type)


