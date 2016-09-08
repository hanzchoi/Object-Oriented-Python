# from monster import Monster


class Monster:
    hit_points = 1
    color = 'yellow'
    weapon = 'sword'
    sound = 'roar'

    def battlecry(self):
        return self.sound.upper()

jubjub = Monster()
jubjub.battlecry()