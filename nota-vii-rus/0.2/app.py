from tkinter import *
import time
import math

class vector():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'vector({self.x}, {self.y})'
    def __repr__(self):
        return f'vector({self.x}, {self.y})'
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    def normalize(self):
        m = self.magnitude()
        self.x = self.x/m
        self.y = self.y/m
    def normalized(self):
        return vector(self.x/self.magnitude(),self.y/self.magnitude())




class object():
    def __init__(self,_position=vector(),scale=[5,5]):
        self._position = _position
        self._scale = {
            'w' : scale[0],
            'h' : scale[1]
        }
    @property
    def scale(self):
        return self._scale
    @scale.setter
    def scale(self,value):
        if type(value) == list or type(value) == tuple:
            return {
            'w' : value[0],
            'h' : value[1]
            }
        elif type(value) == dict:
            try:
                return {
                    'w' : value['w'],
                    'h' : value['h']
                }
            except:
                raise ValueError("invalid dict['w'] and dict['h']")
        else:
            raise ValueError("object's scale must be a list, tuple or dict")
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self,value):
        if type(value) != vector:
            raise ValueError("object's position must be a vector")
        else:
            self._position = value
            return value
    
    def draw(self):
        try:
            canvas.delete(self.image)
        except:
            print('no image')
        x, y = self.position.x, self.position.y
        w, h = self.scale['w'], self.scale['h']
        self.image = canvas.create_rectangle(x-w/2,y-h/2,x+w/2,y+h/2,fill='white',outline='magenta')
    def move(self,direction=vector()):
        self.position += direction
        if (25 > self.position.x or self.position.x > 575) or (25 > self.position.y or self.position.y > 375):
            self.position += vector(direction.x*-1,direction.y*-1)
        print(self.position)
        self.draw()


a = object(vector(20,25),(25,25))
a.position.x += 5

root = Tk()
root.geometry('602x402')
root.resizable(False,False)

canvas = Canvas(root,width=600,height=400,bg='black')
canvas.place(x=-1,y=-1)

canvas.create_rectangle(12.5,12.5,575+12.5,375+12.5,fill='black',outline='red')

a.draw()

def on_key_pressed(event):
    match event.char:
        case 'a':
            a.move(vector(-25,  0))
        case 'd':
            a.move(vector( 25,  0))
        case 'w':
            a.move(vector(  0,-25))
        case 's':
            a.move(vector(  0, 25))

root.bind("<KeyPress>",on_key_pressed)

root.mainloop()