from Packets.Messages.Server.Battle.BattleEndMessage import BattleEndMessage

from Utils.Reader import BSMessageReader


class AskForBattleEndMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.players = {}

    def decode(self):
        self.result   = self.read_Vint()  # Battle Result
        self.unk      = self.read_Vint()  # Unknown
        self.rank     = self.read_Vint()  # Player Rank
        self.mapID    = self.readScId()  # Map ID
        self.count    = self.read_Vint()  # Players Count

        # Players in Battle
        for player in range(self.count):
            self.brawler     = self.readScId()       # Player Skin SCID
            self.skin        = self.readScId()       # Player Skin SCID
            self.team        = self.read_Vint()       # Player Team
            self.unk         = self.read_Vint()       # Unknown
            self.username    = self.read_string()     # Player Name

            self.players[player] = {f'Name': self.username, 'Team': self.team, 'Brawler': self.brawler[1], 'Skin': self.skin[1]}



    def process(self):
        if self.rank != 0:
            self.type = 5  if self.players[0]['Team'] == self.players[1]['Team'] else 2
        else:
            self.type = 0

        BattleEndMessage(self.client, self.player, self.type, self.result, self.players).send()