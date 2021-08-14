from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class TeamGameroomDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player


    def encode(self):
        # Gameroom Type
        DataBase.loadGameroom(self)
        self.writeVint(1)

        self.writeUInt8(0)
        self.writeVint(1)

        # MapID
        self.writeLong(self.player.room_id)

        self.writeUInt8(0)
        self.writeUInt8(0)

        self.writeVint(0)
        self.writeVint(self.player.slot_index)

        # MapID
        self.writeScId(15, self.mapID)

        # Players in Room
        self.writeVint(1)
        for player, values in self.playersdata.items():

            self.writeVint(self.playerCount)
            self.writeLong(int(self.playersdata[player]['LowID'])) # AccountID

            self.writeScId(16, self.playersdata[player]["brawlerID"])  # BrawlerID
            self.writeVint(0)     # SkinID

            self.writeVint(self.player.brawler_trophies) # Trophies
            self.writeVint(self.player.brawler_trophies_for_rank) # Highest Trophies
            self.writeVint(10)    # Power Level

            self.writeVint(3)     # Player State
            self.writeVint(self.playersdata[player]["Ready"])     # Is Player Ready
            self.writeVint(self.playersdata[player]["Team"])     # Team (Blue/Red)
            self.writeVint(0)
            self.writeVint(0)

            # Player Name
            self.writeString(self.playersdata[player]["name"])                  # Player name
            self.writeVint(100)
            self.writeVint(28000000 + self.playersdata[player]["profileIcon"])  # Player icon
            self.writeVint(43000000 + self.playersdata[player]["namecolor"])    # Player name color
            self.writeVint(0)
            self.writeScId(23, self.playersdata[player]["starpower"])       # Starpower
            self.writeScId(23, self.playersdata[player]["gadget"])          # Gadget 


        self.writeVint(0) # array
        self.writeVint(0) # array
        self.writeVint(0)
        if self.player.use_gadget:
            self.writeVint(6)
        else:
            self.writeVint(0)