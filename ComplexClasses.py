#classes always use upper case
class Overwatch_characters:
    """This class will take in Overwatch Characters playerclass, health,
    speed, and power"""
    def __init__(self, playerclass, health, speed, power):
        self.playerclass = playerclass
        self.health = health
        self.speed = speed
        self.power = power

    def __str__(self):
        return f"{self.playerclass} {self.health}"


class Healer(Overwatch_characters):
    """This class looks at differences in healer playerclass"""
    def __init__(self, playerclass, health, speed, power,
                 healspersec, ultimateheals, healrate):
        super().__init__(playerclass, health, speed, power)
        self.healspersec = healspersec
        self.ultimateheals = ultimateheals
        self.selfhealrate = healrate


class Attacker(Overwatch_characters):
    """This class looks at differences in DPS playerclass"""
    def __init__(self, playerclass, health, speed, power,
                 damagesec, damageult, gunrange):
        super().__init__(playerclass, health, speed, power)
        self.damagesec = damagesec
        self.damageult = damageult
        self.gunrange = gunrange


if __name__ == '__main__':
    p1 = Healer('paladin', 150, 50, 50, 15, 400, 120)
    p2 = Healer('mercy', 145, 60, 50, 20, 375, 115)
    print(p2)
