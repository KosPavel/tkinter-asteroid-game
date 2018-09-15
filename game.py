import tkinter
import random

import settings

class Game():

    def __init__(self, root):
        self.height = settings.height
        self.width = settings.width
        self.canvas = tkinter.Canvas(root,
                                    height = self.height,
                                    width = self.width,
                                    bg = settings.background,
                                    )
        self.inst_player = [] #for instance methods
        self.ship_ID = [] #ship ID (for coords updating)

        self.inst_asteroids = [] #for instance methods
        self.asteroids_ID = [] #asteroids ID (for coords updating)

    def create_player(self, player):
        shape = player.shape()
        player_ship = self.canvas.create_polygon(shape,
                                                outline = player.outline,
                                                fill = player.fill)
        self.ship_ID.append(player_ship)
        self.inst_player.append(player)
        self.canvas.pack()

    def create_asteroids(self, asteroids):
        i = 0
        while i < settings.max_asteroids:
            shape = asteroids.shape(i)
            asteroid = self.canvas.create_oval(
                                              shape,
                                              fill = random.choice(settings.colors),
                                              outline = random.choice(settings.colors))
            self.asteroids_ID.append(asteroid)
            i += 1
        self.inst_asteroids.append(asteroids)
        self.canvas.pack()

    def update(self):
        '''
        getting shape coords from each instance, that should
        be painted on canvas
        '''
        new_player_coords = [] #list with LISTS of coordinates of player
        for i in self.inst_player:
            new_player_coords.append(i.shape())
            i.direction()

        new_asteroids_coords = [] #list with LISTS of coordinates of asteroids
        for i in self.inst_asteroids:
            k = 0
            i.direction()
            while k < settings.max_asteroids:
                new_asteroids_coords.append(i.shape(k))
                k += 1
        '''
        updating picture
        '''

        z = 0
        while z < len(new_player_coords):
            self.canvas.coords(self.ship_ID[z], new_player_coords[z])
            z += 1

        z = 0
        while z < len(new_asteroids_coords):
            self.canvas.coords(self.asteroids_ID[z], new_asteroids_coords[z])
            z += 1

        self.canvas.after(10, self.update)
