import tkinter

from player import Player
from game import Game

root = tkinter.Tk()
player = Player(root)
game = Game(root)

'''
arguments below - instances should be drawn on canvas, must have
shape() and direction() methods
'''
game.create_objects(player,
                   )

game.update()

root.mainloop()
