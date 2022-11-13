import pip
import random
from character import Character
import numpy as np

#from playsound import playsound
#playsound('audio.mp3')
"""
map1 = [ ["00","10","20","30","40","50","60","70","80"],
         ["01","11","21","31","41","51","61","71","81"], 
         ["02","12","22","32","42","52","62","72","82"],
         ["03","13","23","33","43","53","63","73","83"],
         ["04","14","24","34","44","54","64","74","84"],
         ["05","15","25","35","45","55","65","75","85"],
         ["06","16","26","36","46","56","66","76","86"],]
"""

"""
UpDown = 1
LeftRight = 1
"""
command = ""




def d20throw() -> int:
    return random.randint(1,20)

def TurnOrder(d20, init) -> int:
    return d20 + init

def selection_sort(x,y):
    for i in range(len(x)):   
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
        (y[i], y[swap]) = (y[swap], y[i])
    return x    
"""

Warrior = [1]
def Rushdown (MP):
    SpellEffectValue = -1 * (WP + d4)
    SpellMPCost: 5
Priest = [2]
def Exorcism (MP):
    SpellEffectValue = -1 * (d4 * 2)
    SpellMPCost: 5
def Mend (MP):
    SpellEffectvalue = d6 + WP
    SpellMPCost: 3
#TÊM DE SER 4
Orc_Warrior = [3]
MageSquad = [Orc_Warrior]
PlayerSquad = [Warrior, Priest]
Spell_Effect_Group =[MageSquad, PlayerSquad]
"""
"""
PlayerSquad = []
MageSquad = [] 
PlayerSquad.append(Warrior)
PlayerSquad.append(Priest)
print (list)
"""
"""
class InitiativePhase:
    pass


class Adventurer:

    def __init__(self, name, HP, MP, AP):
        self.name = name
        self.HP = 32
        self.MP = 5
        self.AP = 2
        self.WP = 5
        self.Init = 2
        print(f"Player {self.name} created")

    def __init__(self, name, HP, MP, AP):
        self.name = name
        self.HP = 20
        self.MP = 25
        self.AP = 0
        self.WP = 2
        self.Init = 6
        print(f"Player {self.name} created")
    
    def attack (Dmg):
        Dmg = MyWP - EnemyAP
        if (Dmg > 0):
            Dmg == 0
        for i in range (0,len(MageSquad)):
            if MageSquad[0]:
                EnemyHP = EnemyHP - Dmg
                if EnemyHP <= 0:
                    MageSquad.remove(0)
                    
    def magic ():
        MyMP >= SpellMPCost
        for i in range (0,len(Spell_Effect_Group)):
            if Spell_Effect_Group[0]:
                for i in range (0, MageSquad):
                    if MageSquad[0]:
                        EnemyHP = EnemyHP + SpellEffectValue
                        MyMP = MyMP - SpellMPCost
                        if EnemyHP <= 0:
                            MageSquad.remove(0)
            if Spell_Effect_Group[1]:
                for i in range (0, PlayerSquad):
                    if PlayerSquad[0]:
                        ChosenHP = ChosenHP + SpellEffectValue
                        MyMP = MyMP - SpellMPCost
                    elif PlayerSquad[1]:
                        ChosenHP = ChosenHP + SpellEffectValue
                        MyMP = MyMP - SpellMPCost



class Monster(Orc_Warrior):
    def __init__(self, name, HP, MP, AP):
        self.name = name
        self.HP = 15
        self.MP = 0
        self.AP = 2
        self.WP = 2
        self.Init = 2
        print(f"Player {self.name} created")


"""
#squad player
_warrior = Character ("warrior", 32,5,2,5,2)
_priest = Character ("priest", 20,5,0,2,6)
#squad mage
_orc1 = Character("orc1", 15,10,2,5,6)
_orc2 = Character("orc2", 20,10,2,5,6)
_orc3 = Character("orc3", 15,10,2,5,6)
_orc4 = Character("orc4", 20,10,2,5,6)
def print_characters_info(c:Character):
    print(c.to_string())
All_characters = [_warrior,_priest,_orc1,_orc2,_orc3,_orc4]

turn_order_info=[0] * len(All_characters)

for i in range(0, len(All_characters)):
    turn_order_info[i] = TurnOrder(d20throw(),All_characters[i].Initiative())
    All_characters[i].set_OrderTurn(turn_order_info[i])
  
selection_sort(turn_order_info,All_characters)

turn_order_info = turn_order_info[::-1]
All_characters = All_characters[::-1]

for i in range(0, len(turn_order_info)):
    print(turn_order_info[i])

#print(TurnOrder(int(d20throw()),int(c.Initiative())))
print("YOUR SQUAD:")
print_characters_info(_warrior)
print_characters_info(_priest)
print("ENEMY SQUAD:")
print_characters_info(_orc1)
print_characters_info(_orc2)
print_characters_info(_orc3)
print_characters_info(_orc4)

print("")
for i in range(0, len(All_characters)):
    print(All_characters[i].to_string())

"""
while (command != "exit"):

    print("You are in " + map1[UpDown][LeftRight])
    print("Where do you want to go?")
    
    command = input()
    if (command == "east"):
        if(LeftRight + 1 > 2):
            LeftRight = 2
            print ("You can't go further")
        else:
            LeftRight = LeftRight + 1
    if (command == "west"):
        if(LeftRight - 1 < 0):
            LeftRight = 0
            print ("You can't go further")
        else:
            LeftRight = LeftRight - 1
    if (command == "south"):
        if(UpDown + 1 > 2):
            UpDown = 2
            print ("You can't go further")
        else:
            UpDown = UpDown + 1
    if (command == "north"):
        if(UpDown - 1 < 0):
            UpDown = 0
            print ("You can't go further")
        else:
            UpDown = UpDown - 1
    if (UpDown == 2 and LeftRight == 1):
        pass
"""