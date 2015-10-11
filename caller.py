# This class holds the information of a CallerMacro

class caller():
    
    interArrivalTime = 0
    arrivalTime = 0
    whenAbleAvailable = 0
    whenBakerAvailable = 0
    serverChosen = 0   # 0 is able and 1 is baker
    serviceTime = 0
    timeServiceBegins = 0
    ableServiceCompletedTime = 0
    bakerServiceCompletedTime = 0
    callerDelay = 0
    timeInsystem = 0
    
    
    def __init__(self):