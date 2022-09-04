from tkinter import *
from random import *
import time
import pygame

pygame.mixer.init()


class Ball:
    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)
        self.canvas.move(self.id, winW / 2, winH / 2)
        self.x = randint(-5, -1) and randint(1, 4)
        self.y = step
        self.notTouchBottom = True
        if self.notTouchBottom:
            pygame.mixer.music.load('../music/1.mp3')
            pygame.mixer.music.play(-1)

    def hit(self, ballPos):
        racketpos = self.canvas.coords(self.racket.id)
        if ballPos[2] >= racketpos[0] and ballPos[0] <= racketpos[2]:
            if racketpos[1] <= ballPos[3] <= racketpos[3]:
                return True
        return False

    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)
        ballPos = self.canvas.coords(self.id)
        if ballPos[1] <= 0:
            self.y = step
        if ballPos[3] >= winH:
            self.y = -step
        if ballPos[0] <= 0:
            self.x = step
        if ballPos[2] >= winW:
            self.x = -step
        if self.hit(ballPos):
            self.y = -step
        if ballPos[3] >= winH:
            self.notTouchBottom = False
            pygame.mixer.music.pause()


class Racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 15, fill=color)
        self.canvas.move(self.id, 270, 400)
        self.x = 0

    def racketmove(self):
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)
        self.canvas.move(self.id, self.x, 0)

    def moveLeft(self, event):
        self.x = -3
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0

    def moveRight(self, event):
        self.x = 3
        pos = self.canvas.coords(self.id)
        if pos[2] >= winW:
            self.x = 0


winW = 640
winH = 480
step = 3
speed = 0.02

tk = Tk()
tk.title('Bouncing')
tk.wm_attributes('-topmost', 1)
c = Canvas(tk, width=winW, height=winH)
c.pack()
c.update()

racket = Racket(c, 'red')
ball = Ball(c, 'yellow', winW, winH, racket)

while ball.notTouchBottom:
    ball.ballMove()
    racket.racketmove()
    c.update()
    time.sleep(speed)

