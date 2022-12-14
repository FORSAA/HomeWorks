from NewBaseAviaryClass import *

class ArcticAviary(BaseAviary):

    def __init__(self, AviaryName, biom):
        super().__init__(AviaryName, biom)
        self._biom = "Арктика"