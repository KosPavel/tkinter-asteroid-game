import math

import settings

class Player():

    def __init__(self, root):
        self.position_x = settings.pos_x
        self.position_y = settings.pos_y
        self.mouse_x = 0
        self.mouse_y = 0
        self.phi = 270               #angle in degrees for ship rotation
        self.DELTA_PHI = 5
        self.SIZE_CONST = 15         #const for ship size regulation
        self.alpha = 270             #angle for speed vector calculation
        self.DELTA_ALPHA = 5
        self.movement_speed = 0      #current speed value, pixels/tick
        self.DELTA_MOVEMENT_SPEED = 1
        self.MOVEMENT_SPEED_MAX = 4  #maximum speed value
        self.MOVEMENT_SPEED_MIN = -3 #minimum speed value

        self.outline = 'red'
        self.fill = 'green'

        '''
        speed vector contains ship coordinates of the next tick
        '''
        self.speed_vector = [self.position_x, self.position_y]

        root.bind('<w>',self.moveForward)
        root.bind('<s>',self.moveBackward)
        root.bind('<a>',self.rotateLeft)
        root.bind('<d>',self.rotateRight)
        root.bind('<Motion>', self.mouseCoords)
        root.bind('<Button-1>', self.shoot)

        '''
        Below we are calculating ship form as triangle. Each point
        calculated using angle phi for future simple realization of rotation.
        '''

    def shape(self):
        shape = [
        self.position_x + self.SIZE_CONST * math.cos(math.radians(self.phi)),
        self.position_y + self.SIZE_CONST * math.sin(math.radians(self.phi)),
        self.position_x + self.SIZE_CONST * math.cos(math.radians(self.phi)-60),
        self.position_y + self.SIZE_CONST * math.sin(math.radians(self.phi)-60),
        self.position_x + self.SIZE_CONST * math.cos(math.radians(self.phi)+60),
        self.position_y + self.SIZE_CONST * math.sin(math.radians(self.phi)+60),
                ]
        return shape

    def moveForward(self, event):
        if self.movement_speed < self.MOVEMENT_SPEED_MAX:
            self.movement_speed += self.DELTA_MOVEMENT_SPEED
        if (self.movement_speed != 0 and self.movement_speed > self.inercia):
            self.inercia += self.DELTA_INERCIA

    def moveBackward(self, event):
        if self.movement_speed > self.MOVEMENT_SPEED_MIN:
            self.movement_speed -= self.DELTA_MOVEMENT_SPEED
        if (self.movement_speed != 0 and self.movement_speed < self.inercia):
            self.inercia -= self.DELTA_INERCIA

    def rotateLeft(self, event):
        if self.movement_speed >= 0:
            self.phi -= self.DELTA_PHI
        else:
            self.phi += self.DELTA_PHI
        if self.phi < 0:
            self.phi = 360
        if self.phi > 360:
            self.phi = 0
        print('Phi = ' + str(self.phi))

    def rotateRight(self, event):
        if self.movement_speed >= 0:
            self.phi += self.DELTA_PHI
        else:
            self.phi -= self.DELTA_PHI
        if self.phi > 360:
            self.phi = 0
        if self.phi < 0:
            self.phi = 360
        print('Phi = ' + str(self.phi))

    def mouseCoords(self, event):
        self.mouse_x, self.mouse_y = event.x, event.y
        print(str(self.mouse_x), ' ', str(self.mouse_y))

    def shoot(self, event):
        pass

    def direction(self): #calculation of second point of speed vector
        '''
        Here below a problem with 0 deg = 360 deg resolved, by comparing deltas
        phi and alpha in two points: alpha will/won't cross zero.
        '''
        if math.fabs(self.phi - self.alpha) < 180:
            if self.phi > self.alpha:
                self.alpha += self.DELTA_ALPHA
            elif self.phi < self.alpha:
                self.alpha -= self.DELTA_ALPHA
            else:
                pass
        elif math.fabs(self.phi - self.alpha) > 180:
            if (360 - self.phi) < self.phi:
                if self.alpha >= 0:
                    self.alpha -= self.DELTA_ALPHA
                else:
                    self.alpha = 360
            else:
                if self.alpha <= 360:
                    self.alpha += self.DELTA_ALPHA
                else:
                    self.alpha = 0
        elif ((math.fabs(self.phi - self.alpha) == 0) or (math.fabs(self.phi - self.alpha) == 360)):
            pass

        vect_x = self.movement_speed * math.cos(math.radians(self.alpha)) + self.position_x
        vect_y = self.movement_speed * math.sin(math.radians(self.alpha)) + self.position_y
        self.speed_vector = [vect_x, vect_y]
        self.position_x = self.speed_vector[0]
        self.position_y = self.speed_vector[1]
