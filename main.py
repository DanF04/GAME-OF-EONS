#######################################################
#                                                     #
#  GAME OF EONS by Daniel Fernandes and Vasco Caleiro #
#                                                     #
#  Version 1.1b - Release Date: 2022/11/13            #
#                                                     #
#######################################################

## ref. to helping packages                                               
import random
import numpy as np


## ref. to project defined classes
from spell import Spell
from spellname import SpellName
from character import Character
from team import Team
from condition import Condition
from attack import Attack


## functions definitions

# 20 sided dice throw simulation
def d20throw() -> int:
    return random.randint(1,20)

# the following func obtains the result of the turnorder by using the d20 dice throw result and the character init value
def GetTurnOrder(d20, init) -> float:
    return (10 * (d20 + init) + init) / 10
    # note: the multiplication and division by 10 is used to try to resolve ties adding the init value again but with lower relevance (the result is a number with decimals)

# sorter of elements in a list (array) using the values of another corresponding list (helper array) as means of comparision: only one is evalued but the two will suffer the same swaps of elements
# in the end this result on both lists is ordered ascending or descending according to parameter descendingOrder
def sortElements(baseElements,elementsToSort,descendingOrder:bool):
    for i in range(len(baseElements)):   
        swap = i + np.argmin(baseElements[i:])
        (baseElements[i], baseElements[swap]) = (baseElements[swap], baseElements[i])
        (elementsToSort[i], elementsToSort[swap]) = (elementsToSort[swap], elementsToSort[i])
    if descendingOrder:
        elementsToSort = elementsToSort[::-1]
    return elementsToSort

# selects a character from a team randomly
def selectRandomCharacterFromTeam(TeamCharacters):
    AliveTeamCharacters = []
    for i in range(0, len(TeamCharacters)):
        if TeamCharacters[i].MyCondition()==Condition.Alive:
            AliveTeamCharacters.append(TeamCharacters[i])
    return AliveTeamCharacters[random.randint(0, len(AliveTeamCharacters)-1)]

# determines if there is at least one element not dead per team
def AllTeamsStillStand(TeamCharacters) -> bool:
    death_cnt:int
    team_cnt:int
    team_cond = [Condition.Alive,Condition.Alive] #[Player Team Condition, Wizard Team Condition]
    for j in range(0, len(TeamCharacters)):
        death_cnt = 0
        team_cnt = len(TeamCharacters[j])
        for i in range(0, len(TeamCharacters[j])):
            if TeamCharacters[j][i].MyCondition()==Condition.Dead:
                death_cnt = death_cnt + 1
        if death_cnt==team_cnt: #all elements are dead in the j team
                team_cond[j]=Condition.Dead
    return (team_cond[Team.Player]==Condition.Alive and team_cond[Team.Wizard]==Condition.Alive)

# obtains the winner team by determining which team has no elements left alive
def TeamVictorius(TeamCharacters) -> Team:
    death_cnt:int
    team_cnt:int
    team_cond = [Condition.Alive,Condition.Alive] #[Player Team Condition, Wizard Team Condition]
    for j in range(0, len(TeamCharacters)):
        death_cnt = 0
        team_cnt = len(TeamCharacters[j])
        for i in range(0, len(TeamCharacters[j])):
            if TeamCharacters[j][i].MyCondition()==Condition.Dead:
                death_cnt = death_cnt + 1 #end for i
        if death_cnt==team_cnt: #all elements are dead in the j team
                team_cond[j]=Condition.Dead #end for j
    if not (team_cond[Team.Player]==Condition.Alive and team_cond[Team.Wizard]==Condition.Alive):
        ret = Team.Wizard if team_cond[Team.Player]==Condition.Dead else Team.Player

    return ret

# determines if there are more than 1 character dead in a team
def MoreThanOneAreDead(TeamCharacters) -> bool :
    death_cnt:int = 0
    for j in range(0, len(TeamCharacters)):
        if TeamCharacters[j].MyCondition()==Condition.Dead:
            death_cnt = death_cnt + 1 
    return (death_cnt > 1)


## Definition and initialization of main data structures

Teams = [Team.Player,Team.Wizard]

#team player elements  (name,hp,mana,armor,wp_dmg,init,team,spell 1,spell 2)
_warrior = Character("Warrior", 32,5,2,5,2,Team.Player,SpellName.Rushdown,SpellName.none)
_priest = Character("Priest", 20,13,0,2,4,Team.Player,SpellName.Exorcism,SpellName.Mend)
_paladine = Character("Paladin", 40,9,6,8,1,Team.Player,SpellName.Rushdown,SpellName.Mend)
_archer = Character("Archer", 25,0,2,7,6,Team.Player,SpellName.none,SpellName.none)
_teamPlayer = [_warrior,_priest,_paladine,_archer]

