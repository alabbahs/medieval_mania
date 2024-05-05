class Army:
    def __init__(self, name, light_unit, medium_unit, heavy_unit):
        self.name = name
        self.unit_1 = light_unit
        self.unit_2 = medium_unit
        self.unit_3 = heavy_unit
        self.health = 100
