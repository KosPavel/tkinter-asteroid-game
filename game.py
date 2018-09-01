import tkinter

class Game():

    def __init__(self, root):
        self.canvas = tkinter.Canvas(root, height = 800, width = 800, bg = 'white')
        self.tags = [] #painted objects on canvas

    def create_objects(*instances):
        '''
        here we are creating painted objects on canvas for the first time
        '''
        for i in instances:
            shape = i.shape()
            ship = self.canvas.create_polygon(shape, outline = i.outline,
                                      fill = i.fill)
            self.tags.append(ship)
            print(self.tags)
        self.canvas.pack()

    def update(self, *instances):
        '''
        getting shape coords from each instance, that should
        be painted on canvas, then updating picture
        '''
        current_tag = -1
        for i in instances:
            current_tag += 1
            shape = i.shape()
            self.canvas.coords(self.tags[current_tag], shape)
            self.canvas.after(30, self.update)
