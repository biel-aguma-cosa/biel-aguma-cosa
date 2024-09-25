#['','','','','','','','','','','','','','','']
#['□','□','□','□','□','□','□','□','□','□','□','□','□','□']
#['■','■','■','■','■','■','■','■','■','■','■','■']
#['■','■','■','■','■','■','■','■','■','■','■','■']
b = ''
background = []
for item in ['□','□','□','□','□','□','□','□','□','□','□','□','□','□','□']:
    background.append(['■','□','□','□','□','□','□','□','□','□','□','□','□','□','■'])
background[0] = ['■','■','■','■','■','■','■','■','■','■','■','■','■','■','■']
background[14] = ['■','■','■','■','■','■','■','■','■','■','■','■','■','■','■']

def screen_refresh():
    global b
    for n in [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]:
        print('')
    for line in background[:]:
        print(line)
    b = input()

def processy(num):
    r = (num*-1) + 7
    return r
def processx(num):
    r = num + 7
    return r

y0 = processy(0)
x0 = processx(0)

class entity_:
    def __init__(self,inx,iny,img):
        self.inx = inx
        self.iny = iny
        self.x = processx(inx)
        self.y = processy(iny)
        self.img = img
    def move(self,y_,x_):
        if not (background[processy(y_)][processx(x_)] == '■'):
            self.y = (processy(y_))
            self.x = (processx(x_))
    def move_x(self,x_):
        if not (background[processy(y_)][processx(x_)] == '■'):
            self.x = (processx(x_))
    def move_y(self,y_):
        if not (background[processy(y_)][processx(x_)] == '■'):
            self.y = (processy(y_))

center = entity_(inx=5,iny=5,img='◌')
player = entity_(inx=2,iny=2,img='☻')
box = entity_(inx=-1,iny=-1,img='◙')

background[player.y][player.x] = player.img
background[box.y][box.x] = box.img
background[y0][x0] = center.img

if not b = 'exit':
    screen_refresh()
else:
    input()
