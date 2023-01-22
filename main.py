from screencaputil import getTask
from actionsutil import *
from tkinter import *
import threading

root = Tk()
root.resizable(False, False)
root.title('Adopt Me')

def start():
    startButton['state'] = DISABLED
    count = 0
    while True:
        with runLock:
            if not run:
                return

        reset()
        task = getTask()
        match task:
            case "thirsty":
                thirsty()

            case "hungry":
                hungry()

            case "bed":
                bed()

            case "shower":
                shower()

            case "bored":
                bored()

            case "pizza":
                pizza()

            case "salon":
                salon()

            case "school":
                school()

            case "camping":
                camping()

            case "sick":
                sick()

        count += 1
        totalTasks = getTotalCompleted()
        with open('count.txt', 'w') as txt:
            totalTasks += 1
            txt.write(str(totalTasks))
        
        updateCounters(totalTasks, count)

def initiateStart():
    global run
    global runLock
    run = True
    runLock = threading.Lock()
    thread = threading.Thread(target=start, daemon=True)
    thread.start()

def updateCounters(totalComplete, currentComplete):
    totalCounter['text'] = f'Total Tasks Completed:   {totalComplete}'
    totalCounter['text'] = f'Current Tasks Completed:   {currentComplete}'

def stop():
    global run 
    startButton['state'] = NORMAL
    with runLock:
        run = False

def getTotalCompleted():
    with open('count.txt', 'r') as txt:
        return int(txt.readline())

buttonFrame = Frame(root)
buttonFrame.pack(side='right')
startButton = Button(buttonFrame, text='START', foreground='green', background='#5A5A5A', command=initiateStart)
startButton.pack(side = 'top', 
                 ipadx = 50,
                 ipady = 4,
                 padx= 5, 
                 pady= 1)
stopButton = Button(buttonFrame, text='STOP', foreground='yellow', background='#5A5A5A', command=stop)
stopButton.pack(side = 'top', 
                 ipadx = 53,
                 ipady = 4,
                 padx= 5, 
                 pady= 1)
quitButton = Button(buttonFrame, text='QUIT', foreground='red', background='#5A5A5A', command=quit)
quitButton.pack(side = 'bottom', 
                 ipadx = 54,
                 ipady = 4,
                 padx= 5, 
                 pady= 1)

counterFrame = Frame(root)
counterFrame.pack(side='left')
totalCounter = Label(counterFrame, font=('Times New Roman', 14), text=f'Total Tasks Completed:   {getTotalCompleted()}')
totalCounter.pack(side='top', padx=50)
currentCounter = Label(counterFrame, font=('Times New Roman', 14), text=f'Current Tasks Completed:   0')
currentCounter.pack(side='bottom')

root.mainloop()