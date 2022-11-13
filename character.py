from spellname import SpellName
from team import Team
from condition import Condition

class Character:
    
    def __init__(self, name: str, hp: int, mana: int, armor, weaponDamage: int, initiative: int, team: Team, spell1: SpellName, spell2: SpellName):
        self.name:str = name
        self.hp:int = hp
        self.mana:int = mana
        self.armor:int = armor
        self.weaponDamage:int = weaponDamage
        self.initiative:int  = initiative
        self.orderturn:int = 0
        self.team:Team = team
        self.condition:Condition = Condition.Alive
        self.spell1:SpellName = spell1
        self.spell2:SpellName = spell2

    def showStatus(self) -> str:
        strStat = str()
        strStat = strStat + " [Name: " + Character.FixToLenghtWithSpaces(self,str(self.name),10) + "] "
        strStat = strStat + "[HP: " + Character.FixToLenghtWithSpaces(self,str(self.hp),2) + "] "
        strStat = strStat + "[Mana: " + Character.FixToLenghtWithSpaces(self,str(self.mana),2) + "] "
        strStat = strStat + "[Armor: " + str(self.armor) + "] "
        strStat = strStat + "[Weapon Damage: " + str(self.weaponDamage) + "] "
        strStat = strStat + "[Init: " + str(self.initiative) + "] "
        strStat = strStat + "[Condition: " + str(self.condition) + "] "
        strStat = strStat + "[Spell(s): " 
        if self.spell1 != SpellName.none:
            strStat = strStat + str(self.spell1) 
        if self.spell2 !=  SpellName.none:
            strStat = strStat + " & " + str(self.spell2) 
        strStat = strStat + "]"
        return strStat

    def showResumedStatus(self) -> str:
        strStat = str()
        strStat = strStat + " [Name: " + Character.FixToLenghtWithSpaces(self,str(self.name),10) + "] "
        strStat = strStat + "[HP: " + Character.FixToLenghtWithSpaces(self,str(self.hp),2) + "] "
        strStat = strStat + "[Mana: " + Character.FixToLenghtWithSpaces(self,str(self.mana),2) + "] "
        strStat = strStat + "[Armor: " + str(self.armor) + "] "
        strStat = strStat + "[Weap.Damage: " + str(self.weaponDamage) + "] "
        strStat = strStat + "[Cond.: " + str(self.condition) + "] "
        strStat = strStat + "[Spell(s): " 
        if self.spell1 != SpellName.none:
            strStat = strStat + str(self.spell1) 
        if self.spell2 !=  SpellName.none:
            strStat = strStat + " & " + str(self.spell2) 
        strStat = strStat + "]"
        return strStat
    
    def showSpells(self) -> str:
        strStat = str()
        strStat = strStat + "{" 
        if self.spell1 != SpellName.none:
            strStat = strStat + str(self.spell1) + " [1]} "
        if self.spell2 !=  SpellName.none:
            strStat = strStat + "{" + str(self.spell2) + " [2]} "
        return strStat

    # used to fix print length of a string
    def FixToLenghtWithSpaces(self, string_to_fix:str, final_len:int) -> str:
        n_missing = final_len - len(string_to_fix)
        for i in range(0, n_missing):
            string_to_fix = string_to_fix + " "
        return string_to_fix    
    
    def Initiative(self) -> int:
        return self.initiative

    def MyName(self) -> str:
        return self.name

    def MyTeam(self) -> Team:
        return self.team

    def MyCondition(self) -> Team:
        return self.condition

    def OrderTurn (self) -> int:
        return self.orderturn
        
    def set_OrderTurn(self, ot:int):
        self.orderturn = ot

    def set_Condition(self, cnd:Condition):
        self.condition = cnd

    def MySpell1(self) -> SpellName:
        return self.spell1

    def MySpell2(self) -> SpellName:
        return self.spell2