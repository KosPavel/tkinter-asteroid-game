import tkinter

from player import Player
from game import Game

root = tkinter.Tk()
player = Player(root)
game = Game(root)
game.create_objects(player)
# game.canvas.after(30, game.update(player))
root.mainloop()



# ship = game.canvas.create_polygon(player.shape,
#                              outline = player.outline,
#                              fill = player.fill)
# game.canvas.pack()
# game.canvas.after(30, game.update(player, ship))
# root.mainloop()