#team wizard elements  (name,hp,mana,armor,wp_dmg,init,team,spell 1,spell 2)
_orc1 = Character("Orc1", 15,0,2,3,2,Team.Wizard,SpellName.none,SpellName.none)
_orc2 = Character("Orc2", 15,0,2,2,2,Team.Wizard,SpellName.none,SpellName.none)
_orc3 = Character("Orc3", 15,0,2,4,2,Team.Wizard,SpellName.none,SpellName.none)
_orc4 = Character("Orc4", 15,0,2,1,2,Team.Wizard,SpellName.none,SpellName.none)
_omag = Character("Ogre-Mage", 10,16,1,1,1,Team.Wizard,SpellName.DarkMagic,SpellName.DarkMend)
_troll = Character("Troll", 30,0,6,9,0,Team.Wizard,SpellName.none,SpellName.none)
_witch = Character("Witch", 15,20,2,3,3,Team.Wizard,SpellName.WitchCraftRevive,SpellName.none)
_teamWizard = [_orc1,_orc2,_orc3,_orc4,_omag,_troll,_witch]

# list (array) that contains all character of all teams to be used in rounds
All_characters = [_warrior,_priest,_paladine,_archer,_orc1,_orc2,_orc3,_orc4,_omag,_troll,_witch]

# helper list of both teams
TeamCharacters = [_teamPlayer,_teamWizard]

# list to store turn order values and help with the sorting function
turn_order_info=[0] * len(All_characters)


##### MAIN EXECUTION SECTION STARTS HERE!!!! #####

print("")
print(" #######################")
print(" WELCOME TO GAME OF EONS")
print(" #######################")
print("")

# show all teams characters status
print(" Player Team:")
for i in range(0, len(_teamPlayer)):
   print(_teamPlayer[i].showStatus())
print()
print(" Wizard Team (bot):")
for i in range(0, len(_teamWizard)):
    print(_teamWizard[i].showStatus())
print()

command = input(" <PRESS ANY KEY TO BEGIN>")
print()

#ROUND CYCLE
roundNr = 1
command = ""

