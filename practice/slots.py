class Inventory:
    def __init__(self):
        self.slots = []
    
    def add_items(self, item):
        self.slots.append(item)
        
class SortedInventory(Inventory):
    def add_items(self, item):
        super().add_items(item)
        self.slots.sort()
        print(self.slots)