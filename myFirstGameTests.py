from functools import partial
from glob import escape
from turtle import *

def play(screen):
    screen.onkey(partial(left, 45), 'Left')
    screen.onkey(partial(right, 45), 'Right')
    screen.onkey(partial(forward, 50), 'Up')
    screen.onkey(partial(back, 50), "Down")
    screen.listen()
    mainloop()

if __name__ == '__main__':
    play(getscreen())