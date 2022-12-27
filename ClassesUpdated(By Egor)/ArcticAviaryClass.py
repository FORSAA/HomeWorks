from NewBaseAviaryClass import *

class ArcticAviary(BaseAviary):

    def __init__(self, AviaryName):
        super().__init__(AviaryName)
        self._biom = "Арктика"