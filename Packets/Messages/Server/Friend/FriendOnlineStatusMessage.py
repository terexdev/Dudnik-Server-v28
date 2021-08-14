from Utils.Writer import Writer

class FriendOnlineStatusMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20109
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(2)
        self.writeInt(0)
        self.writeInt(1)

        print("Friend Online Status Updated!")