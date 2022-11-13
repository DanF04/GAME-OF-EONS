import random
from character import Character
from condition import Condition

class Spell:

    def d4throw() -> int:
        return random.randint(1,4)

    def d6throw() -> int:
        return random.randint(1,6)

    def do_rushdown(user:Character,receiver:Character):
        MyWP:int = user.weaponDamage
        EnemyHP:int = receiver.hp
        SpellEffectValue = MyWP + Spell.d4throw()
        #SpellMPCost: 5
        MyMANA:int = user.mana
        MyMANA = MyMANA - 5
        if (MyMANA < 0):
            MyMANA = 0
        user.mana = MyMANA
        EnemyHP = EnemyHP - SpellEffectValue
        receiver.hp = EnemyHP
        if EnemyHP <= 0:
            receiver.set_Condition(Condition.Dead)

    def do_exorcism(user:Character,receiver:Character):
        EnemyHP:int = receiver.hp
        SpellEffectValue = Spell.d4throw() * 2
        #SpellMPCost: 5
        MyMANA:int = user.mana
        MyMANA = MyMANA - 5
        if (MyMANA < 0):
            MyMANA = 0
        user.mana = MyMANA
        EnemyHP = EnemyHP - SpellEffectValue
        receiver.hp = EnemyHP
        if EnemyHP <= 0:
            receiver.set_Condition(Condition.Dead)

    def do_mend(user:Character,receiver:Character):
        AllyHP:int = receiver.hp
        MyWP:int = user.weaponDamage
        Spelleffectvalue = Spell.d6throw() + MyWP 
        #SpellMPCost: 3
        MyMANA:int = user.mana
        MyMANA = MyMANA - 3
        if (MyMANA < 0):
            MyMANA = 0
        user.mana = MyMANA
        if (Spelleffectvalue < 0):
            Spelleffectvalue = 0
        AllyHP = AllyHP + Spelleffectvalue
        receiver.hp = AllyHP

    def do_dark_magic(user:Character,player_team):
        elementsAlive = []
        for j in range (0, len(player_team)):
            if player_team[j].MyCondition() == Condition.Alive:
                elementsAlive.append(player_team[j])
        for j in range (0, len(elementsAlive)):
            EnemyHP:int = elementsAlive[j].hp
            SpellEffectValue = 4
            #SpellMPCost: 8
            MyMANA:int = user.mana
            MyMANA = MyMANA - 8
            if (MyMANA < 0):
                MyMANA = 0
            user.mana = MyMANA
            EnemyHP = EnemyHP - SpellEffectValue
            elementsAlive[j].hp = EnemyHP
            if EnemyHP <= 0:
                elementsAlive[j].set_Condition(Condition.Dead)
    
    def do_dark_mend(user:Character,wizard_team):
        elementsAlive = []
        for j in range (0, len(wizard_team)):
            if wizard_team[j].MyCondition() == Condition.Alive:
                elementsAlive.append(wizard_team[j])
        for j in range (0, len(elementsAlive)):
            elementHP:int = elementsAlive[j].hp
            SpellEffectValue = 2
            #SpellMPCost: 4
            MyMANA:int = user.mana
            MyMANA = MyMANA - 4
            if (MyMANA < 0):
                MyMANA = 0
            user.mana = MyMANA
            elementHP = elementHP + SpellEffectValue
            elementsAlive[j].hp = elementHP
    
    def do_witch_craft_revive(user:Character,wizard_team):
        elementsDead = []
        for j in range (0, len(wizard_team)):
            if wizard_team[j].MyCondition() == Condition.Dead:
                elementsDead.append(wizard_team[j])
        for j in range (0, len(elementsDead)):
            elementHP:int = elementsDead[j].hp
            SpellEffectValue = 2
            #SpellMPCost: 5
            MyMANA:int = user.mana
            MyMANA = MyMANA - 2
            if (MyMANA < 0):
                MyMANA = 0
            user.mana = MyMANA
            elementHP = SpellEffectValue  #REVIVE
            elementsDead[j].hp = elementHP
            elementsDead[j].condition = Condition.Zombie
            elementsDead[j].armor = 0
            elementsDead[j].weaponDamage = 6
            elementsDead[j].mana = 0