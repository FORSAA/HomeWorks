from BaseAviaryClass import *

class ArcticAviary(BaseAviary):

    def __init__(self, name, canContainPredator=False):
        super().__init__(name, canContainPredator)
        self._aviaryBiom = "Арктика"