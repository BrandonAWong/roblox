import screencaputil
import actionsutil

def start():
    count = 0
    #while True:
    for _ in range(150):
        actionsutil.reset()
        task = screencaputil.getTask()
        count += 1
        print(str(count)+')', end=' ')
        match task:
            case "thirsty":
                actionsutil.thirsty()

            case "hungry":
                actionsutil.hungry()

            case "bed":
                actionsutil.bed()

            case "shower":
                actionsutil.shower()

            case "bored":
                actionsutil.bored()

            case "pizza":
                actionsutil.pizza()

            case "salon":
                actionsutil.salon()

            case "school":
                actionsutil.school()

            case "camping":
                actionsutil.camping()

            case "sick":
                actionsutil.sick()

start()
actionsutil.switchPets(990, 660, 1070, 765)

