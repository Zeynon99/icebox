import pygame
from math import *
from  pygame import  mixer
pygame.init()

screen = pygame.display.set_mode((700, 700))
xx = 600
bbig = True
score = 0
yy = 600
zz = 0
bbbig = False
jcy = 600
jcx = 10
c = 0
cum = 0
kj = 0
s=0
dis =0
fg = 0
x = 1
ff = 0
bf = xx
gf = yy - 32
ll = 0
tt = 200
tty = 150
you = False
uoy = True
pygame.display.set_caption("cumcum69")
# image
pussyi = pygame.image.load("plum r.png")
pussyu = pygame.image.load("plum l.png")
cxid = pygame.image.load('drop.png')
#rest = pygame.image.load("img37.png")
ivon = pygame.image.load("penis.png")
big = pygame.image.load("penis-2.png")
#scren = pygame.image.load("img36.png")
hat = pygame.image.load("hat.png")
juice = pygame.image.load("gift-box-2.png")

pygame.display.set_icon(cxid)
fuck = True
i = 500
j = 900


def dk(a,b):
    screen.blit(juice,(a,b))


def bigs(a, b):
    screen.blit(big, (a, b))

def distance(x1,x2,y1,y2):
    s = sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)))
    return s
def bound(a):
    if a >= 670:
        a = 670
    elif a <= 0:
        a = 0
    return a

def bounds(a):
    if a >= 620:
        a = 620
    elif a <= 0:
        a = 0
    return a

def hats(a, b):
    screen.blit(hat, (a, b))

def times(n):
    i = 0
    while i < n:
        screen.blit(rest, (0, 25))
        i += 1

def pussydw(a, b):
    screen.blit(pussyu, (a, b))


#def rest1(a, b):
    #screen.blit(rest, (a, b))


def pussy(a, b):
    screen.blit(pussyi, (a, b))


#def scr(a, b):
    #screen.blit(scren, (a, b))


def enemy(v, b):
    screen.blit(cxid, (v, b))


def bullet(bool, aa, bb, ):
    while bool:

        enemy(aa, bb)
        bb -= 1
        if bb == -32:
            bool = False



def player(x, y):
    screen.blit(ivon, (x, y))


iii = 0
hj = False
# loop
while fuck:

    iii += 1

    screen.fill((154, 100, 104))
    pussydw(bound(tt) + 55, bound(tty))

    for cv in pygame.event.get():
        if cv.type == pygame.SYSTEM_CURSOR_ARROW:
            fuck = False
        if cv.type == pygame.QUIT:
            fuck = False

        if cv.type == pygame.KEYDOWN:
            if cv.key == pygame.K_DOWN:
                c = x
            if cv.key == pygame.K_UP:
                c = -x
            if cv.key == pygame.K_RIGHT:
                zz = x
            if cv.key == pygame.K_LEFT:
                zz = - x

            if cv.key == pygame.K_SPACE:
                jk = xx
                gf = yy
                ll += 1
                cum += 1
                hj = True
        if cv.type == pygame.KEYUP:
            if cv.key == pygame.K_DOWN or cv.key == pygame.K_UP or cv.key == pygame.K_RIGHT or cv.key == pygame.K_LEFT:
                zz = 0
                c = 0
    xx += zz
    yy += c
    dis = distance(tt, xx, tty, yy)
    if dis  < 150:
        tt += 0
    elif dis > 150:
     if tt < 590 and you:
        tt += 0.5
        uoy = False
     if tt == -10:
        you = True
        tty += 0
     if tt == 590:
        uoy = True
        tty += 0
     if tt > -10 and uoy:
        tt -= 0.5
        you = False


    if ll == 1:
        if bbbig:
            kj = jk + 48
        elif bbbig==False:
            kj = jk + 16
        fg = gf
        ll = 2


    if hj and ll >= 0:

        enemy(kj, fg)

        fg -= 1
        if fg == -32:
            hj = False
            ll = 0

    if bbig:
        dk(jcx, jcy)
        player(bound(xx), bound(yy))

    if sqrt(((jcx - bound(xx)) * (jcx - bound(xx))) + ((jcy - bound(yy)) * (jcy - bound(yy)))) < 20:
        bbig = False
        bbbig = True

    if bbbig:
        bigs(bound(xx), bound(yy))

    pussy(bound(tt), bound(tty))
    hats(tt + 42, tty - 22)

    if cum < 1:
        enemy(600, 25)

    if cum < 2:
        enemy(632, 25)
    if cum < 3:
        enemy(664, 25)
    if cum >= 3 and hj == False:
        bbig = True
        bbbig = False
        cum = 0

    if hj:
        sqx = sqrt(((tt + 18 - kj) * (tt - kj)) + ((tty - fg) * (tty - fg)))
        if sqx <= 80:
            hj = False
            ll = 0
            score += 1
    pygame.display.update()
print(iii)
 