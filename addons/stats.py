import discord
from discord.ext import commands
from sys import argv
from urllib.request import urlopen
import urllib.request
import requests
import math

class Stats:
    """
    Old School Runescape Lookup commands
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context=True)
    async def stats(self, ctx, *, rsn=""):
        """OSRS Stats Lookup. !stats <rsn>"""
        #rsn = rsn.replace(" ", "_")
        try:

            hiscores = "http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={}".format(rsn)
            response = urllib.request.urlopen(hiscores)
            stats = (response.read().decode('utf-8'))
            my_list = stats.split(',')
            meleeCombat = round(0.25 * (int(my_list[5]) + int(my_list[9]) + math.floor(int(my_list[13]) / 2  )) + 0.325 * (int(my_list[3]) + int(my_list[7])),2)
            rangeCombat = round(0.25 * (int(my_list[5]) + int(my_list[9]) + math.floor(int(my_list[13]) / 2  )) + 0.325 * math.floor((int(my_list[11]) / 2) + int(my_list[11])),2)
            magicCombat = round(0.25 * (int(my_list[5]) + int(my_list[9]) +     math.floor(int(my_list[13]) / 2  )) + 0.325 * math.floor((int(my_list[15]) /     2) + int(my_list[15])),2)
            if(rangeCombat > meleeCombat and rangeCombat > magicCombat):
                combat = rangeCombat
            elif(meleeCombat > rangeCombat and meleeCombat > magicCombat):
                combat = meleeCombat
            else:
                combat = magicCombat

            #Assign Stats
            overall = my_list[1]
            attack = my_list[3]
            defence = my_list[5]
            strength = my_list[7]
            hitpoints = my_list[9]
            range = my_list[11]
            prayer = my_list[13]
            magic = my_list[15]
            cooking = my_list[17]
            woodcutting = my_list[19]
            fletching = my_list[23]
            fishing = my_list[23]
            firemaking = my_list[25]
            crafting = my_list[27]
            smithing = my_list[29]
            mining = my_list[31]
            herblore = my_list[33]
            agility = my_list[35]
            thieving = my_list[37]
            slayer = my_list[39]
            farming = my_list[41]
            runecraft = my_list[43]
            hunter = my_list[45]
            construction = my_list[47]
            target_kills = my_list[51]
            await self.bot.say("[{0}]: **Combat {1}** | **Attack {2}** | **Defence {3}** | **Strength {4}** | **Hitpoints {5}** | **Range {6}** | **Prayer {7}** |** Magic {8}** | Cooking {9} | Woodcutting {10} | Fletching {11} | Fishing {12} | Firemaking {13} | Crafting {14} | Smithing {15} | Mining {16} | Herblore {17} | Agility {18} | Thieving {19} | Slayer {20} | Farming {21} | Runecraft {22}| Hunter {23} | Construction {24} | BH Target Kills {25}".format(rsn, combat, attack, defence, strength, hitpoints, range, prayer, magic, cooking, woodcutting, fletching, fishing, firemaking, crafting, smithing, mining, herblore, agility, thieving, slayer, farming, runecraft, hunter, construction, target_kills))
        except Exception:
            await self.bot.say("Could not find stats for ["+rsn+"]")

# Load the extension
def setup(bot):
    bot.add_cog(Stats(bot))

