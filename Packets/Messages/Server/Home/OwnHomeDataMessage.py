from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards
from datetime import datetime

from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

from Logic.Quest import Quests
from Logic.Shop import Shop
from Logic.EventSlots import EventSlots


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self)

        # LOGIC CLIENT HOME #

        # sub_4558EC #
        self.writeVint(0)  # Timestamp
        self.writeVint(0)  # Timestamp

        self.writeVint(self.player.trophies)  # Trophies
        self.writeVint(self.player.highest_trophies)  # Highes Trophies

        self.writeVint(0)
        self.writeVint(200)  # Trophy Road Reward

        self.writeVint(self.player.player_experience)  # Exp Points

        self.writeScId(28, self.player.profile_icon)  # Profile Icon
        self.writeScId(43, self.player.name_color)  # Profile NameColor

        self.writeVint(0)  # array
        for x in range(0):
            pass

        # Selected Skins array
        self.writeVint(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeScId(29, self.player.brawlers_skins[brawler_id] )

        # Unlocked Skins array
        self.writeVint(len(self.player.skinsID))
        for skin_id in self.player.skinsID:
            self.writeScId(29, skin_id)
    

        self.writeVint(999)  # array
        for x in range(999):
            pass
# 20
        self.writeVint(999)
        self.writeVint(999)
        self.writeVint(0)

        self.writeUInt8(0)

        self.writeVint(0)
        self.writeVint(88)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeBool(False)
        self.writeBool(False)

        self.writeUInt8(4)

        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)

        self.writeVint(0)  # Name Change Cost
        self.writeVint(0)   # Name Change Timer

        count = len(Shop.offers)

        self.writeVint(count)
        for i in range(count):
            item = Shop.offers[i]

            self.writeVint(1)

            self.writeVint(item['ID'])
            self.writeVint(item['Multiplier'])
            self.writeVint(0)
            self.writeVint(item['SkinID'])
            self.writeVint(item['ShopType'])  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVint(item['Cost'])  # Cost
            self.writeVint(item['Timer'])

            self.writeVint(1)
            self.writeVint(100)
            self.writeBoolean(False)  # is Offer Purchased

            self.writeBoolean(False)
            self.writeVint(item['ShopDisplay'])  # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(False)
            self.writeVint(0)

            self.writeInt(0)

            self.write_string_reference(item['OfferTitle'])

            self.writeBoolean(False)
            self.writeString()
            self.writeVint(0)
            self.writeBoolean(False)
            self.writeVint(0)
            self.writeVint(0)

        self.writeVint(0)
        self.writeVint(200)

        self.writeVint(5)  # Time till bonus tokens array
        for x in range(0):
            pass

        self.writeVint(0)  # Tickets
        self.writeVint(0)

        self.writeScId(16, self.player.brawler_id)

        self.writeString("RU")
        self.writeString("Romashka")

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(1) # Brawl Pass
        for x in range(1):
            self.writeVint(2) # Current Season

            self.writeVint(9999) # Pass Tokens

            self.writeVint(0) # Premium Pass Progress
            self.writeVint(0) # Free Pass Progress

            self.writeInt8(1)
            for i in range(4):
                self.writeInt(4)

            self.writeInt8(1)
            for i in range(4):
                self.writeInt(4)


        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeByte(1)
        count2 = len(Quests.quests)
        self.writeVint(count2)  # Count
        for i in range(count2): # Count
            item = Quests.quests[i]
            self.writeVint(4) 
            self.writeVint(4)
            self.writeVint(item['MissionID']) # Mission Type
            self.writeVint(item['Reached']) # Current goal achieve
            self.writeVint(item['Max']) # Quest goal
            self.writeVint(item['Reward']) # Tokens reward
            self.writeVint(item['Type']) # Quest Type
            self.writeVint(item['CurrentLVL']) # current level
            self.writeUInt8(item['MaxLVL']) # max level
            self.writeVint(2)

            self.writeVint(item['BrawlPassExclusiveBoolean']) # Brawl Pass Exclusive
            self.writeScId(16, item['BrawlerID']) # csvID and brawlerID

            self.writeVint(item['GamemodeID']) # Gamemode TID
            self.writeVint(1)
            self.writeVint(1)
        # Emotes Array
        self.writeBoolean(True)
        if True:
            self.writeVint(len(self.player.emotesID))
            for emote_id in self.player.emotesID:
                self.writeScId(52, emote_id)
                self.writeVint(1)     # Unknown
                self.writeVint(1)     # Unknown
                self.writeVint(1)     # Unknown


        # sub_2CEABC #
        self.writeVint(0)   # Shop Timestamp
        self.writeVint(100) # Tokens for Brawl Box
        self.writeVint(10)  # Tokens for Big Box

        self.writeVint(30)
        self.writeVint(3)
        self.writeVint(80)

        self.writeVint(10)
        self.writeVint(40)
        self.writeVint(1000)

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)

        self.writeVint(0)

        # LOGIC EVENTS #

        count = len(EventSlots.maps)

        self.writeVint(count + 1)  # Map slots count
        for i in range(count + 1):
            self.writeVint(i)

        self.writeVint(count)

        for map in EventSlots.maps:
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(map['Ended'])
            self.writeVint(EventSlots.Timer)

            self.writeVint(10)

            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString()
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

            self.writeBoolean(False)

            self.writeVint(0)
            self.writeVint(0)

        self.writeVint(0)

        self.writeVint(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(i)

        self.writeVint(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [10, 30, 80]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [6, 20, 60]:
            self.writeVint(i)

        self.writeVint(4)
        for i in [20, 50, 140, 280]:
            self.writeVint(i)

        self.writeVint(4)
        for i in [150, 400, 1200, 2600]:
            self.writeVint(i)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeUInt8(1)

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(1)  # array
        for x in range(1):
            self.writeInt(1)
            self.writeInt(41000014)

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(0)  # array
        for x in range(0):
            pass
        self.writeLong(self.player.low_id)

        self.writeVint(0) # array
        for x in range(0):
            pass

        self.writeVint(0)

        self.writeUInt8(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(self.player.low_id)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        if self.player.name == "Guest":
            self.writeString(self.player.name)
            self.writeVint(0)
            DataBase.createAccount(self)
        else:
            self.writeString(self.player.name)
            self.writeVint(1)

        self.writeInt(0)

        # Commodity count
        self.writeVint(8)

        # Unlocked Brawlers $ Resources array
        self.writeVint(len(self.player.cardsUnlockID) + 4)  # count

        index = 0
        for unlock_id in self.player.cardsUnlockID:
            self.writeVint(23)
            self.writeVint(unlock_id)
            try:
                self.writeVint(self.player.BrawlersUnlockedState[str(index)])
            except:
                self.writeVint(1)

            if index == 34:
                index += 3
            elif index == 32:
                index += 2
            else:
                index += 1

        self.writeVint(5)  # csv id
        self.writeVint(1)  # resource id
        self.writeVint(self.player.brawl_boxes)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(8)  # resource id
        self.writeVint(self.player.gold)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(9)  # resource id
        self.writeVint(self.player.big_boxes)  # resource amount

        self.writeVint(5)  # csv id
        self.writeVint(10)  # resource id
        self.writeVint(self.player.star_points)  # resource amount

        # Brawlers Trophies array
        self.writeVint(len(self.player.brawlersID))  # brawlers count

        for brawler_id in self.player.brawlersID:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_trophies[str(brawler_id)])

        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.brawlersID))  # brawlers count

        for brawler_id in self.player.brawlersID:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_trophies_in_rank[str(brawler_id)])

        self.writeVint(0)  # array

        # Brawlers Upgrade Points array
        self.writeVint(len(self.player.brawlersID))  # brawlers count

        for brawler_id in self.player.brawlersID:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_upgradium[str(brawler_id)])

        # Brawlers Power Level array
        self.writeVint(len(self.player.brawlersID))  # brawlers count

        for brawler_id in self.player.brawlersID:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.Brawler_level[str(brawler_id)])

        # Gadgets and Star Powers array
        spgList = []
        for id, level in self.player.Brawler_level.items():
            if level == 8:
                spg = Cards.get_unlocked_spg(self, int(id))
                for i in range(len(spg)):
                    spgList.append(spg[i])
        self.writeVint(len(self.player.cardsSkillsID))  # count

        for skill_id in self.player.cardsSkillsID:
            self.writeVint(23)
            self.writeVint(skill_id)
            if skill_id in spgList:
                self.writeVint(1)
            else:
                self.writeVint(0)

        # "new" Brawler Tag array
        self.writeVint(0)  # brawlers count

        self.writeVint(self.player.gems)  # Gems
        self.writeVint(self.player.gems)  # Free Gems

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        # Tutorial Step
        self.writeVint(2)

        self.writeVint(0)
        print("OwnHomeData has been SENT!!")