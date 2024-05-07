import random as rand


class Army:
    def __init__(self, name, light_unit, medium_unit, heavy_unit):
        self.name = name
        self.health = 100
        self.light_unit = light_unit
        self.medium_unit = medium_unit
        self.heavy_unit = heavy_unit
        self.unit_list = [light_unit, medium_unit, heavy_unit]


class light_unit:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        if enemy.__class__.__name__ == "light_unit":
            return 20
        if enemy.__class__.__name__ == "medium_unit":
            return 10
        if enemy.__class__.__name__ == "heavy_unit":
            return 30


class medium_unit:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        if enemy.__class__.__name__ == "light_unit":
            return 30
        if enemy.__class__.__name__ == "medium_unit":
            return 20
        if enemy.__class__.__name__ == "heavy_unit":
            return 10


class heavy_unit:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        if enemy.__class__.__name__ == "light_unit":
            return 10
        if enemy.__class__.__name__ == "medium_unit":
            return 30
        if enemy.__class__.__name__ == "heavy_unit":
            return 20


def initialise_armies():

    auxiliary_archers = light_unit("Auxiliary Archers")
    legionaries = medium_unit("Legionaries")
    trebuchet_engineers = heavy_unit("Trebuchet Engineers")
    romans = Army("Romans", auxiliary_archers,
                  legionaries, trebuchet_engineers)

    nubian_archers = light_unit("Nubian Archer")
    janissaries = medium_unit("Janissaries")
    turkic_cavalry = heavy_unit("Turkic Cavalry")
    mamluks = Army("Mamluks", nubian_archers, janissaries, turkic_cavalry)

    shinobi_ninja = light_unit("Shinobi Ninja")
    samurai = medium_unit("Samurai")
    hwacha_engineers = heavy_unit("Hwacha Engineers")
    japanese = Army("Japanese", shinobi_ninja, samurai, hwacha_engineers)

    horseback_archers = light_unit("Horseback Archers")
    nomad_warriors = medium_unit("Nomad Warriors")
    steppe_saboteurs = heavy_unit("Steppe Saboteurs")
    mongols = Army("Mongols", horseback_archers,
                   nomad_warriors, steppe_saboteurs)

    return [mongols, japanese, mamluks, romans]


def how_to_play():
    print("these are the game rules")


def select_army(armies):
    print("\nSelect an empire")
    army_choice = input(
        " 1. Mongol \n 2. Japanese \n 3. Mamluk \n 4. Roman \nEnter choice:")
    return armies[int(army_choice)-1]


def army_synopsis(army_name):

    if army_name == "Mongols":
        return "\nA great choice! The Mongol steppe is known for it's ruthlessness and tenacity on the battlefield, which lead to the fastest growth of any empire we had ever seen.\n\nWith their nomadic warriors and horseback archers, it was easy for this force to quickly and unexpectedly hit their targets like a scourge fire. the motto for this force is, hit them hard and fast! \n\nUnits: \nLight - Horseback Archers \nMedium - Nomad Warriors \nHeavy - Steppe Saboteurs\n"

    elif army_name == "Romans":
        return "\nFrom your choice, you are either an admirer of tradition or someone who upholds the doctrine of papal infallibility. \n\nThe Holy Roman Empire, not to be mistaken with the ancient romans, are nevertheless a continuation of the same great empiric tradition. \n\nKnown for their studded steel armour and long swords, their defense is impenetrable while striking with force! \n\nUnits: \nLight - Horseback Archers \nMedium - Nomad Warriors \nHeavy - Steppe Saboteurs\n"

    elif army_name == "Mamluks":
        return "\nIt is said that when the Arabs were unable to maintain the islamic empire they had formed, the Persians carried the intellectual tradition while the Turks spearheaded the military. \n\nThis force is best summed by its elite class of warriors, the Janissaries, a battalion of young men raised and tempered by an intense regimen of martial training and discipline. \n\nUnits: \nLight - Nubian Archers \nMedium - Janissaries \nHeavy - Turkic Cavalry\n"

    elif army_name == "Japanese":
        return "\nThrough their adherence to the Bushido code, the Japanese army and its great martial tradition is a testament to chivalry and benevolence. During the Mongol invasion of Japan, despite the ruthlessness of the invading forces of Kublai, the Japanese managed to defend their island while staying true to their moral code. \n\nNothing is more emblematic of a true warrior than a samurai and his hardened Katana. \n\nLight - Shinobi Ninja \nMedium - Samurai \nHeavy - Hwacha Engineers\n"


def begin_wars(player_army, enemy_armies):
    for i, enemy_army in enumerate(enemy_armies):
        print(f"War {i+1} - {enemy_army.name}\n")
        while enemy_army.health > 0 and player_army.health > 0:
            unit_selected = input(
                f"Select a unit from your army to engage the opposing force: \n1.{player_army.light_unit.name} \n2.{player_army.medium_unit.name} \n3.{player_army.heavy_unit.name} \n\n")
            enemy_unit = rand.choice(enemy_army.unit_list)
            damage_done = player_army.unit_list[int(
                unit_selected) - 1].attack(enemy_unit)
            enemy_army.health -= damage_done
            print(enemy_army.health)


run = True
while run:
    print("Welcome to Medieval Mania")
    menu_input = input(
        " 1. Play Game \n 2. How To Play \n 3. Quit Game \nEnter choice: ")
    if menu_input == "1":
        armies = initialise_armies()
        player_army = select_army(armies)
        enemy_armies = armies.remove(player_army)
        print(enemy_armies)
        print(army_synopsis(player_army.name))
        begin_wars(player_army, armies)
        run = False
    elif menu_input == "2":
        how_to_play()
    elif menu_input == "3":
        run = False
