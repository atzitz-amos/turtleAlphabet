
import math
import time
import turtle as t

tu = t.Turtle(visible=True)
tu.shape('turtle')
tu.speed(4)
"""
x,y

d
    x2,y2

x2,y2
"""


def talloval(r):    # Vertical Oval
    tu.left(45)
    for _ in range(2):
        tu.circle(r,90)
        tu.circle(r / 5,90)


def flatoval(r):     # Horizontal Oval
    tu.right(45)
    for _ in range(2):
        tu.circle(r,90)
        tu.circle(r / 2,90)


def move(x,y):
    tu.pu()
    tu.goto(x,y)
    tu.pd()
    tu.seth(0)


def _pythagore(a,b):
    return math.sqrt(a ** 2 + b ** 2)

def A(x,y,d):
    move(x + d / 4,y)
    tu.goto(x,y - d)
    move(x + d / 4,y)
    tu.goto(x + d / 2,y - d)
    move(x + d / 8,y - d / 2)
    tu.fd(d / 4)

def a(x,y,d):
    move(x, y - d / 4 * 3)
    tu.seth(270)
    tu.circle(d/4)
    move(x + d / 2, y - d / 2)
    tu.seth(270)
    tu.fd(d / 2)

def B(x,y,d):
    frac1 = 4 / 8
    frac2 = 4 / 8
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.seth(0)
    tu.fd(d / 2 * frac1)
    tu.circle(d * frac2 / 2,180)
    tu.fd(d / 2 * frac1)
    tu.seth(0)
    tu.fd(d / 2 * frac1)
    tu.circle(d * frac1 / 2,180)
    tu.fd(d / 2 * frac1)

