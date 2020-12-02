import copy

class Liar(list):
    def __init__(self, item, *args, **kwargs):
        super().__init__()
        return self.append(item)
    
    