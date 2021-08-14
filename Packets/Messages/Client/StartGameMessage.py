from Utils.Reader import BSMessageReader
from Packets.Messages.Server.StartLoadingMessage import StartLoadingMessage
from Logic.Player import Players

class StartGameMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        pass

    def process(self):
        StartLoadingMessage(self.client, self.player).send()