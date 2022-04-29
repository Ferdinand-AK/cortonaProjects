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
  [" ", " ", " "], 
  [" ", " ", " "], 
  [" ", " ", " "],
]

person1 = { 
  "symbol": "x"
}

person2 = { 
  "symbol": "o"
}
turn = person1
validTurn = True

def check_board_contiditions():
  return True

while True:
  for y, row in enumerate(screen):
    for x, col in enumerate(row):
      sys.stdout.write(col)
    sys.stdout.write("\n")
  sys.stdout.flush()
  render_doc(screen)

  m.getch()
  validTurn = True
  if keyboard.is_pressed("7") and screen[0][0] == " ":
    screen[0][0] = turn["symbol"]
  if keyboard.is_pressed("8") and screen[0][1] == " ":
    screen[0][1] = turn["symbol"]
  if keyboard.is_pressed("9") and screen[0][2] == " ":
    screen[0][2] = turn["symbol"]
  if keyboard.is_pressed("4") and screen[1][0] == " ":
    screen[1][0] = turn["symbol"]
  if keyboard.is_pressed("5") and screen[1][1] == " ":
    screen[1][1] = turn["symbol"]
  if keyboard.is_pressed("6") and screen[1][2] == " ":
    screen[1][2] = turn["symbol"]
  if keyboard.is_pressed("1") and screen[2][0] == " ":
    screen[2][0] = turn["symbol"]
  if keyboard.is_pressed("2") and screen[2][1] == " ":
    screen[2][1] = turn["symbol"]
  if keyboard.is_pressed("3") and screen[2][2] == " ":
    screen[2][2] = turn["symbol"]
  elif keyboard.is_pressed("Escape"):
    break
  else:
    validTurn = False

  print("                ")
  print(validTurn)
  print(keyboard.is_pressed("1") and screen[2][0] == " ")
  print(keyboard.is_pressed("1"))
  print(screen[2][0] == " ")
  print("                ")
  
  if validTurn:
    if turn == person1:
      turn = person2
    else:
      turn = person1

  # check_board_contiditions()

  # 1. bekomme die Information der arrow buttons: rechts, links, ....
  # richtug = ...

  # 2. übersetze diese Information in die Position der ersten Person
  # wenn links: person1["pos"][0] = person1["pos"][0] - 1
  # wenn rechts: person1["pos"][0] = person1["pos"][0] + 1
  # wenn oben: person1["pos"][0] = person1["pos"][1] + 1
  # ...
  # (beachte min 0 und max 9)
