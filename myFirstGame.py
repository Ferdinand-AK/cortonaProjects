from functools import partial
import os
from pydoc import render_doc
import sys
import keyboard
from tkinter import mainloop
import msvcrt as m


def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

screen = [
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]

person1 = { 
  "symbol": "x",
  "pos": [0, 0]
}

person2 = { 
  "symbol": "o",
  "pos": [9, 9]
}

while True:
  for y, row in enumerate(screen):
    for x, col in enumerate(row):
      if person1["pos"][0] == x and person1["pos"][1] == y:
        sys.stdout.write(person1["symbol"])
      elif person2["pos"][0] == x and person2["pos"][1] == y:
        sys.stdout.write(person2["symbol"])
      else:
        sys.stdout.write(col)
    sys.stdout.write("\n")
  sys.stdout.flush()
  render_doc(screen)

  m.getch()
  if keyboard.is_pressed("Left") and person1["pos"][0] > 0:
    person1["pos"][0] -= 1
  elif keyboard.is_pressed("Right") and person1["pos"][0] < 9:
    person1["pos"][0] += 1
  elif keyboard.is_pressed("Up") and person1["pos"][1] > 0:    
    person1["pos"][1] -= 1
  elif keyboard.is_pressed("Down") and person1["pos"][1] < 9:
    person1["pos"][1] += 1
  elif keyboard.is_pressed("Escape"):
    break

  # 1. bekomme die Information der arrow buttons: rechts, links, ....
  # richtug = ...

  # 2. übersetze diese Information in die Position der ersten Person
  # wenn links: person1["pos"][0] = person1["pos"][0] - 1
  # wenn rechts: person1["pos"][0] = person1["pos"][0] + 1
  # wenn oben: person1["pos"][0] = person1["pos"][1] + 1
  # ...
  # (beachte min 0 und max 9)
