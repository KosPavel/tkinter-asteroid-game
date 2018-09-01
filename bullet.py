import math

import settings
from player import Player

class Bullet(Player):

    def __init__(self, pos_x, pos_y, alpha):
        '''
        Bullet creates with x,y as start position
        and alpha as direction angle
        '''
        self.position_x = pos_x
        self.position_y = pos_y
        self.new_x = 0
        self.new_y = 0
        self.alpha = alpha

        self.outline = 'red'
        self.fill = 'yellow'

        self.BULLET_SPEED = 15

    def shape(self):
        shape = [
        self.position_x,
        self.position_y,
                ]

    def direction(self):
        self.new_x = self.BULLET_SPEED * math.cos(math.radians(self.alpha))
                        + self.position_x
        self.new_y = self.BULLET_SPEED * math.sin(math.radians(self.alpha))
                        + self.position_y
