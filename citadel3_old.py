class Citadel(object):
    def __init__(self):
        self.__residents__ = []
        
    def get_all_residents(self):
        return self.__residents__
    
    def add_resident(self, resident):
        self.__residents__.append(resident)
