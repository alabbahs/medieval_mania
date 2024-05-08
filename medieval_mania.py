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

    def attack(self, enemy, terrain):
        if enemy.__class__.__name__ == "light_unit":
            if terrain == "Forest":
                return 20
            elif terrain == "Open field":
                return 20
            elif terrain == "Hill":
                return 20
        if enemy.__class__.__name__ == "medium_unit":
            if terrain == "Forest":
                return 10
            elif terrain == "Open field":
                return 0
            elif terrain == "Hill":
                return 5
        if enemy.__class__.__name__ == "heavy_unit":
            if terrain == "Forest":
                return 40
            elif terrain == "Open field":
                return 30
            elif terrain == "Hill":
                return 20


class medium_unit:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy, terrain):
        if enemy.__class__.__name__ == "light_unit":
            if terrain == "Forest":
                return 20
            elif terrain == "Open field":
                return 40
            elif terrain == "Hill":
                return 30
        if enemy.__class__.__name__ == "medium_unit":
            if terrain == "Forest":
                return 20
            elif terrain == "Open field":
                return 20
            elif terrain == "Hill":
                return 20
        if enemy.__class__.__name__ == "heavy_unit":
            if terrain == "Forest":
                return 5
            elif terrain == "Open field":
                return 10
            elif terrain == "Hill":
                return 0


class heavy_unit:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy, terrain):
        if enemy.__class__.__name__ == "light_unit":
            if terrain == "Forest":
                return 0
            elif terrain == "Open field":
                return 5
            elif terrain == "Hill":
                return 10
        if enemy.__class__.__name__ == "medium_unit":
            if terrain == "Forest":
                return 30
            elif terrain == "Open field":
                return 20
            elif terrain == "Hill":
                return 40
        if enemy.__class__.__name__ == "heavy_unit":
            if terrain == "Forest":
                return 20
            elif terrain == "Open field":
                return 20
            elif terrain == "Hill":
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
    print("\nthese are the game rules\n")


def select_army(armies):
    print("\nSelect an empire")
    army_choice = input(
        " 1. Mongol \n 2. Japanese \n 3. Mamluk \n 4. Roman \nEnter choice:")
    if army_choice not in ["1", "2", "3", "4"]:
        print("INVALID INPUT! Please enter 1, 2, 3 or 4")
        select_army(armies)
    return armies[int(army_choice)-1]


def army_synopsis(army_name):

    if army_name == "Mongols":
        return "\nA great choice! The Mongol steppe is known for it's ruthlessness and tenacity on the battlefield, which lead to the fastest growth of any empire we had ever seen.\n\nWith their nomadic warriors and horseback archers, it was easy for this force to quickly and unexpectedly hit their targets like a scourge of fire. the motto for this force is, hit them hard and fast! \n\nUnits: \nLight - Horseback Archers \nMedium - Nomad Warriors \nHeavy - Steppe Saboteurs\n"

    elif army_name == "Romans":
        return "\nFrom your choice, you are either an admirer of tradition or someone who upholds the doctrine of papal infallibility. \n\nThe Holy Roman Empire, not to be mistaken with the ancient romans, are nevertheless a continuation of the same great empiric tradition. \n\nKnown for their studded steel armour and long swords, their defense is impenetrable while striking with force! \n\nUnits: \nLight - Horseback Archers \nMedium - Nomad Warriors \nHeavy - Steppe Saboteurs\n"

    elif army_name == "Mamluks":
        return "\nIt is said that when the Arabs were unable to maintain the islamic empire they had formed, the Persians carried the intellectual tradition while the Turks spearheaded the military. \n\nThis force is best summed by its elite class of warriors, the Janissaries, a battalion of young men raised and tempered by an intense regimen of martial training and discipline. \n\nUnits: \nLight - Nubian Archers \nMedium - Janissaries \nHeavy - Turkic Cavalry\n"

    elif army_name == "Japanese":
        return "\nThrough their adherence to the Bushido code, the Japanese army and its great martial tradition is a testament to chivalry and benevolence. During the Mongol invasion of Japan, despite the ruthlessness of the invading forces of Kublai, the Japanese managed to defend their island while staying true to their moral code. \n\nNothing is more emblematic of a true warrior than a samurai and his hardened Katana. \n\nLight - Shinobi Ninja \nMedium - Samurai \nHeavy - Hwacha Engineers\n"


