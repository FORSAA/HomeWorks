from NewBaseAviaryClass import *

class SavannaAviary(BaseAviary):

    def __init__(self, AviaryName, biom):
        super().__init__(AviaryName, biom)
        self._biom = "Саванна"