def b(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.bk(d / 4)
    tu.circle(d / 4)

def C(x,y,d):
    move(x + d / 2,y)
    tu.seth(180)
    tu.circle(d / 2,180)

def c(x,y,d):
    move(x + d / 2, y - d / 4 * 3)
    tu.seth(90)
    tu.pu()
    tu.circle(d / 4, 40)
    tu.pd()
    tu.circle(d / 4, 280)


def D(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.seth(0)
    tu.circle(d / 2,180)

def d(x,y,d):
    move(x + d / 2,y)
    tu.seth(270)
    tu.fd(d)
    tu.bk(d / 4)
    tu.circle(-d / 4)


frac1 = 1 / 2
frac2 = 1 / 3


def F(x,y,d):
    move(x,y)
    tu.seth(0)
    tu.fd(d * frac1)
    move(x,y)
    tu.seth(270)
    tu.fd(d / 2)
    tu.seth(0)
    tu.fd(frac2 * d)
    move(x,y - d / 2)
    tu.seth(270)
    tu.fd(d / 2)

def f(x,y,d):
    move(x, y - d)
    tu.seth(90)
    tu.fd(d / 4 * 3)
    tu.circle(-d / 4, 180)
    move(x, y - d / 2)
    tu.fd(d / 4)


def E(x,y,d):
    F(x,y,d)
    tu.seth(0)
    tu.fd(d * frac1)

def e(x,y,d):
    move(x, y - d / 4 * 3)
    tu.fd(d / 2)
    tu.seth(90)
    tu.circle(d / 4, 270)
    tu.fd(d / 4)


def e_accentaigu(x,y,d):
    e(x,y,d)
    move(x + d / 8,y - d / 6)
    tu.goto(x + d / 2,y)


def G(x,y,d):
    move(x + d / 2,y)
    tu.seth(180)
    tu.circle(d / 2,180)
    tu.seth(90)
    tu.fd(d / 2)
    tu.seth(180)
    tu.fd(d / 4)

def g(x,y,d):
    move(x, y - d / 4 * 3)
    tu.seth(270)
    tu.circle(d / 4)
    move(x + d / 2, y - d / 2)
    tu.seth(270)
    tu.fd(d / 3 * 2)
    tu.circle(-d / 4, 180)

def H(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.bk(d / 2)
    tu.seth(0)
    tu.fd(d / 2)
    tu.seth(90)
    tu.fd(d / 2)
    tu.bk(d)

def h(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.bk(d / 4)
    tu.seth(90)
    tu.circle(-d / 4, 180)
    tu.fd(d / 4)


barfrac = 5 / 12
def I(x,y,d):
    move(x,y)
    tu.fd(d / 2)
    tu.bk(d / 4)
    tu.seth(270)
    tu.fd(d)
    tu.seth(0)
    tu.fd(d / 4)
    tu.bk(d / 2)
    tu.bk(d / 4)
    tu.fd(d / 2)

def i(x,y,d):
    move(x + d / 4, y - d)
    tu.seth(90)
    tu.fd(d / 2)
    move(x + d / 4, y - d / 4)
    tu.dot(3)



def J(x,y,d):
    move(x,y)
    tu.fd(d / 2)
    tu.seth(270)
    tu.fd(d / 4 * 3)
    tu.circle(-d / 4,180)

def j(x,y,d):
    i(x,y,d)
    move(x + d / 4, y - d)
    tu.seth(270)
    tu.circle(-d / 8, 180)

def K(x,y,d):
    ang = 45
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.back(d / 2)
    tu.goto(x + d / 2,y)
    move(x,y - d / 2)
    tu.goto(x + d / 2,y - d)

def k(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.back(d / 2)
    tu.goto(x + d / 3, y - d / 4)
    move(x,y - d / 2)
    tu.goto(x + d / 2,y - d)

def L(x,y,d):
    frac = 1 / 2
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.seth(0)
    tu.fd(frac * d)

def l(x,y,d):
    move(x + d / 4,y)
    tu.seth(270)
    tu.fd(d / 4 * 3)
    tu.circle(d / 4, 90)


def M(x,y,d):
    ang = -45
    ang = ang + ang / 2
    seg = 2 / 3
    midang = ang * 2

    move(x,y)
    tu.seth(270)
    tu.fd(d)
    move(x,y)
    tu.seth(ang)
    tu.fd(d * seg)
    tu.right(midang)
    tu.fd(d * seg)

    tu.seth(270)
    tu.fd(d)

def m(x,y,d):
    move(x, y - d / 2)
    tu.seth(270)
    tu.fd(d / 2)
    tu.seth(90)
    tu.fd(d / 8 * 3)
    tu.circle(-d / 8, 180)
    tu.fd(d / 8 * 3)
    tu.seth(90)
    tu.fd(d / 8 * 3)
    tu.circle(-d / 8, 180)
    tu.fd(d / 8 * 3)



def N(x,y,d):
    move(x, y-d)
    tu.seth(90)
    tu.fd(d)
    tu.goto(x + d / 2, y - d)
    tu.fd(d)

def n(x,y,d):
    move(x, y - d / 2)
    tu.seth(270)
    tu.fd(d / 2)
    tu.seth(90)
    tu.fd(d / 4 * 1)
    tu.circle(-d / 4, 180)
    tu.fd(d / 4 * 1)


"""def O(x,y,d):
    move(x + d / 5,y)
    tu.seth(180)
    talloval(d / 3 * 2)
"""
def O(x,y,d):
    move(x, y - d / 4)
    tu.seth(270)
    tu.fd(d / 2)
    tu.circle(d / 4, 180)
    tu.fd(d / 2)
    tu.circle(d / 4, 180)

def o(x,y,d):
    move(x, y - d / 4 * 3)
    tu.seth(270)
    tu.circle(d / 4)


def P(x,y,d):
    move(x,y)
    tu.fd(d / 4)
    tu.circle(-d / 4, 180)
    tu.fd(d / 4)
    move(x, y)
    tu.seth(270)
    tu.fd(d)

def p(x,y,d):
    move(x, y - d / 2)
    tu.seth(270)
    tu.fd(d / 4 * 3)
    tu.bk(d / 2)
    tu.circle(d / 4)


def Q(x,y,d):
    move(x,y)
    O(x, y, d)
    move(x + d / 4, y - d / 3 * 2)
    tu.goto(x + d / 2, y - d)

def q(x,y,d):
    move(x + d / 2, y - d / 2)
    tu.seth(270)
    tu.fd(d / 4 * 3)
    tu.bk(d / 2)
    tu.circle(-d / 4)


def R(x,y,d):
    P(x,y,d)
    move(x,y - d / 2)
    tu.goto(x + d / 2,y - d)


def r(x,y,d):
    move(x, y - d / 2)
    tu.seth(270)
    tu.fd(d / 2)
    tu.seth(90)
    tu.fd(d / 4 * 1)
    tu.circle(-d / 4, 180)


def S(x,y,d):
    fracx = 1 / 2
    fracy = 1 / 4
    sx = x + d * fracx
    sy = y - d * fracy
    move(sx,sy)
    tu.seth(90)
    tu.circle(d / 4,270)
    tu.circle(-d / 4,270)

def s(x,y,d):
    S(x + d / 6,y - d / 2,d / 2)


def T(x,y,d):
    frac = 1 / 4
    move(x,y)
    tu.fd(d * frac * 2)
    tu.bk(d * frac)
    tu.seth(270)
    tu.fd(d)

def t(x,y,d):
    frac = 1 / 4
    move(x,y - d / 4)
    tu.fd(d * frac * 2)
    tu.bk(d * frac)
    move(x + d / 16 * 3, y)
    tu.seth(270)
    tu.fd(d / 4 * 3)
    tu.circle(d/4, 90)


def U(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d / 4 * 3)
    tu.circle(d / 4,180)
    tu.fd(d / 4 * 3)
    
def u(x,y,d):
    move(x,y - d / 2)
    tu.seth(270)
    tu.fd(d / 4)
    tu.circle(d/4, 180)
    tu.fd(d / 4)
    tu.bk(d / 2)


def V(x,y,d):
    move(x,y)
    tu.goto(x + d / 4,y - d)
    tu.goto(x + d / 2,y)

def v(x,y,d):
    move(x,y - d / 2)
    tu.goto(x + d / 4,y - d)
    tu.goto(x + d / 2,y - d / 2)


def W(x,y,d):
    frac = 1 / 2
    move(x,y)
    tu.goto(x + d / 8,y - d)
    tu.goto(x + d / 4,y - d * frac)
    tu.goto(x + d / 8 * 3,y - d)
    tu.goto(x + d / 2,y)

def w(x,y,d):
    frac = 1 / 2
    move(x,y - d / 2)
    tu.goto(x + d / 8,y - d)
    tu.goto(x + d / 4,y - d * frac)
    tu.goto(x + d / 8 * 3,y - d)
    tu.goto(x + d / 2,y - d / 2)


def X(x,y,d):
    move(x,y)
    tu.goto(x + d / 2,y - d)
    move(x + d / 2,y)
    tu.goto(x,y - d)

def x(x,y,d):
    move(x,y - d / 2)
    tu.goto(x + d / 2,y - d)
    move(x + d / 2,y - d / 2)
    tu.goto(x,y - d)


def Y(x,y,d):
    move(x,y)
    tu.goto(x + d / 4,y - d / 3)
    tu.goto(x + d / 2,y)
    move(x + d / 4,y - d / 3)
    tu.seth(270)
    tu.fd(d / 3 * 2)

def y(x,y,d):
    move(x, y - d / 2)
    tu.goto(x + d / 4, y - d)
    tu.goto(x + d / 2, y - d / 2)
    tu.goto(x + d / 8, y - d / 4 * 5)


def Z(x,y,d):
    move(x,y)
    tu.fd(d / 2)
    tu.goto(x,y - d)
    tu.seth(0)
    tu.fd(d / 2)

def z(x,y,d):
    move(x,y - d / 2)
    tu.fd(d / 2)
    tu.goto(x,y - d)
    tu.seth(0)
    tu.fd(d / 2)

def unknown(x, y, d):
    move(x, y)
    tu.fd(d / 2)
    tu.seth(270)
    tu.fd(d)
    tu.seth(180)
    tu.fd(d / 2)
    tu.seth(90)
    tu.fd(d)



pointfrac = 3 / 16
def _dot(x,y,d,frac = pointfrac,size=6):
    tu.goto(x,y - (d - d * frac))
    move(x,y - d + size / 2)
    tu.dot(size)

    
def exclamation_point(x,y,d,size=3):
    move(x,y)
    _dot(x,y,d,size=size)


def question_mark(x,y,d,size=3):
    move(x,y)
    tu.circle(-d / 4,180)
    _dot(x,y,d,size=size)


def point(x,y,d,size=4):
    move(x,y - (d - size / 2))
    tu.dot(size)

def comma(x,y,d, size=4):
    move(x,y - (d - size / 2))
    point(x,y,d,size)
    tu.seth(270)
    tu.circle(-d / 4, 70)

def apostrophe(x,y,d,size=4):
    move(x,y)
    tu.dot(size)
    tu.seth(270)
    tu.circle(-d / 4, 70)



def onOnePlace(letters,x,y,d,espacement=10):
    for l in letters:
        tu.clear()
        l(x,y,d)
        time.sleep(espacement / 100)


class DefilThread:

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
    for letter in text:
        if letter in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
            exec(f"{letter}({posX}, {posY}, {size})")
            posX += step
        elif letter in "!.,?'éèàêâ":
            _char_to_func = {'!':exclamation_point,'.':point,',':comma,'?':question_mark,"'":apostrophe,'é':e_accentaigu}
            _char_to_func[letter](posX,posY,size)
            posX += step / 2
        elif letter == " ":
            posX += step / 4
        elif letter == "\n":
            posY -= size + size / 3 * 4
            posX = start[0] - step
        posX += step


var = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

#var = [B,O,N,N,E,N,U,I,T]

"""start = -550
step = 55
for v in var:
    v(start,10,50)
    start += step

var[0](0, 0, 100)
G(0,0,100)
L(0, 0, 100)

"""

tu.speed(3)
textToWrite = """é"""
write(textToWrite,30,(-350,0))
tu.ht()
tu.screen.mainloop()