# main cycle
while AllTeamsStillStand(TeamCharacters) and command!="exit":

    #INITIATIVE PHASE
    #TURNORDER

    # stores turn order values
    for i in range(0, len(All_characters)):
        turn_order_info[i] = GetTurnOrder(d20throw(),All_characters[i].Initiative())
        All_characters[i].set_OrderTurn(turn_order_info[i])
  
    # sort character by they turn order value
    All_characters = sortElements(turn_order_info,All_characters,True)

    print(" ROUND " + str(roundNr) + " TURN ORDER:")
    cntAlive = 0
    # show turn order results for characters
    for i in range(1, len(All_characters)+1):
        if All_characters[i-1].MyCondition() in (Condition.Alive,Condition.Zombie):
            cntAlive = cntAlive + 1
            print("\t" + str(cntAlive) + ("st" if cntAlive==1 else ("nd" if cntAlive==2 else ("rd" if cntAlive==3 else "th"))) + " to play: " + All_characters[i-1].MyName() + " (T.O. obtained: " + str(All_characters[i-1].OrderTurn()) + ")")
    print()

    #ATTACK PHASE
    print(" ROUND " + str(roundNr) + " ACTION:")

    # attack/spell cycle: cycles through all characters in all teams by the pre-defined turn order
    for i in range(0, len(All_characters)):
        # evaluates and only continues if character is not dead - note: zombies are considered not dead!
        if All_characters[i].MyCondition() in (Condition.Alive,Condition.Zombie):
            #TEAM PLAYER
            # evaluates if character is in player team and if there is at least one element not dead per team (to prevent the continuation of the game when a team has already lost)
            if All_characters[i].MyTeam()==Team.Player and AllTeamsStillStand(TeamCharacters):
                s:str = " > What do you want " + All_characters[i].MyName() +  " to do? "
                # gives a choice to player according to character's current mana value
                if All_characters[i].mana > 0:
                    s = s + "{Attack [1]} {Magic [2]} : "
                else:
                    s = s + "{Attack [1]} : "
                ask:str = input(s)
                # player chose attack
                if ask == "1":
                    s:str = " > Which enemy do you want " + All_characters[i].MyName() + " to attack? "
                    enemiesAlive = []
                    cntAlive = 0
                    # cycles through Wizard team characters to find only the ones not dead and stores in enemiesAlive
                    for j in range (0, len(TeamCharacters[Team.Wizard])):
                        if TeamCharacters[Team.Wizard][j].MyCondition() in (Condition.Alive,Condition.Zombie):
                            cntAlive = cntAlive + 1
                            s = s + "{" + TeamCharacters[Team.Wizard][j].MyName() + " [" + str(cntAlive) + "]} "
                            enemiesAlive.append(TeamCharacters[Team.Wizard][j])
                    s = s + ": "
                    ask2:str = input(s)
                    # performs an attack on an Wizard team character according to players choice
                    Attack.do_attack(All_characters[i],enemiesAlive[int(ask2)-1])
                    print("\t" + All_characters[i].MyName() + " attacks " + enemiesAlive[int(ask2)-1].MyName() + " : " + enemiesAlive[int(ask2)-1].MyName() + "'s HP = " + str(enemiesAlive[int(ask2)-1].hp)) 
                # player chose magic
                if ask == "2":
                    ask3:str = input(" > Which spell do you want to use from " + All_characters[i].MyName() + "? " + All_characters[i].showSpells() + ": ")
                    # player chose spell 1
                    if ask3 == "1":
                        if All_characters[i].spell1 == SpellName.Exorcism:
                            s:str = " > Which enemy do you want " + All_characters[i].MyName() + " to use the Exorcism on? "
                            enemiesAlive = []
                            cntAlive = 0
                            # cycles through Wizard team characters to find only the ones not dead and stores in enemiesAlive
                            for j in range (0, len(TeamCharacters[Team.Wizard])):
                                if TeamCharacters[Team.Wizard][j].MyCondition() in (Condition.Alive,Condition.Zombie):
                                    cntAlive = cntAlive + 1
                                    s = s + "{" + TeamCharacters[Team.Wizard][j].MyName() + " [" + str(cntAlive) + "]} "
                                    enemiesAlive.append(TeamCharacters[Team.Wizard][j])
                            s = s + ": "
                            ask4:str = input(s)
                            # performs a spell on a Wizard team character according to players choice
                            Spell.do_exorcism(All_characters[i],enemiesAlive[int(ask4)-1])
                            print("\t" + All_characters[i].MyName() + " uses Exorcism on " + enemiesAlive[int(ask4)-1].MyName() + " : " + enemiesAlive[int(ask4)-1].MyName() + "'s HP = " + str(enemiesAlive[int(ask4)-1].hp))          
                        elif All_characters[i].spell1 == SpellName.Rushdown:
                            s:str = " > Which enemy do you want " + All_characters[i].MyName() + " to use the Rushdown on? "
                            enemiesAlive = []
                            cntAlive = 0
                            # cycles through Wizard team characters to find only the ones not dead and stores in enemiesAlive
                            for j in range (0, len(TeamCharacters[Team.Wizard])):
                                if TeamCharacters[Team.Wizard][j].MyCondition() in (Condition.Alive,Condition.Zombie):
                                    cntAlive = cntAlive + 1
                                    s = s + "{" + TeamCharacters[Team.Wizard][j].MyName() + " [" + str(cntAlive) + "]} "
                                    enemiesAlive.append(TeamCharacters[Team.Wizard][j])
                            s = s + ": "
                            ask4:str = input(s)
                            # performs a spell on a Wizard team character according to players choice
                            Spell.do_rushdown(All_characters[i],enemiesAlive[int(ask4)-1])
                            print("\t" + All_characters[i].MyName() + " uses Rushdown on " + enemiesAlive[int(ask4)-1].MyName() + " : " + enemiesAlive[int(ask4)-1].MyName() + "'s HP = " + str(enemiesAlive[int(ask4)-1].hp))
                        elif All_characters[i].spell1 == SpellName.Mend:
                            s:str = " > Which ally do you want " + All_characters[i].MyName() + " to use the Mend on? "
                            alliesAlive = []
                            cntAlive = 0
                             # cycles through Player team characters to find only the ones not dead and stores in alliesAlive
                            for j in range (0, len(TeamCharacters[Team.Player])):
                                if TeamCharacters[Team.Player][j].MyCondition() == Condition.Alive:
                                    cntAlive = cntAlive + 1
                                    s = s + "{" + TeamCharacters[Team.Player][j].MyName() + " [" + str(cntAlive) + "]} "
                                    alliesAlive.append(TeamCharacters[Team.Player][j])
                            s = s + ": "
                            ask4:str = input(s)
                            # performs a spell on a Player team character according to players choice
                            Spell.do_mend(All_characters[i],alliesAlive[int(ask4)-1])
                            print("\t" + All_characters[i].MyName() + " uses Mend on " + alliesAlive[int(ask4)-1].MyName() + " : " + alliesAlive[int(ask4)-1].MyName() + "'s HP = " + str(alliesAlive[int(ask4)-1].hp))         
                    # player chose spell 2
                    elif ask3 == "2":
                        if All_characters[i].spell2 == SpellName.Exorcism:
                            s:str = " > Which enemy do you want " + All_characters[i].MyName() + " to use the Exorcism on? "
                            enemiesAlive = []
                            cntAlive = 0
                            # cycles through Wizard team characters to find only the ones not dead and stores in enemiesAlive
                            for j in range (0, len(TeamCharacters[Team.Wizard])):
                                if TeamCharacters[Team.Wizard][j].MyCondition() in (Condition.Alive,Condition.Zombie):
                                    cntAlive = cntAlive + 1
                                    s = s + "{" + TeamCharacters[Team.Wizard][j].MyName() + " [" + str(cntAlive) + "]} "
                                    enemiesAlive.append(TeamCharacters[Team.Wizard][j])
                            s = s + ": "
                            ask4:str = input(s)
                            # performs a spell on an Wizard team character according to players choice
                            Spell.do_exorcism(All_characters[i],enemiesAlive[int(ask4)-1])
                            print("\t" + All_characters[i].MyName() + " uses Exorcism on " + enemiesAlive[int(ask4)-1].MyName() + " : " + enemiesAlive[int(ask4)-1].MyName() + "'s HP = " + str(enemiesAlive[int(ask4)-1].hp))
                        elif All_characters[i].spell2 == SpellName.Rushdown:
                            s:str = " > Which enemy do you want " + All_characters[i].MyName() + " to use the Rushdown on? "
                            enemiesAlive = []
                            cntAlive = 0
                            # cycles through Wizard team characters to find only the ones not dead and stores in enemiesAlive
                            for j in range (0, len(TeamCharacters[Team.Wizard])):
                                if TeamCharacters[Team.Wizard][j].MyCondition() in (Condition.Alive,Condition.Zombie):
                                    cntAlive = cntAlive + 1
                                    s = s + "{" + TeamCharacters[Team.Wizard][j].MyName() + " [" + str(cntAlive) + "]} "
                                    enemiesAlive.append(TeamCharacters[Team.Wizard][j])
                            s = s + ": "
                            ask4:str = input(s)
                            # performs a spell on an Wizard team character according to players choice
                            Spell.do_rushdown(All_characters[i],enemiesAlive[int(ask4)-1])
                            print("\t" + All_characters[i].MyName() + " uses Rushdown on " + enemiesAlive[int(ask4)-1].MyName() + " : " + enemiesAlive[int(ask4)-1].MyName() + "'s HP = " + str(enemiesAlive[int(ask4)-1].hp))
                        elif All_characters[i].spell2 == SpellName.Mend:
                            s:str = " > Which ally do you want " + All_characters[i].MyName() + " to use the Mend on? "
                            alliesAlive = []
                            cntAlive = 0
                            # cycles through Player team characters to find only the ones not dead and stores in alliesAlive
                            for j in range (0, len(TeamCharacters[Team.Player])):
                                if TeamCharacters[Team.Player][j].MyCondition() == Condition.Alive:
                                    cntAlive = cntAlive + 1
                                    s = s + "{" + TeamCharacters[Team.Player][j].MyName() + " [" + str(cntAlive) + "]} "
                                    alliesAlive.append(TeamCharacters[Team.Player][j])
                            s = s + ": "
                            ask4:str = input(s)
                            # performs a spell on a Player team character according to players choice
                            Spell.do_mend(All_characters[i],alliesAlive[int(ask4)-1])
                            print("\t" + All_characters[i].MyName() + " uses Mend on " + alliesAlive[int(ask4)-1].MyName() + " : " + alliesAlive[int(ask4)-1].MyName() + "'s HP = " + str(alliesAlive[int(ask4)-1].hp))         
                   
            #TEAM WIZARD (BOT)
            #  evaluates if character is in player team and if there is at least one element not dead per team (to prevent the continuation of the game when a team has already lost) 
            #  also evaluates and only continues if character is not dead - note: zombies are considered not dead! 
            if All_characters[i].MyTeam()==Team.Wizard and AllTeamsStillStand(TeamCharacters) and All_characters[i].MyCondition() in (Condition.Alive,Condition.Zombie) :
                cn = All_characters[i].MyName()
                # check if the character has any spell and it's current mana value is above 0
                if (not (All_characters[i].MySpell1() == SpellName.none and All_characters[i].MySpell2() == SpellName.none)) and All_characters[i].mana > 0 :

                    if (random.randint(1,2) == 1) or (random.randint(1,2) == 2 and All_characters[i].mana <= 0): #random decision to attack
                        tc:Character = selectRandomCharacterFromTeam(TeamCharacters[Team.Player])
                        Attack.do_attack(All_characters[i],tc)
                        print("\t" + All_characters[i].MyName() + " attacks " + tc.MyName() + " : " + tc.MyName() + "'s HP = " + str(tc.hp))
                    else: #random decision to spell
                        if ((All_characters[i].MySpell2() == SpellName.none) or (random.randint(1,2) == 1)) : # character has no spell2 or random decision to which spell is 1
                            if All_characters[i].MySpell1() == SpellName.DarkMagic:
                                Spell.do_dark_magic(All_characters[i],TeamCharacters[Team.Player])
                                print("\t" + All_characters[i].MyName() + " uses Dark Magic on all opponents : ")
                                for j in range (0, len(TeamCharacters[Team.Player])):
                                    if TeamCharacters[Team.Player][j].MyCondition() == Condition.Alive:
                                        print("\t\t" + TeamCharacters[Team.Player][j].MyName() + "'s HP = " + str(TeamCharacters[Team.Player][j].hp))  
                            if All_characters[i].MySpell1() == SpellName.WitchCraftRevive:
                                # check if there is more than 1 characters dead on Wizard team
                                if MoreThanOneAreDead(TeamCharacters[Team.Wizard]): 
                                    Spell.do_witch_craft_revive(All_characters[i],TeamCharacters[Team.Wizard])
                                    print("\t" + All_characters[i].MyName() + " uses WitchCraft Revive : ")
                                    for j in range (0, len(TeamCharacters[Team.Wizard])):
                                        if TeamCharacters[Team.Wizard][j].MyCondition() == Condition.Zombie:
                                            print("\t\t" + TeamCharacters[Team.Wizard][j].MyName() + " became zombie... " )
                                else: # there's less than 2 characters dead on Wizard team
                                    tc:Character = selectRandomCharacterFromTeam(TeamCharacters[Team.Player])
                                    # performs an attack on a randomly selected Player team character
                                    Attack.do_attack(All_characters[i],tc)
                                    print("\t" + All_characters[i].MyName() + " attacks " + tc.MyName() + " : " + tc.MyName() + "'s HP = " + str(tc.hp))
                        else:
                            if All_characters[i].spell2 == SpellName.DarkMend:
                                Spell.do_dark_mend(All_characters[i],TeamCharacters[Team.Wizard])
                                print("\t" + All_characters[i].MyName() + " uses Dark Mend on all team elements : ")
                                for j in range (0, len(TeamCharacters[Team.Wizard])):
                                    if TeamCharacters[Team.Wizard][j].MyCondition() == Condition.Alive:
                                        print("\t\t" + TeamCharacters[Team.Wizard][j].MyName() + "'s HP = " + str(TeamCharacters[Team.Wizard][j].hp))  
                else:        
                    tc:Character = selectRandomCharacterFromTeam(TeamCharacters[Team.Player])
                    # performs an attack on a randomly selected Player team character
                    Attack.do_attack(All_characters[i],tc)
                    print("\t" + All_characters[i].MyName() + " attacks " + tc.MyName() + " : " + tc.MyName() + "'s HP = " + str(tc.hp))  

    # attack/spell cycle END

    print()

    print(" ROUND " + str(roundNr) + " RESULTS:")
    print()
    print(" Player Team:")
    for i in range(0, len(_teamPlayer)):
       print(_teamPlayer[i].showResumedStatus())
    print()
    print(" Wizard Team (bot):")
    for i in range(0, len(_teamWizard)):
        print(_teamWizard[i].showResumedStatus())
    print()

    # check if a team won
    if not AllTeamsStillStand(TeamCharacters):
        print(" ***** GAME OVER: TEAM WIZARD WINS *****" if TeamVictorius(TeamCharacters)==Team.Wizard else " ***** GAME OVER: TEAM PLAYER WINS *****")
        print()
        #command = input(" <PRESS ANY KEY TO EXIT>")
        break #ends execution

    command = input(" <PRESS ANY KEY FOR NEXT ROUND>")
    print()
    roundNr = roundNr + 1
# end of main cycle

    

