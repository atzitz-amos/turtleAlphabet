
from scipy.signal.lti_conversion import ss2tf
import math
import threading
import time
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