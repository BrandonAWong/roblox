from PIL import ImageGrab
import os
def getTaskOnScreen(x1, y1, x2, y2):
    screen = ImageGrab.grab(bbox = (x1, y1, x2, y2))
    screen.save(f'{os.getcwd()}\\imgs\\screen\\task.png')

getTaskOnScreen(925, 90, 990, 160)