import pydirectinput
from time import sleep
from screencaputil import getBackpackPage

def moveUp(seconds):
    pydirectinput.keyDown('w')
    sleep(seconds)
    pydirectinput.keyUp('w')    

def moveDown(seconds):
    pydirectinput.keyDown('s')
    sleep(seconds)
    pydirectinput.keyUp('s')    

def moveRight(seconds):
    pydirectinput.keyDown('d')
    sleep(seconds)
    pydirectinput.keyUp('d')

def moveLeft(seconds):
    pydirectinput.keyDown('a')
    sleep(seconds)
    pydirectinput.keyUp('a')  

def openBackpack():
    pydirectinput.PAUSE = 0.25
    pydirectinput.moveTo(971, 971)
    pydirectinput.click(x=970, y=970)

def switchPets(x, y):
    openBackpack()
    pydirectinput.moveTo(771, 681)
    pydirectinput.click(x=770, y=680)
    pydirectinput.moveTo(x+1, y+1)
    pydirectinput.click(x=x, y=y)
    pydirectinput.moveTo(x+100, y+100)
    pydirectinput.click(x=x+100, y=y+100)
    pydirectinput.moveTo(971, 971)
    pydirectinput.click(x=970, y=970)
    pydirectinput.PAUSE = 0.15

def teleport(page, x, y):
    openBackpack()
    currentPage, error = getBackpackPage()
    if page != currentPage:
        pydirectinput.moveTo(828, 861)
        pydirectinput.click(x=827, y=860)
    pydirectinput.moveTo(x+1, y+1)
    pydirectinput.doubleClick(x=x, y=y)
    pydirectinput.moveTo(901, 681)
    pydirectinput.doubleClick(x=900, y=680)
    pydirectinput.moveTo(1051, 638)
    pydirectinput.doubleClick(x=1050, y=637)
    sleep(8)
    pydirectinput.PAUSE = 0.15
    moveDown(1.5)
    sleep(5)

def reset():
    pydirectinput.moveTo(876, 641)
    pydirectinput.doubleClick(x=875, y= 640)
    pydirectinput.press('esc')
    pydirectinput.press('r')
    pydirectinput.press('enter')
    sleep(4)

def interact1():
    pydirectinput.press('e')
    pydirectinput.press('1')

def interact2():
    pydirectinput.press('e')
    pydirectinput.press('2')

def thirsty():
    moveUp(2)
    sleep(2)
    moveLeft(0.65)
    sleep(2)
    moveUp(0.3)
    interact1()
    moveLeft(1.5)
    interact1()
    pydirectinput.click(x=300, y=600)
    pydirectinput.press('1')
    for _ in range(5):
        sleep(2)
        pydirectinput.click(x=300, y=600)

def hungry():
    moveUp(2)
    sleep(2)
    moveLeft(0.5)
    sleep(2)
    moveUp(0.3)
    interact1()
    moveDown(0.3)
    moveRight(0.15)
    moveUp(0.1)
    interact1()
    sleep(0.5)
    pydirectinput.click(x=50, y=620)
    pydirectinput.press('1')
    for _ in range(3):
        sleep(3)
        pydirectinput.click(x=50, y=620)

def bed():
    moveUp(2)
    interact1()
    sleep(3)
    interact2()
    sleep(18)

def shower():
    moveUp(0.5)
    moveRight(0.5)
    interact2()
    moveUp(0.2)
    interact1()
    sleep(9)

def bored():
    moveLeft(0.5)
    interact2()
    moveDown(0.5)
    interact1()
    sleep(20)

def pizza():
    teleport('two', 770, 650)
    moveLeft(2.3)
    moveDown(3.3)
    moveRight(2.8)
    sleep(3)
    moveUp(2)
    sleep(60)

def salon():
    teleport('two', 770, 650)
    moveUp(0.5)
    sleep(0.3)
    moveLeft(5)
    sleep(3)
    moveUp(1.5)
    sleep(60)

def school():
    teleport('one', 770, 680)
    moveUp(1.4)
    moveLeft(4)
    sleep(3)
    moveUp(2)
    sleep(60)

def camping():
    teleport('one', 775, 790)
    moveUp(2.5)
    moveRight(15)
    moveUp(2)
    moveRight(9)
    moveDown(9)
    sleep(60)

def sick():
    teleport('one', 770, 680)
    moveUp(0.5)
    moveRight(3)
    moveDown(2.75)
    pydirectinput.keyDown('right')
    sleep(0.8)
    pydirectinput.keyUp('right')
    pydirectinput.keyDown('w')
    pydirectinput.press('space')
    pydirectinput.keyUp('w')
    moveUp(5)
    moveRight(4)
    moveUp(0.025)
    moveRight(1)
    pydirectinput.press('e')
    sleep(3.5)
    pydirectinput.moveTo(1051, 638)
    pydirectinput.click(x=1050, y=637)
    sleep(20)