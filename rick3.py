class Rick(object):
    def __init__(self, universe):
        self.universe = universe
        self.morty = None
        
    def assign(self, morty):
        self.morty = morty
        morty.is_assigned = True
