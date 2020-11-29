import random

from attribute import Sneaky, Agile
from characters import Character


class Thief(Sneaky, Agile, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
