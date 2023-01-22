from PIL import ImageGrab
import cv2
import numpy
from time import sleep
import os

# bounding box cords must be lower if in house due to house gui:
# odd  | default : (925, 30, 990, 100)    |   house : (925, 90, 990, 160)   
# even | default : (891, 30, 956, 100)    |   house : (891, 90, 956, 160) 
def getTaskOnScreen(x1, y1, x2, y2):
    screen = ImageGrab.grab(bbox = (x1, y1, x2, y2))
    screen.save(f'{os.getcwd()}\\imgs\\screen\\task.png')
    cvscreen = cv2.imread(f'{os.getcwd()}\\imgs\\screen\\task.png')
    cvscreen = cv2.cvtColor(cvscreen, cv2.COLOR_BGR2GRAY)
    return cvscreen

def getBackpackPage():
    page = ImageGrab.grab(bbox = (765, 850, 800, 880))
    page.save(f'{os.getcwd()}\\imgs\\backpackPage\\page.png')
    cvpage = cv2.imread(f'{os.getcwd()}\\imgs\\backpackPage\\page.png')
    cvpage = cv2.cvtColor(cvpage, cv2.COLOR_BGR2GRAY)
    currentPage = calculatErrorValues(cvpage, 'backpackReference')
    return(currentPage)

def calculateMeanSquaredError(img1, img2):
    height, width = img1.shape
    difference = cv2.subtract(img1, img2)
    error = numpy.sum(difference ** 2)
    mse = error / (float(height * width))
    return mse

def calculatErrorValues(screen, references):
    errorValues = []
    imgs = os.listdir(f'{os.getcwd()}\\imgs\\{references}')
    for img in imgs:
        cvimg = cv2.imread(f'{os.getcwd()}\\imgs\\{references}\\{img}')
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2GRAY)
        error = calculateMeanSquaredError(cvimg, screen)
        errorValues.append(error)
    best = min(errorValues)
    index = errorValues.index(best)
    item = imgs[index]
    return item[0:-5], best 

def getTask():
    while True:
        taskOnScreen = getTaskOnScreen(925, 90, 990, 160)
        task, error = calculatErrorValues(taskOnScreen, 'referenceTasks')
        if error < 1:
            break
        taskOnScreen = getTaskOnScreen(891, 90, 956, 160)
        task, error = calculatErrorValues(taskOnScreen, 'referenceTasks')
        if error < 1:
            break
        sleep(5)
    print(task)
    return task