def show_health(army1, army2):
    print(f"your health: {army1.health}")
    print(f"enemy health: {army2.health}\n")


def terrain_roll():
    input("\nPress Enter to roll for the terrain this war will proceed on")
    print("Rolling...")

    terrain = rand.choice(["Forest", "Open field", "Hill"])

    print(f"Terrain to be fought on: {terrain}\n")

    return terrain


def enemy_terrain_roll():
    print("\nYour opponent is rolling for the terrain...")

    terrain = rand.choice(["Forest", "Open field", "Hill"])

    print(f"Terrain to be fought on: {terrain}\n")

    return terrain


def unit_select():
    unit_selected = input(
        f"Select a unit from your army to engage the opposing force: \n1.{player_army.light_unit.name} \n2.{player_army.medium_unit.name} \n3.{player_army.heavy_unit.name} \n\n")
    player_unit = player_army.unit_list[int(
        unit_selected) - 1]
    if unit_selected not in ["1", "2", "3"]:
        print("INVALID INPUT! Please enter 1, 2 or 3")
        unit_select()
    else:
        return player_unit


def check_winner(player_army, enemy_army, win_counter, loss_counter):
    if enemy_army.health <= 0:
        print("You won the war\n")
        win_counter += 1
        print(f"wins - {win_counter}")
        print(f"losses - {loss_counter}")

    elif player_army.health <= 0:
        print("You lost the war\n")
        loss_counter += 1
        print(f"wins - {win_counter}")
        print(f"losses - {loss_counter}")


def check_final_score(win_counter, loss_counter):
    if win_counter == 3 and loss_counter == 0:
        print("THE KHANS TRIUMPH\n\n")
    elif win_counter == 2 and loss_counter == 1:
        print("Sun Tzu's Successn\n\n")
    elif win_counter == 1 and loss_counter == 2:
        print("\nHannibal's Retreat\n\n")
    elif win_counter == 0 and loss_counter == 3:
        print("\nNapoleons Waterloo\n\n")


def begin_wars(player_army, enemy_armies):

    win_counter = 0
    loss_counter = 0

    for i, enemy_army in enumerate(enemy_armies):
        print(f"War {i+1} - {enemy_army.name}\n")

        while ((enemy_army.health > 0) and (player_army.health > 0)):

            player_unit = unit_select()
            enemy_unit = rand.choice(enemy_army.unit_list)

            terrain = terrain_roll()

            damage_done = player_unit.attack(enemy_unit, terrain)

            enemy_army.health -= damage_done
            show_health(player_army, enemy_army)

            if enemy_army.health <= 0:
                continue

            player_unit = unit_select()
            enemy_unit = rand.choice(enemy_army.unit_list)

            terrain = enemy_terrain_roll()

            damage_done = enemy_unit.attack(player_unit, terrain)

            player_army.health -= damage_done
            show_health(player_army, enemy_army)

        # check_winner(player_army, enemy_army, win_counter, loss_counter)
        if enemy_army.health <= 0:
            print("You won the war\n")
            win_counter += 1
            print(f"wins - {win_counter}")
            print(f"losses - {loss_counter}\n")

        elif player_army.health <= 0:
            print("You lost the war\n")
            loss_counter += 1
            print(f"wins - {win_counter}")
            print(f"losses - {loss_counter}\n")

        player_army.health = 100

    check_final_score(win_counter, loss_counter)


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
