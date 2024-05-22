from config import Locations


class LocationBonus(Locations):
    def __init__(self):
        super().__init__(self.environment, self.complexity)
