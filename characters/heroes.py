from config import CreateCharacters


HeroCreator = CreateCharacters

David = HeroCreator('David', 'Warrior', 'Human',
                    70, 15, 6, 8).character_info()

Carol = HeroCreator('Carol', 'Mage', 'Elf',
                    35, 55, 3, 15).character_info()

Dorob = HeroCreator('Dorob', 'Tank', 'Dwarf',
                    90, 9, 9, 4).character_info()

Freid = HeroCreator('Freid', 'Shooter', 'Human',
                    45, 20, 3, 11).character_info()

Azulon = HeroCreator('Azulon', 'nature', 'Silf',
                     60, 26, 5, 7).character_info()

all_heroes = [David, Carol, Freid, Azulon, Dorob]


def view_all_heroes(heroes_list):
    for hero in heroes_list:
        print(f"{'Имя':<3}: {hero['Имя']:<10} "
              f"{'Раса':<3}: {hero['Раса']:<10} "
              f"{'Класс':<4}: {hero['Класс']:<10} "
              f"{'Здоровье':<8}: {hero['Здоровье']:<4} "
              f"{'Мана':<4}: {hero['Мана']:<4} "
              f"{'Защита':<5}: {hero['Защита']:<4} "
              f"{'Урон':<4}: {hero['Урон']:<4}")

