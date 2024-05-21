from config import CreateCharacters


HeroCreator = CreateCharacters

David = HeroCreator('David', 'Warrior', 'Human',
                    70, 15, 6, 8).character_info()

Carol = HeroCreator('Carol', 'Mage', 'Elf',
                    35, 55, 3, 15).character_info()

Dorob = HeroCreator('Dorob', 'Tank', 'Dwarf',
                    90, 9, 9, 5).character_info()

Freid = HeroCreator('Freid', 'Shooter', 'Human',
                    45, 20, 3, 11).character_info()

Azulon = HeroCreator('Azulon', 'nature', 'Silf',
                     60, 26, 5, 7).character_info()

all_heroes = [David, Carol, Freid, Azulon, Dorob]


