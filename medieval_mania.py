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

    # Damage done (number returned) adjusted based on enemy unit and terrain advantage/disadvantage, done for all unit types
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


# This function is called when the game is started to create all the armies with their specific units
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
    print("\nGame Rules:\n")
    print("1. Select an army from the listed historical empires.")
    print("2. Battles are turn-based. In each turn, you will:")
    print("   - Choose a unit (light, medium, or heavy) to send into battle.")
    print("   - Roll for terrain (Forest, Open field, or Hill), which affects combat outcomes.")
    print("3. Each unit type has strengths and weaknesses depending on the enemy unit type and the terrain.")
    print("4. The goal is to reduce the enemy army's health to zero to win the battle.")
    print("5. Win the game by defeating all enemy armies in successive battles.\n")


# Here the armies input is the list of all the armies that were returned in the initialise_armies() function
def select_army(armies):
    print("\nSelect an empire")
    army_choice = input(
        " 1. Mongol \n 2. Japanese \n 3. Mamluk \n 4. Roman \nEnter choice:")
    if army_choice not in ["1", "2", "3", "4"]:
        print("\nINVALID INPUT! Please enter 1, 2, 3 or 4")
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


# Randomises terrain that will be fought on
def terrain_roll():
    input("\nPress Enter to roll for the terrain this bout will proceed on")
    print("Rolling...")

    terrain = rand.choice(["Forest", "Open field", "Hill"])

    print(f"Terrain to be fought on: {terrain}\n")

    return terrain


def enemy_terrain_roll():
    print("\nYour opponent is rolling for the terrain...")

    terrain = rand.choice(["Forest", "Open field", "Hill"])

    print(f"Terrain to be fought on: {terrain}\n")

    return terrain


# Asks player which unit they want to send in, returns the unit
def unit_select():
    unit_selected = input(
        f"Select a unit from your army to engage the opposing force: \n1.{player_army.light_unit.name} \n2.{player_army.medium_unit.name} \n3.{player_army.heavy_unit.name} \n\n Enter choice: ")

    # To catch any invalid inputs, avoiding indexing out of range
    if unit_selected in ["1", "2", "3"]:
        player_unit = player_army.unit_list[int(unit_selected) - 1]
        return player_unit
    else:
        print("\nINVALID INPUT! Please enter 1, 2 or 3")
        return unit_select()


# This is called after each turn in order to check if one of the armies has lost

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


# Prints the final record of all the wars with a title for each score

def check_final_score(win_counter, loss_counter):
    if win_counter == 3 and loss_counter == 0:
        print("THE KHANS' TRIUMPH\n\n")
        print("Much like Genghis Khan’s Mongol Empire, your flawless campaign has swept across the continents, unmatched in both strategy and force. Genghis Khan, known for his ability to utilize superior military strategies to conquer vast territories, would be proud of your achievement.\n")
        print("\n - 'I am the punishment of God... If you had not committed great sins, God would not have sent a punishment like me upon you.' - Genghis Khan\n")
    elif win_counter == 2 and loss_counter == 1:
        print("Sun Tzu's Success\n\n")
        print("Your strategic prowess echoes that of Sun Tzu, the ancient Chinese military strategist, author of 'The Art of War'. Your victories, achieved through the careful balance of strength and wisdom, remind us of Sun Tzu's teachings on the importance of knowing when to engage and when to hold back to ensure overall success.\n")
        print(" - 'Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.' - Sun Tzu\n")
    elif win_counter == 1 and loss_counter == 2:
        print("Hannibal's Retreat\n")
        print("Your strife is like that of Hannibal Barca's during the Second Punic War, you demonstrated tactical genius in several battles but faced strategic setbacks ultimately. Hannibal, known for his daring crossing of the Alps and victories in enemy territory, eventually had to retreat due to the lack of support and resources, similar to the challenges you faced.\n")
        print("- 'I will either find a way, or make one.' - Hannibal Barca\n")
    elif win_counter == 0 and loss_counter == 3:
        print("Napoleon's Waterloo\n\n")
        print("Your campaign ended much like Napoleon’s at Waterloo—a defeat that marked the end of an era. Napoleon Bonaparte, once the master of Europe, met his match at Waterloo in 1815, which decisively ended his rule and reshaped European politics. Like Napoleon, you've faced formidable opposition that halted your conquests.\n")
        print(" - 'Never interrupt your enemy when he is making a mistake.' - Napoleon Bonaparte\n")


# player_army is the one picked from the list of armies returned by initialise_armies(), enemy_armies is a list of the remaining armies that will be fought against.

def begin_wars(player_army, enemy_armies):

    win_counter = 0
    loss_counter = 0

    # i is the number of iterations in this for loop, allowing us to track and display which number war is being fought
    for i, enemy_army in enumerate(enemy_armies):
        print(f"War {i+1} - {enemy_army.name}\n")

        while ((enemy_army.health > 0) and (player_army.health > 0)):

            # Players turn to attack
            player_unit = unit_select()
            enemy_unit = rand.choice(enemy_army.unit_list)

            terrain = terrain_roll()

            # attack calculates damage done given enemy and terrain
            damage_done = player_unit.attack(enemy_unit, terrain)

            # Subtract health by number returned from attack()
            enemy_army.health -= damage_done
            show_health(player_army, enemy_army)

            # Line added to account for while loop not breaking if enemy is defeated, before this the game would wait for the enemies turn
            if enemy_army.health <= 0:
                continue

            # Opponent/CPU turn to attack
            player_unit = unit_select()
            enemy_unit = rand.choice(enemy_army.unit_list)

            terrain = enemy_terrain_roll()

            damage_done = enemy_unit.attack(player_unit, terrain)

            player_army.health -= damage_done
            show_health(player_army, enemy_army)

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

    # Checking the score and return appropriate message
    check_final_score(win_counter, loss_counter)


# Game loop
run = True
while run:
    print("\n\nWelcome to Medieval Mania")
    menu_input = input(
        " 1. Play Game \n 2. How To Play \n 3. Quit Game \nEnter choice: ")
    if menu_input == "1":
        armies = initialise_armies()
        player_army = select_army(armies)
        enemy_armies = armies.remove(player_army)
        print(army_synopsis(player_army.name))
        begin_wars(player_army, armies)
        run = False
    elif menu_input == "2":
        how_to_play()
    elif menu_input == "3":
        run = False
