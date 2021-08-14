from Utils.Writer import Writer


class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players

    def encode(self):
        self.writeVint(self.type)   # GameMode Type
        self.writeVint(self.result) # Battle Result
        self.writeVint(20) # Tokens Gained
        self.writeVint(10) # Trophies Result
        self.writeVint(0) # Unknown
        self.writeVint(2147483647) # Doubled Tokens
        self.writeVint(2147483647) # Double Token Event
        self.writeVint(2147483647) # Token Doubler Remaining
        self.writeVint(0) # Championship Lose 
        self.writeVint(0) # Unknown
        self.writeVint(0) # Championship Level Passed
        self.writeVint(0) # Challenge Reward Type (0 = Star Tokens, 1 = Star Tokens)
        self.writeVint(0) #C hallenge Reward Ammount
        self.writeVint(0) # Championship Losses Left
        self.writeVint(0) # Championship Maximun Losses
        self.writeVint(8) # Coin Shower Event
        self.writeVint(0) #Underdog (But I Didn't Coded Yet)
        self.writeVint(23) #  Battle Result Info and Stuff
        self.writeVint(1) # Championship Type
        self.writeVint(0) # Unused Star Token (Beta Brawl Pass Stuff?)

        # Players in Game Array
        self.writeVint(len(self.players))

        for player in self.players:
            self.brawler  = self.players[player]['Brawler']
            self.skin     = self.players[player]['Skin']
            self.team     = self.players[player]['Team']
            self.username = self.players[player]['Name']

            if self.type == 5:
                self.writeVint(player) if self.team == 0 else self.writeVint(2)
            else:
                self.writeVint(2 if self.team != 0 else 1) if self.type == 2 else self.writeVint(self.team if self.team != 1 else 2)

            self.writeScId(16, self.brawler)if self.brawler != -1 else self.writeVint(0) # Player Brawler SCID
            self.writeScId(29, self.skin)   if self.skin    != -1 else self.writeVint(0) # Player Skin SCID

            self.writeVint(99999) # Player Trophies
            self.writeVint(99999) # Player Highest Trophies
            self.writeVint(10)    # Player Power Level

            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(1)

            self.writeString(self.username) # Player Name

            self.writeVint(100)      # Unknown
            self.writeVint(28000000) # Player Profile Icon ID
            self.writeVint(43000001) # Player Name Color ID
            self.writeVint(0)


        # Experience Array
        self.writeVint(2) # Count
        self.writeVint(0) # Normal Experience ID
        self.writeVint(1) # Normal Experience Ammount
        self.writeVint(8) # Star Player Experience ID
        self.writeVint(2) # Star Player Experience Ammount

        # Rank Up and Level Up Bonus Array
        self.writeVint(2) # Count
        self.writeVint(39) # Milestone CsvID
        self.writeVint(33) # Milestone Row (row 33 is rank 35)
        self.writeVint(39) # Milestone CsvID
        self.writeVint(34) # Milestone Row


        # Trophies and Experience Bars Array
        self.writeVint(2) # Count
        self.writeVint(1) # Ranks Milestone ID
        self.writeVint(0) # Brawler Trophies Bar
        self.writeVint(0) # Brawler Trophies for Rank
        self.writeVint(5) # Experience Milestone ID
        self.writeVint(0) # Total Experience Bar
        self.writeVint(0) # ???
        
        self.writeVint(0)  # Unknown
        self.writeBoolean(True)  # Play Again
        self.writeVint(1) # Count

        for x in range(1):
            self.writeVint(1)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeUInt8(0)

            self.writeScId(16, 0)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
