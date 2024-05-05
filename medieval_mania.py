class Army:
    def __init__(self, name, light_unit, medium_unit, heavy_unit):
        self.name = name
        self.health = 100
        self.light_unit = light_unit
        self.medium_unit = medium_unit
        self.heavy_unit = heavy_unit


class light_unit:
    def __init__(self, name):
        self.name = name

    def attack(enemy, terrain):
        if (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30

        elif (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30

        elif (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30


class medium_unit:
    def __init__(self, name):
        self.name = name

    def attack(enemy, terrain):
        if (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30

        elif (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30

        elif (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30


class heavy_unit:
    def __init__(self, name):
        self.name = name

    def attack(enemy, terrain):
        if (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30

        elif (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30

        elif (terrain == "forest") and (type(enemy).__name__ == "heavy_unit"):
            enemy.army.health -= 30


def initialise_game():

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
    steppe_saboteur = heavy_unit("Steppe Saboteur")
    mongols = Army("Mamluks", horseback_archers,
                   nomad_warriors, steppe_saboteur)


initialise_game()
