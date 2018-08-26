import random
import tkinter
import math

class Player():

    def __init__(self, root):
        self.position_x = 400
        self.position_y = 400
        self.phi = 270               #angle in degrees for ship rotation
        self.DELTA_PHI = 5
        self.SIZE_CONST = 15         #const for ship size regulation
        self.alpha = 270             #angle for speed vector calculation
        self.DELTA_ALPHA = 5
        self.movement_speed = 0      #current speed value, pixels/tick
        self.DELTA_MOVEMENT_SPEED = 1
        self.MOVEMENT_SPEED_MAX = 4  #maximum speed value
        self.MOVEMENT_SPEED_MIN = -3 #minimum speed value

        '''
        speed vector can provide 'open space' movement, when
        you can rotate your ship without changing direction.
        Arguments are coordinates of second point of vector.
        '''
        self.speed_vector = [self.position_x, self.position_y]

        root.bind('<w>',self.moveForward)
        root.bind('<s>',self.moveBackward)
        root.bind('<a>',self.rotateLeft)
        root.bind('<d>',self.rotateRight)

        '''
        Below we are creating ship by drawing triangle. Each point calculated
        using angle phi for future simple realization of rotation.
        '''
        self.shape = [
        self.position_x + self.SIZE_CONST * math.cos(math.radians(self.phi)),
        self.position_y + self.SIZE_CONST * math.sin(math.radians(self.phi)),
        self.position_x + self.SIZE_CONST * math.cos(math.radians(self.phi)-60),
        self.position_y + self.SIZE_CONST * math.sin(math.radians(self.phi)-60),
        self.position_x + self.SIZE_CONST * math.cos(math.radians(self.phi)+60),
        self.position_y + self.SIZE_CONST * math.sin(math.radians(self.phi)+60),
                     ]

        self.ship = canvas.create_polygon(self.shape, outline = 'red', fill = 'green')

    def moveForward(self, event):
        if self.movement_speed < self.MOVEMENT_SPEED_MAX:
            self.movement_speed += self.DELTA_MOVEMENT_SPEED
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
        self.direction()
        self.position_x = self.speed_vector[0]
        self.position_y = self.speed_vector[1]
        print('Alpha = ' + str(self.alpha))
        print('Movement_speed = ' + str(self.movement_speed))
        print('position_x = ' + str(self.position_x))
        print('position_y = ' + str(self.position_y))

    def moveBackward(self, event):
        if self.movement_speed > self.MOVEMENT_SPEED_MIN:
            self.movement_speed -= self.DELTA_MOVEMENT_SPEED
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
        self.direction()
        self.position_x = self.speed_vector[0]
        self.position_y = self.speed_vector[1]
        print('Alpha = ' + str(self.alpha))
        print('Movement_speed = ' + str(self.movement_speed))
        print('position_x = ' + str(self.position_x))
        print('position_y = ' + str(self.position_y))

    def rotateLeft(self, event): #MUST CORRECT THIS
        self.phi -= self.DELTA_PHI
        if self.phi < 0:
            self.phi = 360
        print('Phi = ' + str(self.phi))

    def rotateRight(self, event):
        self.phi += self.DELTA_PHI
        if self.phi > 360:
            self.phi = 0
        print('Phi = ' + str(self.phi))

    def direction(self): #calculation of second point of speed vector
        vect_x = self.movement_speed * math.cos(math.radians(self.alpha)) + self.position_x
        vect_y = self.movement_speed * math.sin(math.radians(self.alpha)) + self.position_y
        self.speed_vector = [vect_x, vect_y]
        print('speed_vector = ' + str(self.speed_vector))

    def shape_coords_update(self): #new coords for ship, using in .after
        updated_shape = [
        player.position_x + player.SIZE_CONST * math.cos(math.radians(player.phi)),
        player.position_y + player.SIZE_CONST * math.sin(math.radians(player.phi)),
        player.position_x + player.SIZE_CONST * math.cos(math.radians(player.phi)-60),
        player.position_y + player.SIZE_CONST * math.sin(math.radians(player.phi)-60),
        player.position_x + player.SIZE_CONST * math.cos(math.radians(player.phi)+60),
        player.position_y + player.SIZE_CONST * math.sin(math.radians(player.phi)+60),
                        ]
        for coord in updated_shape:
            coord = math.ceil(coord)

        return updated_shape

class Game():

    def __init__(self):
        pass

    def update(self):
        # canvas.coords(player.ship, player.position_x, player.position_y)
        # canvas.coords(player.ship, player.shape)
        new_shape_coords = player.shape_coords_update()
        canvas.coords(player.ship, new_shape_coords)
        canvas.after(30, self.update)

root = tkinter.Tk()
canvas = tkinter.Canvas(root, height = 800, width = 800, bg = 'white')
canvas.pack()
game = Game()
player = Player(root)
canvas.after(30, game.update)
root.mainloop()
