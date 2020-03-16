import lettersFuncs as let

tu = let.tu

def onOnePlace(letters,x,y,d,espacement=10):
    for l in letters:
        tu.clear()
        l(x,y,d)
        time.sleep(espacement / 100)


class DefilThread():

    def __init__(self,letters,size,x,y,diameter,interval,delay):
        super().__init__()

        self.delay = delay
        self.letters = letters
        self.size = size
        self.x = x
        self.y = y
        self.diameter = diameter
        self.interval = interval
    
    def run(self):
        sx,sy = self.x,self.y
        for i,l in enumerate(self.letters):
            tu.clear()
            letters = self.letters[:i]
            x,y = sx,sy
            l(sx,sy,self.diameter)
            for letter in reversed(letters):
                x -= self.interval
                if x >= self.size:
                    break
                letter(x,y,self.diameter)
                time.sleep(self.delay / 100)
        sx -= self.interval
        while True:
            tu.clear()
            for l in self.letters:
                l(sx,sy,self.diameter)
                sx -= self.interval
            print(sx,self.size)
            if abs(sx) >= self.size:
                tu.clear()
                break


def defil(letters,screensize,start=None,diameter=100,interval=None,delay=10):
    if not interval:
        interval = diameter / 2 + 10
    if not start:
        start = (screensize - screensize / 4,0)
    DefilThread(letters,screensize,*start,diameter,interval,delay).run()


def write(text, size, start=(0,0)):
    step = size / 2
    posX = start[0]
    posY = start[1]
    for letter in text.upper():
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            exec(f"let.{letter}({posX}, {posY}, {size})")
            posX += step
        elif letter == " ":
            posX += step / 4
        elif letter == "\n":
            posY -= size + size / 4
            posX = start[0] - step
        posX += step


#var = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

#var = [B,O,N,N,E,N,U,I,T]

"""start = -550
step = 55
for v in var:
    v(start,10,50)
    start += step

var[0](0, 0, 100)
G(0,0,100)
L(0, 0, 100)"""

tu.speed(7)

textToWrite = """iiiiiiiiiiiiiiiiiiiiiillllllllllllllllllllll"""
write(textToWrite, 30, (-350, 0))
#defil([A,S,S,S,X],400,interval=60)
tu.ht()
tu.screen.mainloop()