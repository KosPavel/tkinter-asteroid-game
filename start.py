import tkinter

from player import Player
from game import Game

root = tkinter.Tk()
player = Player(root)
game = Game(root)
game.create_objects(player)
game.update()

root.mainloop()
