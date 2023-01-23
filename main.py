from screencaputil import getTask
from actionsutil import *
from tkinter import *
import threading

root = Tk()
root.resizable(False, False)
root.title('Adopt Me')
root.wm_attributes("-topmost", 1)
root.geometry('590x150+0+0')

def start():
    count = 0
    while run:
        reset()
        task = getTask()
        taskLabel['text'] = f'Current Task:   {task}'
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
        taskLabel['text'] = f'Current Task:   waiting'
        updateCounters(totalTasks, count)
        if not run:
            startButton['state'] = NORMAL
            warning.pack_forget()

def initiateStart():
    global run
    startButton['state'] = DISABLED
    stopButton['state'] = NORMAL
    run = True
    thread = threading.Thread(target=start, daemon=True)
    thread.start()

def updateCounters(totalComplete, currentComplete):
    totalCounter['text'] = f'Total Tasks Completed:   {totalComplete}'
    currentCounter['text'] = f'Current Run:   {currentComplete}'

def stop():
    global run 
    stopButton['state'] = DISABLED
    run = False
    warning.pack(side='bottom')

def getTotalCompleted():
    with open('count.txt', 'r') as txt:
        return int(txt.readline())

buttonFrame = Frame(root)
buttonFrame.pack(side='right')
startButton = Button(buttonFrame, text='START', foreground='green', background='#5A5A5A', command=initiateStart)
startButton.pack(side = 'top', 
                 ipadx = 50,
                 ipady = 12,
                 padx= 5, 
                 pady= 1)
stopButton = Button(buttonFrame, text='STOP', foreground='yellow', background='#5A5A5A', state=DISABLED, command=stop)
stopButton.pack(side = 'top', 
                 ipadx = 53,
                 ipady = 12,
                 padx= 5, 
                 pady= 1)
quitButton = Button(buttonFrame, text='QUIT', foreground='red', background='#5A5A5A', command=quit)
quitButton.pack(side = 'bottom', 
                 ipadx = 54,
                 ipady = 12,
                 padx= 5, 
                 pady= 1)

labelFrame = Frame(root)
labelFrame.pack(side='left')
totalCounter = Label(labelFrame, font=('Yu Gothic UI', 18), text=f'Total Tasks Completed:   {getTotalCompleted()}')
totalCounter.pack(side='top', padx=50)
currentCounter = Label(labelFrame, font=('Yu Gothic UI', 18), text=f'Current Run:   0')
currentCounter.pack(side='top')
taskLabel = Label(labelFrame, font=('Yu Gothic UI', 18), text='Current Task:   waiting')
taskLabel.pack(side='top')
warning = Label(labelFrame, text='FINISHING LAST TASK BEFORE STOPPING', font=('Yu Gothic UI', 17), foreground='red')

root.mainloop()