# from monster import Monster
import random

COLOR = ['yellow', 'red', 'blue', 'green']


class Monster:
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    hit_points = 1



    color = 'yellow'
    weapon = 'sword'
    sound = 'roar'

    def battlecry(self):
        return self.sound.upper()

jubjub = Monster()
jubjub.battlecry()