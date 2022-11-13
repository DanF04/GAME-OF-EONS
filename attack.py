from character import Character
from condition import Condition

class Attack:

    # performs an attack from an attacker character to the enemy team character
    def do_attack(attacker:Character,attacked:Character):
        MyWP:int = attacker.weaponDamage
        EnemyAP:int = attacked.armor
        EnemyHP:int = attacked.hp
        Dmg:int = MyWP - EnemyAP
        if (Dmg < 0):
            Dmg = 0
        EnemyHP = EnemyHP - Dmg
        attacked.hp = EnemyHP
        if EnemyHP <= 0:
            attacked.set_Condition(Condition.Dead)