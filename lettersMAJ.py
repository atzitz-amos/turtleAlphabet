
import math
import turtle as t

tu = t.Turtle(visible=True)
tu.shape('turtle')
tu.speed(0)
"""
x,y

d
    x2,y2

x2,y2
"""


def talloval(r):
    tu.left(45)
    for _ in range(2):
        tu.circle(r,90)
        tu.circle(r / 2,90)


def flatoval(r):  # Horizontal Oval
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


def B(x,y,d):
    dx = d / 2
    frac1 = 3 / 8
    frac2 = 5 / 8
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.seth(0)
    tu.fd(d / 2 * frac1)
    tu.circle(d * frac2 / 2,180)
    tu.fd(d / 2 * frac1)
    tu.seth(0)
    tu.fd(d / 2 * frac2)
    tu.circle(d * frac1 / 2,180)
    tu.fd(d / 2 * frac2)


def C(x,y,d):
    move(x,y)
    tu.seth(180)
    tu.circle(d / 2,180)


def D(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.seth(0)
    tu.circle(d / 2,180)


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


def E(x,y,d):
    F(x,y,d)
    tu.seth(0)
    tu.fd(d * frac1)


def G(x,y,d):
    move(x,y)
    tu.seth(180)
    tu.circle(d / 2,200)
    tu.seth(90)
    tu.fd(d / 2)
    tu.seth(180)
    tu.fd(d / 4)

def H(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.bk(d / 2)
    tu.seth(0)
    tu.fd(d / 3 * 2)
    tu.seth(90)
    tu.fd(d / 2)
    tu.bk(d)


barfrac = 5 / 12
def I(x,y,d):
    move(x,y)
    tu.fd(d * barfrac / 2)
    tu.bk(d * barfrac)
    tu.fd(d * barfrac / 2)
    tu.seth(270)
    tu.fd(d)
    tu.seth(0)
    tu.bk(d * barfrac / 2)
    tu.fd(d * barfrac)


def J(x,y,d):
    move(x,y)
    tu.bk(d * barfrac / 2)
    tu.fd(d * barfrac)
    tu.bk(d * barfrac / 2)
    move(x,y)
    tu.seth(270)
    tu.fd(d / 6 * 5)
    tu.circle(-d / 6,180)


def K(x,y,d):
    ang = 45
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    tu.back(d / 2)
    tu.goto(x + d / 2,y)
    move(x,y - d / 2)
    tu.goto(x + d / 2,y - d)

def L(x,y,d):
    frac = 1 / 2
    move(x,y)

    tu.seth(270)
    tu.fd(d)
    tu.seth(0)
    tu.fd(frac * d)


def M(x,y,d):
    ang = -45
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


def N(x,y,d):
    ang = 7 / 12
    move(x,y)
    tu.seth(270)
    tu.fd(d)
    move(x,y)
    tu.goto(x + d * ang,y - d)
    tu.seth(90)
    tu.fd(d)

def O(x,y,d):
    move(x,y)
    tu.seth(180)
    talloval(d / 3 * 2)


def P(x,y,d):
    move(x,y)
    D(x,y,d / 2)
    tu.seth(270)
    tu.fd(d)


def Q(x,y,d):
    ang = 45
    move(x,y)
    tu.circle(-d / 2)
    move(x + d / 10,y - d / 2 - d / 10)
    tu.right(ang)
    tu.fd(d / 3 * 2)


def R(x,y,d):
    P(x,y,d)
    move(x,y - d / 2)
    tu.goto(x + d / 3,y - d)


def S(x,y,d):
    fracx = 1 / 2
    fracy = 1 / 4
    sx = x + d * fracx
    sy = y - d * fracy
    move(sx,sy)
    tu.seth(90)
    tu.circle(d / 4,270)
    tu.circle(-d / 4,270)


def T(x,y,d):
    frac = 1 / 4
    move(x,y)
    tu.fd(d * frac * 2)
    tu.bk(d * frac)
    tu.seth(270)
    tu.fd(d)


def U(x,y,d):
    move(x,y)
    tu.seth(270)
    tu.fd(d / 4 * 3)
    tu.circle(d / 4,180)
    tu.fd(d / 4 * 3)


def V(x,y,d):
    move(x,y)
    tu.goto(x + d / 4,y - d)
    tu.goto(x + d / 2,y)

def W(x,y,d):
    frac = 1 / 2
    move(x,y)
    tu.goto(x + d / 8,y - d)
    tu.goto(x + d / 4,y - d * frac)
    tu.goto(x + d / 8 * 3,y - d)
    tu.goto(x + d / 2,y)


def X(x,y,d):
    move(x,y)
    tu.goto(x + d / 2,y - d)
    move(x + d / 2,y)
    tu.goto(x,y - d)


def Y(x,y,d):
    move(x,y)
    tu.goto(x + d / 4,y - d / 3)
    tu.goto(x + d / 2,y)
    move(x + d / 4,y - d / 3)
    tu.seth(270)
    tu.fd(d / 3 * 2)


def Z(x,y,d):
    move(x,y)
    tu.fd(d / 2)
    tu.goto(x,y - d)
    tu.seth(0)
    tu.fd(d / 2)


# var = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
var = [B,O,N,N,E,N,U,I,T]

start = -550
step = 100
for v in var:
    v(start,10,100)
    start += step
tu.ht()
tu.screen.mainloop()
