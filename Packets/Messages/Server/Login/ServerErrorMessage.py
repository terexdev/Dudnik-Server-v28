from Utils.Writer import Writer
from Utils.Fingerprint import Fingerprint
import random

class ServerErrorMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24115
        self.player = player

    def encode(self):
        self.writeInt(random.randrange(43, 55))