from NewBaseAviaryClass import *

class SavannaAviary(BaseAviary):

    def __init__(self, AviaryName):
        super().__init__(AviaryName)
        self._biom = "Саванна"