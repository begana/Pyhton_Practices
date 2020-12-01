import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

class Thief(Character):
    sneaky = True
    
    def pick_pocket(self):
        if self.sneaky:
            return bool(random.randint(0, 1))
        return False
    
    def hide(self, light_level):
        return self.sneaky and light_level < 10
    