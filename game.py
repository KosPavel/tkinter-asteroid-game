import tkinter

class Game():

    def __init__(self, root):
        self.canvas = tkinter.Canvas(root, height = 800, width = 800, bg = 'white')
        self.objectsIDs = [] #painted objects on canvas
        self.instances = [] #all instances

    def create_objects(self, *instances):
        '''
        here we are creating painted objects on canvas for the first time
        '''
        for i in instances:
            shape = i.shape()
            ship = self.canvas.create_polygon(shape,
                                             outline = i.outline,
                                             fill = i.fill)
            self.objectsIDs.append(ship) #list of drew objects
            self.instances.append(i) #list of instances for using their methods
            print(self.objectsIDs)
            print(self.instances)
        self.canvas.pack()

    def update(self):
        '''
        getting shape coords from each instance, that should
        be painted on canvas
        '''
        new_shape = [] #list with LISTS of coordinates for each instance
        for instance in self.instances:
            new_shape.append(instance.shape())
        '''
        updating picture
        '''
        for current_ID in self.objectsIDs:
            self.canvas.coords(self.objectsIDs[current_ID - 1],
                              new_shape[current_ID - 1],
                              )
        self.canvas.after(10, self.update)
